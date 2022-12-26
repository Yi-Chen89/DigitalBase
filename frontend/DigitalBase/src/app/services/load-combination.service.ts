import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";


const baseUrl = 'http://127.0.0.1:8080/calc';

@Injectable({providedIn: 'root'})
export class LoadCombinationService {

  constructor(private http: HttpClient) {}

  postLoadCaseData(data) {
    return this.http
      .post(
        baseUrl + '/loadcombination/',
        data,
      );
  }
}