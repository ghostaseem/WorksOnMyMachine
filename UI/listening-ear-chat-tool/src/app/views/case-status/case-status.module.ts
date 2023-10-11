import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CaseStatusComponent } from './case-status.component';
import { MatSidenavModule } from '@angular/material/sidenav';


@NgModule({
  declarations: [
    CaseStatusComponent
  ],
  imports: [
    BrowserModule,
    MatSidenavModule
  ],
  providers: [],
  bootstrap: [CaseStatusComponent]
})
export class CaseStatus { }
