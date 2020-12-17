name := "ModelarDB"
version := "1.0"
scalaVersion := "2.12"
scalacOptions ++= Seq("-optimise", "-feature", "-deprecation", "-Xlint:_")

resolvers += "Repo at github.com/ankurdave/maven-repo" at "https://github.com/ankurdave/maven-repo/raw/master"
resolvers += "Spark Packages Repo" at "https://dl.bintray.com/spark-packages/maven"
resolvers += "Bintray sbt plugin releases" at "https://dl.bintray.com/sbt/sbt-plugin-releases/"

libraryDependencies ++= Seq(
  "org.scala-lang" % "scala-compiler" % scalaVersion.value,
  "org.xerial" % "sqlite-jdbc" % "3.18.0",
  "com.datastax.spark" %% "spark-cassandra-connector" % "2.0.3",
  "amplab" % "spark-indexedrdd" % "0.4.0",
  "org.apache.spark" %% "spark-core" % "2.1.0" % "provided",
  "org.apache.spark" %% "spark-streaming" % "2.1.0" % "provided",
  "org.apache.spark" %% "spark-sql" % "2.1.0" % "provided",
  "com.eed3si9n" % "sbt-assembly" % "0.15.0")

run in Compile := Defaults.runTask(fullClasspath in Compile, mainClass in (Compile, run), runner in (Compile, run)).evaluated
