import { Component, OnInit } from '@angular/core';
import { FormArray, FormControl, FormGroup, Validators } from '@angular/forms';

import { SectionService } from '../services/section.service';
import { SteelGrades, SteelGrade, SteelSections, SteelSection } from '../models/sections.model';


@Component({
  selector: 'app-calc',
  templateUrl: './calc.component.html',
  styleUrls: ['./calc.component.css']
})
export class CalcComponent implements OnInit {

  inputForm: FormGroup;

  codes = ['AISC 360-05', 'AISC 360-10', 'AISC 360-16'];
  tension_check: boolean;
  compression_check: boolean;
  flexure_check: boolean;
  shear_check: boolean;
  torsion_check: boolean;

  steelSections: SteelSections[];
  steelSection: SteelSection;
  steelGrades: SteelGrades[];
  steelGrade: SteelGrade;
  length: number;
  length_show: boolean = true;

  load_cases = ['D', 'L', 'Lr'];

  F_y: number;
  F_u: number;
  E: number;

  A_g: number;

  tensionStrength: number;
  compressionStrength: number;
  flexureStrength: number;
  shearStrength: number;
  torsionStrength: number;

  tensionStrengthAC: string;
  flexureStrengthAC: string;
  
  outputMode: string = 'instruction';


  constructor(private sectionService: SectionService) { }

  ngOnInit(): void {
    this.inputForm = new FormGroup({
      'checks': new FormGroup({
        'code': new FormControl(null, Validators.required),
        'tensionCheck': new FormControl(true),
        'compressionCheck': new FormControl(true),
        'flexureCheck': new FormControl(true),
        'shearCheck': new FormControl(true),
        'torsionCheck': new FormControl(false),
      }),

      'section': new FormGroup({
        'sectionSize': new FormControl(null, Validators.required),
        'steelGrade': new FormControl(null, Validators.required),
        'length': new FormControl(0, Validators.required),
      }),

      'forces': new FormArray([
        new FormGroup({
          'case': new FormControl(null),
          'P': new FormControl(null), 
          'Vx': new FormControl(null),
          'Vy': new FormControl(null),
          'Mxx': new FormControl(null),
          'Myy': new FormControl(null),
          'T': new FormControl(null),
        })
      ]),
    });

    this.sectionService.fetchAllSteelSections()
      .subscribe(
        steelSections => {
          this.steelSections = steelSections;
        }
      );
    
    this.sectionService.fetchAllSteelGrades()
      .subscribe(
        steelGrades => {
          this.steelGrades = steelGrades;
        }
      );
    
    this.inputForm.get('checks').valueChanges
      .subscribe(
        value => {
          this.tension_check = value['tensionCheck'];
          this.compression_check = value['compressionCheck'];
          this.flexure_check = value['flexureCheck'];
          this.shear_check = value['shearCheck'];
          this.torsion_check = value['torsionCheck'];

          if (this.compression_check || this.flexure_check || this.torsion_check) {
            this.length_show = true;
          } else {
            this.length_show = false;
          }
        }
      );
    
    this.inputForm.get('section.sectionSize').valueChanges
      .subscribe(
        value => {
          if (value) {
            this.sectionService.fetchSteelSection(value)
            .subscribe(
              section => {
                this.inputForm.patchValue({
                  'section': {
                    'steelGrade': section['type']['preferred_steel']['id'],
                  }
                })
              }
            )
          }
        }
      );
  }

  onAddForce() {
    const group = new FormGroup({
      'case': new FormControl(null),
      'P': new FormControl(null), 
      'Vx': new FormControl(null),
      'Vy': new FormControl(null),
      'Mxx': new FormControl(null),
      'Myy': new FormControl(null),
      'T': new FormControl(null),
    });
    (<FormArray>this.inputForm.get('forces')).push(group);
  }

  onRemoveForce(index:number) {
    (<FormArray>this.inputForm.get('forces')).removeAt(index);
  }

  getForceControls() {
    return (<FormArray>this.inputForm.get('forces')).controls;
  }

  onSubmit() {
    this.outputMode = 'result';

    this.tension_check = this.inputForm.get('checks.tensionCheck').value;
    this.compression_check = this.inputForm.get('checks.compressionCheck').value;
    this.flexure_check = this.inputForm.get('checks.flexureCheck').value;
    this.shear_check = this.inputForm.get('checks.shearCheck').value;
    this.torsion_check = this.inputForm.get('checks.torsionCheck').value;

    const steel_grade_id = +this.inputForm.get('section.steelGrade').value;
    this.sectionService.fetchSteelGrade(steel_grade_id)
      .subscribe(
        steel => {
          this.F_y = steel['F_y'];
        }
      );

    const steel_section_id = +this.inputForm.get('section.sectionSize').value;
    this.sectionService.fetchSteelSection(steel_section_id)
      .subscribe(
        section => {
          this.A_g = section['A'];
        }
      );
    
    this.length = +this.inputForm.get('section.length').value;

    const inputData = {
      'checks': {
        'tensionCheck': this.tension_check,
        'compressionCheck': this.compression_check,
        'flexureCheck': this.flexure_check,
        'shearCheck': this.shear_check,
        'torsionCheck': this.torsion_check,
      },
      'steelSection': {
        'steelSectionId': steel_section_id,
        'steelGradeId': steel_grade_id,
        'length': this.length,
      },
      'forces': {
        'case': null,
        'P': null,
        'Vx': null,
        'Vy': null,
        'Mxx': null,
        'Myy': null,
        'T': null,
      }
    };

    this.sectionService.postSteelCalcData(inputData)
      .subscribe(
        response => {
          this.F_y = response['material']['F_y'];
          this.F_u = response['material']['F_u'];
          this.E = response['material']['E'];

          this.A_g = response['property']['A_g'];

          this.tensionStrength = response['result']['tension'];
          this.compressionStrength = response['result']['compression'];
          this.flexureStrength = response['result']['flexure'];
          this.shearStrength = response['result']['shear'];
          this.torsionStrength = response['result']['torsion'];

          this.tensionStrengthAC = response['result']['tension_ac'];
          this.flexureStrengthAC = response['result']['flexure_ac'];

          console.log(response);
        }
      );
  }

  onClearForm() {
    this.inputForm.patchValue({
      'checks': {
        'code': null,
      },
      'section': {
        'sectionSize': null,
        'steelGrade': null,
        'length': null,
      },
    });

    this.A_g = null;

    this.outputMode = 'instruction';
  }
}
