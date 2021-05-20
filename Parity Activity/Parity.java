import java.applet.Applet;
import java.awt.*;
public class Parity extends Applet {
	public void paint(Graphics g){
		//size is going to be 6 x 6
		g.setColor(Color.red);  
		int h = 20;
		int w = 20;
		int numRect = 6;
		for (int i = 0; i < numRect; i++){
			for (int j = 0; j < numRect; j++){
				g.drawRect(i*h, j*w, h, w);
			}
		}
		g.drawString("welcome", 150, 150);
	}
}