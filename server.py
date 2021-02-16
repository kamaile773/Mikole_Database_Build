"""Mikole party service application Flask server.

Provides web interface for browsing party services, seeing detail about party package and
assigns location, host and party package.
"""
from flask import Flask, render_template, redirect, flash, session
import jinja2
from model import connect_to_db

app = Flask(__name__)


@app.route("/")
def homepage():
    """Return homepage."""

    return render_template("homepage.html")

@app.route('/partypackages')
def all_party_packages():
    """View all Party Packages."""

    party_packages = crud.get_partypackages()

    return render_template('party_packages.html', partypackages=partypackages)

@app.route('/partypackages/<purchase_id>')
def show_partypackages(purchase_id):
    """Show details on a particular party package."""

    partypackages = crud.get_partypackages_by_id(purchase_id)

    return render_template('partypackages_details.html', partypackage=partypackage)

@app.route('/clients')
def all_clients():
    """View all clients."""

    clients = crud.get_clients()

    return render_template('all_clients.html', clients=clients)


@app.route('/clients/<client_id>')
def show_client(client_id):
    """Show details on a particular user."""

    client = crud.get_client_by_id(client_id)

    return render_template('client_details.html', client=client)

@app.route('/events')
def all_events():
    """View all events."""

    events = crud.get_events()

    return render_template('all_events.html', events=events)


@app.route('/events/<event_id>')
def show_event(event_id):
    """Show details on a particular event."""

    event = crud.get_event_by_id(event_id)

    return render_template('event_details.html', event=event)

@app.route('/locations')
def all_locations():
    """View all locations."""

    locations = crud.get_locations()

    return render_template('all_locations.html', locations=locations)


@app.route('/locations/<location_id>')
def show_location(location_id):
    """Show Location."""

    location = crud.get_location_by_id(location_id)

    return render_template('location_details.html', location=location)

@app.route('/')
def all_locations():
    """View all locations."""

    locations = crud.get_locations()

    return render_template('all_locations.html', locations=locations)


@app.route('/locations/<location_id>')
def show_location(location_id):
    """Show Location."""

    location = crud.get_location_by_id(location_id)

    return render_template('location_details.html', location=location)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# import jinja2
# from model import connect_to_db
# #import party packages

# app = Flask(__name__)

# # A secret key is needed to use Flask sessioning features
# app.secret_key = '//76ist5s67a88b%out78572get3848y88jiuyrks'
# app.jinja_env.undefined = jinja2.StrictUndefined


# @app.route("/cart") 
# def show_shopping_cart():
#     """Display content of shopping cart."""

#     # Keep track of the total cost of the order
#     order_total = 0

#     # Create a list to hold Melon objects corresponding to the melon_id's in
#     # the cart
#     cart_melons = []

#     # Get the cart dictionary out of the session (or an empty one if none
#     # exists yet)
#     cart = session.get("cart", {})

#     # Loop over the cart dictionary
#     for melon_id, quantity in cart.items():
#         # Retrieve the Melon object corresponding to this id
#         melon = melons.get_by_id(melon_id)

#         # Calculate the total cost for this type of melon and add it to the
#         # overall total for the order
#         total_cost = quantity * melon.price
#         order_total += total_cost

#         # Add the quantity and total cost as attributes on the Melon object
#         melon.quantity = quantity
#         melon.total_cost = total_cost

#         # Add the Melon object to our list
#         cart_melons.append(melon)

#     # Pass the list of Melon objects and the order total to our cart template

#     return render_template("cart.html",
#                            cart=cart_melons,
#                            order_total=order_total)


# @app.route("/add_to_cart/<melon_id>")
# def add_to_cart(melon_id):
#     """Add a melon to cart and redirect to shopping cart page.

#     When a melon is added to the cart, redirect browser to the shopping cart
#     page and display a confirmation message: 'Melon successfully added to
#     cart'."""

#     # Check if we have a cart in the session and if not, add one
#     # Also, bind the cart to the name 'cart' for easy reference below
#     if 'cart' in session:
#         cart = session['cart']
#     else:
#         cart = session['cart'] = {}

#     # We could also do this with setdefault:
#     # cart = session.setdefault("cart", {})

#     # Add melon to cart - either increment the count (if melon already in cart)
#     # or add to cart with a count of 1
#     cart[melon_id] = cart.get(melon_id, 0) + 1

#     # Print cart to the terminal for testing purposes
#     # print("cart:")
#     # print(cart)

#     # Show user success message on next page load
#     flash("Melon successfully added to cart.")

#     # Redirect to shopping cart page
#     return redirect("/cart")


# @app.route("/login", methods=["GET"])
# def show_login():
#     """Show login form."""

#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def process_login():
#     """Log user into site.

#     Find the user's login credentials located in the 'request.form'
#     dictionary, look up the user, and store them in the session.
#     """

#     # TODO: Need to implement this!

#     # The logic here should be something like:
#     #
#     # - get user-provided name and password from request.form
#     # - use customers.get_by_email() to retrieve corresponding Customer
#     #   object (if any)
#     # - if a Customer with that email was found, check the provided password
#     #   against the stored one
#     # - if they match, store the user's email in the session, flash a success
#     #   message and redirect the user to the "/melons" route
#     # - if they don't, flash a failure message and redirect back to "/login"
#     # - do the same if a Customer with that email doesn't exist

#     return "Oops! This needs to be implemented"


# @app.route("/checkout")
# def checkout():
#     """Checkout customer, process payment, and ship melons."""

#     # For now, we'll just provide a warning. Completing this is beyond the
#     # scope of this exercise.

#     flash("Sorry! Checkout will be implemented in a future version.")
#     return redirect("/melons")


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')