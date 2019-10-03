import java.net.*;

public class intReceiver {

	private final static int PACKETSIZE = 100 ;

	public static void main( String args[] ) { 
    // Check the arguments
    if (args.length != 2) {
      System.out.println( "usage: UDPReceiver port n" ) ;
      return ;
    }

    try {
      // Convert the argument to ensure that is it valid
      int port = Integer.parseInt( args[0] ) ;
      int n = Integer.parseInt( args[1] ) ;

      // Construct the socket
      DatagramSocket socket = new DatagramSocket(port);

      for(int i = 0; i < n; i++)
      {
        System.out.println("Receiving on port " + port) ;
        DatagramPacket packet = new DatagramPacket( new byte[PACKETSIZE], PACKETSIZE ) ;
        socket.receive( packet ) ;
				String message = new String(packet.getData()).trim();
        System.out.println( packet.getAddress() + " " + packet.getPort() + ": " +  message) ;
      }  
    } catch (Exception e) {
      System.out.println(e) ;
    }
  }
}

