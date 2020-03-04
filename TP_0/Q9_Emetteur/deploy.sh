rm tm/*_.java
javac tm/*a
mv tm/*s WEB-INF/classes/tm/
jar cvf Q9.war WEB-INF 
asadmin deploy --force Q9.war