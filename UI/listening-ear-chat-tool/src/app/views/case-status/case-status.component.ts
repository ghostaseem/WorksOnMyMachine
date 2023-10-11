import { Component } from '@angular/core';

@Component({
  selector: 'app-case-status',
  templateUrl: './case-status.component.html',
  styleUrls: ['./case-status.component.scss']
})

export class CaseStatusComponent {
  messages = 'I am a new message';
  isTrue = false;
  chat = false;
  caseStatus = [
    {id: 0, name: 'New - Unassigned', dropdown: false},
    {id: 1, name: 'Assigned', dropdown: true},
    {id: 1, name: 'Closed', dropdown: false},
  ]
  assignedStatus = [
    {id: 0, name: 'Active Chats'},
    {id: 1, name: 'Inactive Chats'},
  ]

  getMessages(status: string){
    if (status == 'New - Unassigned' ) {
      this.messages = 'I am a new message'
    } 
    else if (status == 'Assigned') {
      this.messages = 'I am an assigned message'
    }
    else if (status == 'Closed') {
      this.messages = 'I am a closed message'
    }
    else if (status == 'Active Chats') {
      this.messages = 'I am an active message'
    }
    else if (status == 'Inactive Chats') {
      this.messages = 'I am an inactive message'
    }
  }

  getDropdown() {
    this.isTrue = true
  }

  getChat() {
    this.chat = true
  }
}
