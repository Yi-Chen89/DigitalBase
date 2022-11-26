import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { ProjectComponent } from './project/project.component';
import { CalcComponent } from './calc/calc.component';
import { CalcListComponent } from './calc/calc-list/calc-list.component';
import { SteelCalcComponent } from './calc/steel-calc/steel-calc.component';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'project', component: ProjectComponent },
  { path: 'calc', component: CalcListComponent },
  { path: 'steelcalc', component: SteelCalcComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
