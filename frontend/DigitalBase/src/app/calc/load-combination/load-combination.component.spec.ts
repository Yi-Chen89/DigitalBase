import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoadCombinationComponent } from './load-combination.component';

describe('LoadCombinationComponent', () => {
  let component: LoadCombinationComponent;
  let fixture: ComponentFixture<LoadCombinationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoadCombinationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LoadCombinationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
