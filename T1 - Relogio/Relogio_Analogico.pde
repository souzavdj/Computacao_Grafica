void setup () {
  size(1000,1000);
  //rectMode(CENTER);
}

void draw () {
  float raio = 0.45*width;
  float raioPontosSegundos = raio*0.98;
  float raioPontosMinutos = raio*0.95;
  float raioPontosHoras = raio*0.92;
  float raioSegundos = raio*0.90;
  float raioMinutos = raio*0.70;
  float raioHoras = raio*0.50;
  float anguloSegundos = (second() * (PI/30)) - (PI/2);
  float anguloMinutos = (((minute()*60)+second()) * (PI/1800) ) - (PI/2);
  float anguloHoras = (((hour()*3600)+((minute()*60)+second())) * (PI/21600)) - (PI/2);
  background(255, 255, 255);
  translate(width/2, height/2);
  beginShape();
    strokeWeight(8);
    ellipse(0,0,2*raio,2*raio);
    strokeWeight(1);
    stroke (200, 200, 0);
    fill(200,200,0);
    ellipse(0,0,20,20);
    noFill();
    line(0,0,raioSegundos*cos(anguloSegundos),raioSegundos*sin(anguloSegundos));
    stroke (0);
    strokeWeight(4);
    line(0,0,raioMinutos*cos(anguloMinutos),raioMinutos*sin(anguloMinutos));
    strokeWeight(8);
    line(0,0,raioHoras*cos(anguloHoras),raioHoras*sin(anguloHoras));
    strokeWeight(1);
    for(int angulo = 0; angulo <= 360; angulo++){
      float anguloRadSegundos = (angulo * (PI/150));
      float anguloRadMinutos = (angulo*(PI/30));
      float anguloRadHoras = (angulo*(PI/6));
      line(raioPontosSegundos*cos(anguloRadSegundos),raioPontosSegundos*sin(anguloRadSegundos),raio*cos(anguloRadSegundos),raio*sin(anguloRadSegundos));
      strokeWeight(4);
      line(raioPontosMinutos*cos(anguloRadMinutos),raioPontosMinutos*sin(anguloRadMinutos),raio*cos(anguloRadMinutos),raio*sin(anguloRadMinutos));
      strokeWeight(8);
      line(raioPontosHoras*cos(anguloRadHoras),raioPontosHoras*sin(anguloRadHoras),raio*cos(anguloRadHoras),raio*sin(anguloRadHoras));
      strokeWeight(1);
    }
  endShape(CLOSE);
}
