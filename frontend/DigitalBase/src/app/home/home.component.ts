import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  // apps data should come from the server
  apps = [
    'project',
    'calc',
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
