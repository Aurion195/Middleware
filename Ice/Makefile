CXXFLAGS=-std=c++11 -I Serveur/H -DICE_CPP11_MAPPING

Annuaire : Serveur/O/Main.o Serveur/O/Launcher.o Serveur/O/IAnnuaire.o
	g++ -o Annuaire -g $^ -lIce++11 -lvlc -pthread

Serveur/O/Main.o : Serveur/C/Main.cpp
	g++ ${CXXFLAGS} -o Serveur/O/Main.o -c $<

Serveur/O/Launcher.o : Serveur/C/Launcher.cpp Serveur/H/Launcher.h
	g++ ${CXXFLAGS} -o Serveur/O/Launcher.o -c $<

Serveur/O/IAnnuaire.o : Serveur/C/IAnnuaire.cpp Serveur/H/IAnnuaire.h
	g++ ${CXXFLAGS} -o Serveur/O/IAnnuaire.o -c $<

ice :
	slice2cpp IAnnuaire.ice
	mv IAnnuaire.cpp Serveur/C
	mv IAnnuaire.h Serveur/H
	slice2py IAnnuaire.ice 
	mv IAnnuaire_ice.py Client/

clean : 
	rm Serveur/O/*

MrPropre : clean
	rm Annuaire