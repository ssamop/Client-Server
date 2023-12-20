# Client-Server
The project was divided into four milestones, each focusing on different aspects of the client-server model. The milestones were designed to explore various ways of implementing and utilizing the client-server architecture.

Project Description:

*Milestone 0:*

In Milestone 0, the goal is to build a chatting application using a client-server model. The application should have the following features:
  1. The client can initiate a chat with the server at any time.
  2. The server responds by echoing the message sent by the client in capitalized format.
  3. The connection between the client and server remains open until the client sends a message containing "CLOSE SOCKET," upon which the connection is closed.
  4. The chat connections are based on the TCP protocol.
Note: The server should continue running even if a client terminates, allowing subsequent clients to connect and chat with the server in Milestone 1.

Milestone 1: 
In Milestone 1, the objective is to extend the chatting application to support multiple clients and a single server. The application should have the following features:
1. The server should be able to communicate with multiple clients concurrently using threading.
2. The server should store client information such as connection socket and output stream using a suitable data structure (e.g., linked list, array).
3. Each client can initiate a chat with the server at any time.
4. The server responds by echoing the message sent by the corresponding client in capitalized format.
5. The connection between a client and the server remains open until the client sends a message containing "CLOSE SOCKET," upon which the connection is closed.
6. The chat connections continue to use the TCP protocol.
Note: You can use the provided client code or continue building upon the client code from Milestone 0. For the server side and implementing threading, you can refer to the provided hints or choose any other coding approach that you understand and prefer.


Milestone 2: This milestone aimed to optimize the client-server model for scalability and performance. The team implemented load balancing techniques to distribute incoming client requests across multiple servers, improving the system's responsiveness and resource utilization.

Milestone 3: The final milestone involved implementing advanced features in the client-server model. The team incorporated real-time communication capabilities, allowing clients to receive instant updates from the server. Additionally, they integrated a robust error handling mechanism to ensure fault tolerance and graceful recovery from failures.

Overall, the project explored different aspects of the client-server model, including basic communication, security, scalability, performance optimization, real-time updates, and error handling. Each milestone contributed to the development of a comprehensive and efficient client-server architecture.
