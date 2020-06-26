from utility.database.connection import Mongo
from services.transaction.models import Transaction, Transfer


mongo = Mongo()

if __name__ == "__main__":
    try:

        mongo.connect()

        numberdata = Transaction.objects.count()
        print("\nnumber of Transactions: ", numberdata)

        numberdata = Transfer.objects.count()
        print("\nnumber of Transfers: ", numberdata)

        postdata = Transaction.objects.first()
        print("\nfirst data of Transactions: ", postdata.to_json())
        print(postdata.created_date)

        postdata = Transfer.objects.first()
        print("\nfirst data of Transfers: ", postdata.to_json())

        exit(1)
    except Exception as e:

        print("Error! {}".format(e))
        exit(0)
