import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalclistComponent } from './calclist.component';

describe('CalclistComponent', () => {
  let component: CalclistComponent;
  let fixture: ComponentFixture<CalclistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalclistComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CalclistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
