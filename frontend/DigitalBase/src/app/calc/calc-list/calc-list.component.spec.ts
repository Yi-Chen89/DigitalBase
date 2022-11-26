import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalcListComponent } from './calc-list.component';

describe('CalcListComponent', () => {
  let component: CalcListComponent;
  let fixture: ComponentFixture<CalcListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalcListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CalcListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
