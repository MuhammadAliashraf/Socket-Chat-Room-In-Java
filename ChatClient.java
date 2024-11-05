import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ChatClient {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345)) { // Connect to the server on port 12345
            // Create input and output streams for communication with the server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Create a reader for user input from the console
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Connected to the chat server.");

            // Create a separate thread to listen for messages from the server
            new Thread(() -> {
                String serverMessage;
                try {
                    while ((serverMessage = in.readLine()) != null) {
                        System.out.println("Server: " + serverMessage);
                    }
                } catch (IOException e) {
                    System.out.println("Connection closed by server.");
                }
            }).start();

            // Send messages to the server
            String messageToSend;
            while ((messageToSend = userInput.readLine()) != null) {
                out.println(messageToSend);
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error connecting to the server.");
        }
    }
}
