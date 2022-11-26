import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-calc-list',
  templateUrl: './calc-list.component.html',
  styleUrls: ['./calc-list.component.css']
})
export class CalcListComponent implements OnInit {

  loadCalcs = {
    'DL Estimate': null,
    'LL Finder': null,
    'Seismic Load': null,
    'Wind Load': null,
  };
  steelCalcs = {
    'Section Finder': null,
    'Member Check': '/steelcalc',
  };
  concreteCalcs = {
    'Rebar Finder': null,
    'Member Check': null,
  };

  constructor() { }

  ngOnInit(): void {
  }

}
