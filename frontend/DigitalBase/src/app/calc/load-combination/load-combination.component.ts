import { Component, OnInit } from '@angular/core';
import { FormArray, FormControl, FormGroup, Validators } from '@angular/forms';

import { CodeService } from 'src/app/services/code.service';
import { LoadCombinationService } from 'src/app/services/load-combination.service';
import { ASCE7Version } from 'src/app/models/codes.model';


@Component({
  selector: 'app-load-combination',
  templateUrl: './load-combination.component.html',
  styleUrls: ['./load-combination.component.css']
})
export class LoadCombinationComponent implements OnInit {

  inputForm: FormGroup;

  ASCE7Versions: ASCE7Version[]

  LRFDCombination = null;
  ASDCombination = null;

  warning: boolean = false;
  warning_code: string = null;
  warning_method: string = null;

  outputMode: string = 'instruction';


  constructor(private codeService: CodeService, 
              private loadCombinationService: LoadCombinationService) { }

  ngOnInit(): void {
    this.inputForm = new FormGroup({
      'code': new FormGroup({
        'code': new FormControl(null, Validators.required),
        'LRFD': new FormControl(true),
        'ASD': new FormControl(true),
      }),

      'loadCase': new FormGroup({
        'D': new FormControl(true),
        // 'DSum': new FormControl(true),
        // 'DCases': new FormArray([
        //   new FormGroup({
        //     'name': new FormControl(null, Validators.required),
        //     'abbr': new FormControl(null, Validators.required),
        //   })
        // ]),
        'L': new FormControl(false),
        'T': new FormControl(false),
        'L_r': new FormControl(false),
        'S': new FormControl(false),
        'R': new FormControl(false),
        'W': new FormControl(false),
        'E': new FormControl(false),
      }),
    });

    this.codeService.fetchAllASCE7Versions()
      .subscribe(
        ASCE7Versions => {
          this.ASCE7Versions = ASCE7Versions;
        }
      );
    

    this.inputForm.valueChanges
      .subscribe(
        value => {
          this.outputMode = 'result';

          if (!value['code']['code']) {

            this.warning = true;
            this.warning_code = 'No code selected';

            if (!value['code']['LRFD'] && !value['code']['ASD']) {
              this.warning_method = 'No design method selected';
            }

          } else if (!value['code']['LRFD'] && !value['code']['ASD']) {

            this.warning = true;
            this.warning_code = null;
            this.warning_method = 'No design method selected';

          } else {

            this.warning = false;
            this.warning_code = null;
            this.warning_method = null;

            this.loadCombinationService.postLoadCaseData(value)
              .subscribe(
                response => {
                  this.LRFDCombination = response['LRFD']
                  this.ASDCombination = response['ASD']

                  console.log(response)
                }
              );
            console.log(value);
          }

        }
      );

  }

  onSubmit() {}

  onClearForm() {
    
    this.inputForm.patchValue({
      'code': {
        'code': null,
        'LRFD': true,
        'ASD': true,
      },
      'loadCase': {
        'D': true,
        'L': false,
        'T': false,
        'L_r': false,
        'S': false,
        'R': false,
        'W': false,
        'E': false,
      },
    });

    this.outputMode = 'instruction';
  }





  // getDCaseControls() {
  //   return (<FormArray>this.inputForm.get('loadCase').get('DCases')).controls;
  // }

  // onRemoveForce(index:number) {
  //   (<FormArray>this.inputForm.get('DCases')).removeAt(index);
  // }
}