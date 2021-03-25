// setting  up form options for website 

function optionList() {
    
    d3.json("../static/js/uniques.json").then( rawData => {

        //console.log("reading json");
        var typeNames = rawData.type;
        var manufacturerNames = rawData.manufacturer;
        var fuelNames = rawData.fuel;
        var transmissionNames = rawData.transmission;
        var driveNames = rawData.drive;


        //console.log(rawData);
        //console.log(typeNames);

        //adding options to vehicle type dropdown menu
        var TypedropdownMenu = d3.selectAll(".vehicleType");
        
        for (i=0; i<typeNames.length; i++) {
            TypedropdownMenu.append("option")
                        .text(typeNames[i])
                        .attr("value", typeNames[i])
        };

        //adding options to manufacturer type dropdown menu
        var ManudropdownMenu = d3.selectAll(".carManufacturer");
        
        for (i=0; i<manufacturerNames.length; i++) {
            ManudropdownMenu.append("option")
                        .text(manufacturerNames[i])
                        .attr("value", manufacturerNames[i])
        };

        //adding options to fuel type dropdown menu
        var fueldropdownMenu = d3.selectAll(".fuelType");
        
        for (i=0; i<fuelNames.length; i++) {
            fueldropdownMenu.append("option")
                        .text(fuelNames[i])
                        .attr("value", fuelNames[i])
        };

        //adding options to transmission type dropdown menu
        var transmissiondropdownMenu = d3.selectAll(".transmission");
        
        for (i=0; i<transmissionNames.length; i++) {
            transmissiondropdownMenu.append("option")
                        .text(transmissionNames[i])
                        .attr("value", transmissionNames[i])
        };

        //adding options to drive type dropdown menu
        var drivedropdownMenu = d3.selectAll(".drive");
        
        for (i=0; i<driveNames.length; i++) {
            drivedropdownMenu.append("option")
                        .text(driveNames[i])
                        .attr("value", driveNames[i])
        };


    });

};

optionList();
