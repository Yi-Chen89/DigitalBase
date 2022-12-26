import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

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
    

    this.inputForm.get('loadCase').valueChanges
      .subscribe(
        value => {
          this.loadCombinationService.postLoadCaseData(value)
            .subscribe(
              response => {
                this.LRFDCombination = response['LRFD']
                this.ASDCombination = response['ASD']
              }
            );
          console.log(value);
        }
      );
  }

  onSubmit() {}

  onClearForm() {}
}
