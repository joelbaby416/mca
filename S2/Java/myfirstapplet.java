
import java.applet.*;
import java.awt.*;


public class myfirstapplet extends Applet{
	public void paint(Graphics g) {
		g.drawLine(20, 20, 200, 20);
		g.drawRect(20, 60, 200, 40);
		g.drawOval(20, 120, 200, 160);
	}

}

 /* 
<applet code="myfirstapplet.class" width="500" height="700" border="2"> 
</applet> 
*/  
