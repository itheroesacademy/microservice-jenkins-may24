
FROM maven:3.6.3-jdk-11 AS build

WORKDIR /app

COPY pom.xml .
RUN mvn dependency:go-offline -B

COPY src ./src
RUN mvn package -DskipTests

EXPOSE 1002

ENTRYPOINT ["java", "-jar", "app.jar"]
