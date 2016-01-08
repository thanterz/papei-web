jQuery.ajax({
	url: "http://www.theama.info/curbweb/api/api/menu/?format=json",
	type: "GET",
	contentType: 'application/json; charset=utf-8',
	success: function(resultData) {
		$.each( resultData, function( key, value ) {
			if(key == 4)
				$( ".data" ).append( "<center>"+value.title+"</center>" );        
		});     

	},
	error : function(jqXHR, textStatus, errorThrown) {
	},

	timeout: 120000,
});

function validate_form()
{
	// Παίρνουμε τις τιμές των html στοιχείων της φόρμας ανάλογα με το id τους
	var firstname = document.getElementById('firstname').value;
	var lastname = document.getElementById('lastname').value;
	var email = document.getElementById('email').value;
	var tel = document.getElementById('tel').value;
	var message = document.getElementById('message').value;

	// Δημιουργούμε ένα μήνυμα σε περίπτωση που ο χρήστης δεν έχει συμπληρώσει κάποιο από τα πεδία της φόρμας
	var msg = "Δεν έχετε συμπληρώσει τα παρακάτω πεδία\n";

	if (blank(firstname)) {
		msg = msg + "- Όνομα\n";
	}

	if (blank(lastname)) {
		msg = msg + "- Επώνυμο\n";
	}

	if (blank(email)) {
		msg = msg + "- Email\n";
	}
	else if (!email.match(/(\w+)@(.+)\.(\w+)$/)) { // Ελέγχουμε με κατάλληλο regular expression αν η τιμή του mail έχει έγκυρη μορφή. Για περισσότερες λεπτομέρειες, μπορεί να ανατρέξει κανείς στο google με αναζήτηση 'regular expressions javascript' 
		msg = msg + "- Το e-mail δεν είναι έγκυρο\n";
	}
	
	if (blank(tel)) {
		msg = msg + "- Τηλέφωνο\n";
	}
	
	if (blank(message)) {
		msg = msg + "- Μήνυμα\n";
	}

	if (msg!="Δεν έχετε συμπληρώσει τα παρακάτω πεδία\n") {
		alert ( msg );
		return false;
	}

	return true;
}


// Η συνάρτηση αυτή επιστρέφει 1 αν η τιμή του x είναι κενή, 0 σε διαφορετική περίπτωση
function blank ( x )
{
	 var length = x.length; // Αποθηκεύουμε τον αριθμό των χαρακτήρων
	 var result = 1;

	for (i = 1;i <= length;i++)
	{
		if (x.charAt(i-1) != " ") { // Διατρέχουμε έναν έναν χαρακτήρα και αν υπάρχει έστω ένας που ΔΕΝ είναι ο κενός, επιστρέφουμε 0
			
			result = 0;
			break;
		}
	} 
	return result;
}
