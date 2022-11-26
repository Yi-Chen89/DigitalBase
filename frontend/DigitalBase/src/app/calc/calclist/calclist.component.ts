import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-calclist',
  templateUrl: './calclist.component.html',
  styleUrls: ['./calclist.component.css']
})
export class CalclistComponent implements OnInit {

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
