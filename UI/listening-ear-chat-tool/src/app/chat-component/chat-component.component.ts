import { Component } from '@angular/core';
import { webSocket } from 'rxjs/webSocket'

@Component({
  selector: 'app-chat-component',
  templateUrl: './chat-component.component.html',
  styleUrls: ['./chat-component.component.scss']
})
export class ChatComponentComponent {
  chatOpen: boolean = false;
  message: string = '';
  isChatOpen = false;
  sentMessages: string[] = [];
  ws = new WebSocket("ws://localhost:8000/ws");

  constructor(){
    this.ws.onmessage = (event) => {
    this.sentMessages.push(event.data)
 };
  }
   

  openChat() {
    this.isChatOpen = true;
  }

  handleButtonClick(buttonName: string): void {
    // Implement the desired logic for each button
    switch (buttonName) {
      case 'Chat 1':
        // Handle the action for Button 1
        console.log('Button 1 clicked');
        break;
      case 'Chat 2':
        // Handle the action for Button 2
        console.log('Button 2 clicked');
        break;
      case 'Chat 3':
        // Handle the action for Button 3
        console.log('Button 3 clicked');
        break;
      default:
        break;
    }
  }

  // Correct
toggleChatBox(): void {
  this.chatOpen = !this.chatOpen;
  console.log(this.chatOpen)
}

sendMessage(): void {
  // var input = this.message
  // this.ws.send(input)
  if (this.message.trim() !== '') {
    this.sentMessages.push(this.message); // Add the message to the sent messages

    console.log('Message sent:', this.message);
    this.message = '';
  }

  // this.ws.onmessage = function(event) {
  //   var messages = document.getElementById('messages')
  //   var message = document.createElement('li')
  //   var content = document.createTextNode(event.data)
  //   message.appendChild(content)
  //   messages.appendChild(message)
  // }

}



}