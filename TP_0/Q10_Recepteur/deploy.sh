rm tm/*_.java
javac tm/*a
mv tm/*s WEB-INF/classes/tm/
jar cvf Q10.war WEB-INF/ index.html
asadmin deploy --force Q10.war