
import java.io.*;
import java.net.*;

public class ChatServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) { // Server will listen on port 12345
            System.out.println("Server started, waiting for client...");

            Socket clientSocket = serverSocket.accept(); // Wait for a connection
            System.out.println("Client connected!");

            // Set up input and output streams
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

            // Separate thread to listen for messages from client
            new Thread(() -> {
                try {
                    String message;
                    while ((message = in.readLine()) != null) {
                        System.out.println("Client: " + message);
                    }
                } catch (IOException e) {
                    System.out.println("Client disconnected.");
                }
            }).start();

            // Main thread to send messages to the client
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            String messageToSend;
            while ((messageToSend = userInput.readLine()) != null) {
                out.println(messageToSend);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
