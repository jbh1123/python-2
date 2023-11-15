class Invoice:

    def __init__(self, in_id, user_id, amount, paid) -> None:
        self.invoice_id = in_id
        self.user_id = user_id
        self.amount = amount
        self.paid = paid

    def __repr__(self) -> str:
        return f"Invoice(invoice_id='{self.invoice_id}', user_id='{self.user_id}', amount='{self.amount}', paid='{self.paid}')"
    
    @staticmethod
    def generate_list_of_invoices(list_of_strings):
        resulting_list = []
        for invoice_string in list_of_strings:
            fields = invoice_string.split(', ')
            resulting_list.append(Invoice(fields[0], fields[1], fields[2], fields[3]))
        return resulting_list