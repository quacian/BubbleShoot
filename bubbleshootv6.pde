void setup(){
 
 size(700,800);
 frameRate(28);
//noLoop(); //no flashing colours
}

int ax = 355;
int ay = 527;
float distance;
float theta;
float circleX, circleY;
float circleSpeed = 7;
float shootAngle = PI / 2; // starting shooting angle position
boolean mousePressedMove = false;

void draw() {
  background(#FAB1F3);
 
  
  int noofCircles = 10;
  float circleSize = 26; // this makes the circle bigger w/ increase in integer
  float centreX = width / 2;
  float centreY = 50;
  float Spacing = 2 * circleSize; 
  float positionAmount = 70;


  //array for specific colours of bubbles
  
  color[] circleColors = {
    color(#FF4350),    // red
    color(#2BE04D),    // green
    color(#79F3FF),    // blue
    color(#FFE200),  // yellow
    color(#FF03D6)   // pink
  };
  
  int count = 0;
  // adjust no. of rows
  for (int row = 0; row < 5; row++) { 
  for ( int spacing = 0; spacing < noofCircles; spacing++) {
    float x = spacing * ( 2 * circleSize + 10) + positionAmount;
    float y = centreY + row * Spacing;
    
    // random colour selector from my combination
    //fill(circleColors[int(random(circleColors.length))]);
    fill(circleColors[count]);
    noStroke();
    count++;
    if(count>4){
     count = 0; 
    }
    ellipse(x, y, circleSize * 2, circleSize * 2);
  }    
  }

 //hearts
fill(#F03F3F);
beginShape();
vertex(36,761);
vertex(37,760);
vertex(38,760);
vertex(40,759);
vertex(40,758);
vertex(42,758);
vertex(42,757);
vertex(46,757);
vertex(46,758);
vertex(49,758);
vertex(49,759);
vertex(50,759);
vertex(51,759);
vertex(52,762);
vertex(52,764);
vertex(53,764);
vertex(53,771);
vertex(52,771);
vertex(52,773);
vertex(51,773);
vertex(51,775);
vertex(50,775);
vertex(50,777);
vertex(49,777);
vertex(49,778);
vertex(48,778);
vertex(48,780);
vertex(47,780);
vertex(47,781);
vertex(46,781);
vertex(46,782);
vertex(44,782);
vertex(44,783);
vertex(43,783);
vertex(43,784);
vertex(42,784);
vertex(42,785);
vertex(40,785);
vertex(40,786);
vertex(38,786);
vertex(38,787);
vertex(35,787);
vertex(35,786);
vertex(33,786);
vertex(33,785);
vertex(31,785);
vertex(31,784);
vertex(30,784);
vertex(30,783);
vertex(29,783);
vertex(29,782);
vertex(28,782);
vertex(28,781);
vertex(27,781);
vertex(27,780);
vertex(26,780);
vertex(26,779);
vertex(25,779);
vertex(25,778);
vertex(24,778);
vertex(24,777);
vertex(23,777);
vertex(23,775);
vertex(22,775);
vertex(22,773);
vertex(21,773);
vertex(21,770);
vertex(20,770);
vertex(20,764);
vertex(21,764);
vertex(21,762);
vertex(22,762);
vertex(22,760);
vertex(23,760);
vertex(23,759);
vertex(24,759);
vertex(24,758);
vertex(27,757);
vertex(31,757);
vertex(31,758);
vertex(34,758);
vertex(34,759);
vertex(35,759);
vertex(35,760);
vertex(36,760);
vertex(36,761);
endShape(CLOSE);



beginShape();
vertex(78,761);
vertex(79,761);
vertex(79,760);
vertex(80,760);
vertex(80,759);
vertex(82,759);
vertex(82,758);
vertex(84,758);
vertex(84,757);
vertex(88,757);
vertex(88,758);
vertex(91,758);
vertex(91,759);
vertex(92,759);
vertex(92,760);
vertex(93,760);
vertex(93,762);
vertex(94,762);
vertex(94,764);
vertex(95,764);
vertex(95,771);
vertex(94,773);
vertex(93,773);
vertex(93,775);
vertex(92,775);
vertex(92,777);
vertex(91,778);
vertex(90,778);
vertex(90,780);
vertex(89,780);
vertex(89,781);
vertex(88,782);
vertex(86,782);
vertex(86,783);
vertex(85,783);
vertex(85,784);
vertex(84,784);
vertex(84,783);
vertex(82,785);
vertex(82,786);
vertex(80,786);
vertex(80,787);
vertex(77,787);
vertex(77,786);
vertex(75,786);
vertex(75,785);
vertex(73,785);
vertex(73,784);
vertex(72,784);
vertex(72,783);
vertex(71,783);
vertex(71,782);
vertex(70,782);
vertex(70,781);
vertex(69,781);
vertex(69,780);
vertex(68,780);
vertex(68,779);
vertex(67,779);
vertex(67,778);
vertex(66,778);
vertex(66,777);
vertex(65,777);
vertex(65,775);
vertex(64,775);
vertex(64,773);
vertex(63,770);
vertex(63,762);
vertex(64,762);
vertex(65,760);
vertex(65,759);
vertex(66,759);
vertex(66,758);
vertex(69,758);
vertex(69,757);
vertex(73,757);
vertex(73,758);
vertex(76,758);
vertex(76,759);
vertex(77,760);
vertex(78,760);
vertex(78,761);
endShape(CLOSE);

beginShape();
vertex(120,761);
vertex(121,761);
vertex(121,761);
vertex(121,760);
vertex(122,760);
vertex(122,759);
vertex(124,759);
vertex(124,758);
vertex(126,758);
vertex(126,757);
vertex(130,757);
vertex(130,758);
vertex(133,758);
vertex(133,759);
vertex(134,759);
vertex(134,760);
vertex(135,760);
vertex(135,762);
vertex(136,764);
vertex(137,764);
vertex(137,771);
vertex(136,771);
vertex(136,773);
vertex(135,773);
vertex(135,775);
vertex(134,775);
vertex(134,777);
vertex(133,777);
vertex(133,778);
vertex(132,780);
vertex(131,780);
vertex(131,781);
vertex(130,781);
vertex(130,782);
vertex(128,782);
vertex(128,783);
vertex(127,783);
vertex(127,784);
vertex(126,784);
vertex(126,785);
vertex(124,785);
vertex(124,786);
vertex(122,786);
vertex(122,787);
vertex(119,787);
vertex(119,786);
vertex(117,786);
vertex(117,785);
vertex(115,785);
vertex(115,784);
vertex(114,784);
vertex(114,783);
vertex(113,783);
vertex(113,782);
vertex(112,782);
vertex(112,781);
vertex(111,781);
vertex(111,780);
vertex(110,780);
vertex(110,779);
vertex(109,779);
vertex(109,778);
vertex(108,778);
vertex(108,777);
vertex(107,777);
vertex(107,775);
vertex(106,775);
vertex(106,773);
vertex(105,773);
vertex(105,770);
vertex(104,770);
vertex(104,764);
vertex(105,764);
vertex(105,762);
vertex(106,760);
vertex(107,760);
vertex(107,759);
vertex(108,759);
vertex(108,758);
vertex(111,758);
vertex(111,757);
vertex(115,757);
vertex(115,758);
vertex(118,758);
vertex(118,759);
vertex(119,759);
vertex(119,760);
vertex(120,760);
vertex(120,761);
endShape(CLOSE);
















fill(#811578);
noStroke();
rect(234,680,234,40);

fill(#FF03D6);
noStroke();
circle(355,660,40);






stroke(0);
strokeWeight (2.5);
//When the mouse is behind the line
if(mouseY>=ay+109 && mouseX>ax){
 line(ax,ay+109,ax+100,ay+109);//draw horizontal line right
 line(ax+100,ay+109,ax+75,ay+99);
 line(ax+100,ay+109,ax+75,ay+119);
}
if(mouseY>=ay+109 && mouseX<ax){
 line(ax,ay+109,ax-100,ay+109);//draw horizontal line left
 line(ax-100,ay+109,ax-75,ay+99);
 line(ax-100,ay+109,ax-75,ay+119);
}
if(ax - mouseX != 0){//prevents divison by 0
if(mouseY<ay+109 && mouseX>ax){//if mouse is above and right
  distance = dist(mouseX,mouseY,ax,ay+109);//calculate distance to mouse
  theta = acos((ay+109-mouseY)/distance);//calculate angle between mouse and vertical
  pushMatrix();//store grid
  translate(ax,ay+109);//move grid
  rotate((3*PI/2)+theta);//rotate grd
  line(0,0,100,0);//draw line
  line(100,0,75,10);
  line(100,0,75,-10);
  popMatrix();//restore grid
}
if(mouseY<ay+109 && mouseX<ax){//if mouse is above left
  distance = dist(mouseX,mouseY,ax,ay+109);//calculate distance to mouse
  theta = acos((ay+109-mouseY)/distance);//calculate angle between mouse and vertical
  pushMatrix();//store grid
  translate(ax,ay+109);//move grid
  rotate((3*PI/2)-theta);//rotate grd
  line(0,0,100,0);//draw line
  line(100,0,75,10);
  line(100,0,75,-10);
  popMatrix();//restore grid
}
}

if (mousePressedMove) {
  fill(255,0,0); //its red rn but make sure to try and make the colour randomise when shoot
  noStroke();
  ellipse(circleX, circleY, 43, 43);
  circleX += circleSpeed * cos(shootAngle);
  circleY += circleSpeed * sin(shootAngle);
  
  //make sure the circle shoots in the correct direction
  if (circleY < 0) {
    mousePressedMove = false; //stop drawing the circle (1)
  }
  
  if (circleY > height) {
    mousePressedMove = false; //stop drawing the circle (2)
  }
  
  if (circleX < 0) {
    mousePressedMove = false; //stop drawing the circle (3)
  }
  
  if (circleX > width) {
    mousePressedMove = false; //stop drawing the circle (4)
  }
 }
}

void mousePressed() {
  mousePressedMove = true;
  circleX = ax;
  circleY = ay + 109;
  
  // shooting angle is based on mouse position + arrow position so we calculate it
  
  distance = dist(mouseX, mouseY, ax, ay + 109);
  theta = acos ((ay + 109 - mouseY) / distance);
  if (mouseX < ax) {
    shootAngle = (3 * PI / 2) - theta;
  } else {
    shootAngle = (3 * PI / 2) + theta;
  }
}
  
  
  
  
  
  
