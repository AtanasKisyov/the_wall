Wall API

Input:

api_app/files/config.txt 

Contains information of each profile on a separate line and height separated by space.


Endpoints:

GET /profiles/{int}/days/{int} // Returns JSON with needed ice for the specified profile and specified day

GET /profiles/{int}/overview/{int} // Returns JSON with needed gold for the specified profile and specified day

GET /profiles/overview/{int} // Returns JSON with needed gold for all profiles and specified day

GET /profiles/overview // Returns JSON with needed gold to finish the wall

JSON example:

{

    "day": {int},
    "ice_amount": {int},
}

or

{

    "day": {int}, # or None if endpoint is /profiles/overview
    "cost": {int},
}
