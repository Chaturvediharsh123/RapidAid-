def route_department(issue):

    routing_map = {

        "Road Damage": "Public Works Department",
        "Waste Management": "Municipal Sanitation Department",
        "Water Supply": "Water Authority",
        "Electricity Failure": "Electricity Board",

        "Fire Emergency": "Fire Department",
        "Accident": "Traffic Police"
    }

    return routing_map.get(issue, "Municipal Office")