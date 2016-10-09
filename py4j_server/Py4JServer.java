import py4j.GatewayServer;
import java.io.*;

public class Py4JServer {

    public static void main(String[] args) {
        int port;
        if (args.length == 0) {
            System.err.println("You must specify a port number.");
            System.exit(1);
        }
        port = Integer.parseInt(args[0]);
        GatewayServer gatewayServer = new GatewayServer(new Py4JServer(),
                                                        port);
        gatewayServer.start();
        /* Print out the listening port so that clients can discover it. */
        int listening_port = gatewayServer.getListeningPort();
        System.out.println("" + listening_port);
        System.out.println("Py4J Gateway Server started on port " +
            listening_port);

        /* Exit on EOF or broken pipe.  This ensures that the server dies if
         * the program that launched the server dies. */
        BufferedReader stdin = new BufferedReader(
                               new InputStreamReader(System.in));
        try {
            stdin.readLine();
            System.exit(0);
        } catch (java.io.IOException e){
            System.exit(0);
        }
    }
}
