import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { map } from 'rxjs/operators';

import { SteelGrades, SteelGrade, SteelSections, SteelSection } from "../models/sections.model";


const baseUrl = 'http://127.0.0.1:8080/calc';

@Injectable({providedIn: 'root'})
export class SectionService {

  constructor(private http: HttpClient) {}
    
  fetchAllSteelGrades() {
    return this.http
      .get(
        baseUrl + '/steelgrades/',
      )
      .pipe(
        map(responseData => {
          let allSteelGrades: SteelGrades[] = [];
          for (let key in responseData) {
            const steelGrade: SteelGrades = responseData[key];
            allSteelGrades.push({'id': steelGrade['id'], 'name': steelGrade['name']});
          }
          return allSteelGrades;
        })
      );
  }
  
  fetchSteelGrade(id: number) {
    return this.http
      .get(
        baseUrl + '/steelgrade/' + id,
      );
  }
  
  
  fetchAllSteelSections() {
    return this.http
      .get(
        baseUrl + '/steelsections/',
      )
      .pipe(
        map(responseData => {
          let allSteelSections: SteelSections[] = [];
          for (let key in responseData) {
            const steelSection: SteelSections = responseData[key];
            allSteelSections.push({'id': steelSection['id'], 'name': steelSection['name']});
          }
          return allSteelSections;
        })
      );
  }
  
  fetchSteelSection(id: number) {
    return this.http
      .get(
        baseUrl + '/steelsection/' + id,
      );
  }
  
  
  postSteelCalcData(data) {
    return this.http
      .post(
        baseUrl + '/steelcalc',
        data,
      );
  }
}