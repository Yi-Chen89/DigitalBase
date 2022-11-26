import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { ProjectComponent } from './project/project.component';
import { CalcComponent } from './calc/calc.component';
import { CalclistComponent } from './calc/calclist/calclist.component';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'project', component: ProjectComponent },
  { path: 'steelcalc', component: CalcComponent },
  { path: 'calc', component: CalclistComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
