import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'listening-ear-chat-tool';
  text = "Open"
  isChatOpen = false;

  openChat() {
    if(this.isChatOpen == false){
      this.isChatOpen = true;
      this.text = "Close"
    }
    else{
      this.isChatOpen = false;
      this.text = "Open"
    }
    
  }
}
