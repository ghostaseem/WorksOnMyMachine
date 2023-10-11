import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket: WebSocket;
  public messages: string[] = [];

  constructor() {
    // Initialize the WebSocket connection
    this.socket = new WebSocket('ws://localhost:8000/ws'); // Replace with your WebSocket URL

    // Handle WebSocket messages
    this.socket.onmessage = (event) => {
      this.messages.push(event.data);
    };

    this.socket.onopen = (event) =>{
      console.log("Connection Established")
    }
  }

  sendMessage(message: string): void {
    // Send a message through the WebSocket connection
    this.socket.send(message);
  }

  closeConnection(): void {
    // Close the WebSocket connection when needed
    this.socket.close();
  }
}

