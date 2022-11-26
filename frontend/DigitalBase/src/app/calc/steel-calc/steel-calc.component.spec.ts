import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SteelCalcComponent } from './steel-calc.component';

describe('SteelCalcComponent', () => {
  let component: SteelCalcComponent;
  let fixture: ComponentFixture<SteelCalcComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SteelCalcComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SteelCalcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
