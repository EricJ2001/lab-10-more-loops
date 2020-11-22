!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <script>
      var maximum_stories = 10;
      var userstring = prompt("on what floor of the building is your office?");
      var usernum = parsetInt(userstring, 10);

      while (usernum > maximum_stories) {
        console.log("you entered: " + usernum + "but there are only " + maximum_stories + floors in this building.);
        var userstring = prompt(you entered: " + usernum + "but there are only " + maximum_stories + floors in this building.);
        var usernum = parsetInt(userstring, 10);

      }

      console.log("Congrats! You work on: " + usernum)

   </script>
  </body>
</html>
