import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { map } from 'rxjs/operators';

import { ASCE7Version } from "../models/codes.model";


const baseUrl = 'http://127.0.0.1:8080/calc';

@Injectable({providedIn: 'root'})
export class CodeService {

  constructor(private http: HttpClient) {}
    
  fetchAllASCE7Versions() {
    return this.http
      .get(
        baseUrl + '/asce7versions/',
      )
      .pipe(
        map(responseData => {
          let allASCE7Versions: ASCE7Version[] = [];
          for (let key in responseData) {
            const ASCE7Version: ASCE7Version = responseData[key];
            allASCE7Versions.push({'id': ASCE7Version['id'], 'name': ASCE7Version['name']});
          }
          return allASCE7Versions;
        })
      );
  }
}