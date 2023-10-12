import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CaseStatusComponent } from './case-status.component';
import { MatSidenavModule } from '@angular/material/sidenav';
import { ChatComponentComponent } from '../../chat-component/chat-component.component';


@NgModule({
  declarations: [
    CaseStatusComponent,
    ChatComponentComponent
  ],
  imports: [
    BrowserModule,
    MatSidenavModule
  ],
  providers: [],
  bootstrap: [CaseStatusComponent]
})
export class CaseStatus { }
