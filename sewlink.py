# ============================================================
# SEWLINK TAILORING MARKETPLACE MANAGEMENT SYSTEM
# Single-file terminal-based management system using Python OOP.
# ============================================================

class Customer:
    """Represents a client requesting tailoring services."""
    def __init__(self, customer_id, name, phone, email, location):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location

    def display(self):
        print(f"[{self.customer_id}] Name: {self.name} | Phone: {self.phone} | Email: {self.email} | Location: {self.location}")


class Tailor:
    """Represents a tailor providing sewing/design services."""
    def __init__(self, tailor_id, name, phone, email, location, specialization):
        self.tailor_id = tailor_id
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location
        self.specialization = specialization

    def display(self):
        print(f"[{self.tailor_id}] Name: {self.name} | Spec: {self.specialization} | Phone: {self.phone} | Location: {self.location}")


class Job:
    """Represents a tailoring job posted by a customer."""
    def __init__(self, job_id, customer_id, title, description, category, budget):
        self.job_id = job_id
        self.customer_id = customer_id
        self.title = title
        self.description = description
        self.category = category
        self.budget = budget
        self.tailor_id = None
        self.status = "Open"  # Open, Accepted, Rejected, In Progress, Completed, Cancelled

    def display(self):
        tailor_str = self.tailor_id if self.tailor_id else "Unassigned"
        print(f"[{self.job_id}] Title: {self.title} | Cat: {self.category} | Budget: ${self.budget:.2f} | Status: {self.status} | Customer: {self.customer_id} | Tailor: {tailor_str}")
        print(f"    Description: {self.description}")


class Message:
    """Represents direct communication between users."""
    def __init__(self, message_id, sender, receiver, content):
        self.message_id = message_id
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def display(self):
        print(f"[{self.message_id}] From: {self.sender} -> To: {self.receiver}")
        print(f"    Content: {self.content}")


class Order:
    """Represents an active transactional order created from an accepted job."""
    def __init__(self, order_id, job_id, customer_id, tailor_id, agreed_price):
        self.order_id = order_id
        self.job_id = job_id
        self.customer_id = customer_id
        self.tailor_id = tailor_id
        self.agreed_price = agreed_price
        self.status = "Created"  # Created, In Progress, Ready, Completed, Cancelled

    def display(self):
        print(f"[{self.order_id}] Job ID: {self.job_id} | Customer: {self.customer_id} | Tailor: {self.tailor_id} | Price: ${self.agreed_price:.2f} | Status: {self.status}")


class SewLink:
    """Core System Class handling memory storage, business logic, and workflows."""
    def __init__(self):
        self.customers = {}
        self.tailors = {}
        self.jobs = {}
        self.messages = {}
        self.orders = {}

    # ------------------------------------------------------------
    # CUSTOMER MANAGEMENT
    # ------------------------------------------------------------
    def add_customer(self):
        print("\n--- Add New Customer ---")
        customer_id = input("Enter Customer ID: ").strip()
        if customer_id in self.customers:
            print("Error: Customer ID already exists!")
            return
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone: ").strip()
        email = input("Enter Email: ").strip()
        location = input("Enter Location: ").strip()

        self.customers[customer_id] = Customer(customer_id, name, phone, email, location)
        print("Customer added successfully!")

    def view_customers(self):
        print("\n--- Registered Customers ---")
        if not self.customers:
            print("No customers registered.")
            return
        for customer in self.customers.values():
            customer.display()

    def search_customer(self):
        cid = input("Enter Customer ID to search: ").strip()
        customer = self.customers.get(cid)
        if customer:
            customer.display()
        else:
            print("Customer not found.")

    def update_customer(self):
        cid = input("Enter Customer ID to update: ").strip()
        customer = self.customers.get(cid)
        if not customer:
            print("Customer not found.")
            return
        print("Leave blank to keep existing value.")
        name = input(f"New Name [{customer.name}]: ").strip()
        phone = input(f"New Phone [{customer.phone}]: ").strip()
        email = input(f"New Email [{customer.email}]: ").strip()
        location = input(f"New Location [{customer.location}]: ").strip()

        if name: customer.name = name
        if phone: customer.phone = phone
        if email: customer.email = email
        if location: customer.location = location
        print("Customer updated successfully!")

    def delete_customer(self):
        cid = input("Enter Customer ID to delete: ").strip()
        if cid in self.customers:
            del self.customers[cid]
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")

    # ------------------------------------------------------------
    # TAILOR MANAGEMENT
    # ------------------------------------------------------------
    def add_tailor(self):
        print("\n--- Add New Tailor ---")
        tailor_id = input("Enter Tailor ID: ").strip()
        if tailor_id in self.tailors:
            print("Error: Tailor ID already exists!")
            return
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone: ").strip()
        email = input("Enter Email: ").strip()
        location = input("Enter Location: ").strip()
        specialization = input("Enter Specialization (e.g., Suits, Dresses, Alterations): ").strip()

        self.tailors[tailor_id] = Tailor(tailor_id, name, phone, email, location, specialization)
        print("Tailor added successfully!")

    def view_tailors(self):
        print("\n--- Registered Tailors ---")
        if not self.tailors:
            print("No tailors registered.")
            return
        for tailor in self.tailors.values():
            tailor.display()

    def search_tailor(self):
        tid = input("Enter Tailor ID to search: ").strip()
        tailor = self.tailors.get(tid)
        if tailor:
            tailor.display()
        else:
            print("Tailor not found.")

    def update_tailor(self):
        tid = input("Enter Tailor ID to update: ").strip()
        tailor = self.tailors.get(tid)
        if not tailor:
            print("Tailor not found.")
            return
        print("Leave blank to keep existing value.")
        name = input(f"New Name [{tailor.name}]: ").strip()
        phone = input(f"New Phone [{tailor.phone}]: ").strip()
        email = input(f"New Email [{tailor.email}]: ").strip()
        location = input(f"New Location [{tailor.location}]: ").strip()
        spec = input(f"New Specialization [{tailor.specialization}]: ").strip()

        if name: tailor.name = name
        if phone: tailor.phone = phone
        if email: tailor.email = email
        if location: tailor.location = location
        if spec: tailor.specialization = spec
        print("Tailor updated successfully!")

    def delete_tailor(self):
        tid = input("Enter Tailor ID to delete: ").strip()
        if tid in self.tailors:
            del self.tailors[tid]
            print("Tailor deleted successfully.")
        else:
            print("Tailor not found.")

    # ------------------------------------------------------------
    # JOB MANAGEMENT & WORKFLOW
    # ------------------------------------------------------------
    def create_job(self):
        print("\n--- Create New Job ---")
        job_id = input("Enter Job ID: ").strip()
        if job_id in self.jobs:
            print("Error: Job ID already exists!")
            return
        cid = input("Enter Customer ID: ").strip()
        if cid not in self.customers:
            print("Error: Customer ID does not exist. Please register customer first.")
            return
        title = input("Enter Job Title: ").strip()
        description = input("Enter Description: ").strip()
        category = input("Enter Category (Suits/Dresses/Repair/etc.): ").strip()
        try:
            budget = float(input("Enter Budget ($): "))
        except ValueError:
            print("Invalid budget amount.")
            return

        self.jobs[job_id] = Job(job_id, cid, title, description, category, budget)
        print("Job posted successfully! Status: Open")

    def view_jobs(self):
        print("\n--- All Posted Jobs ---")
        if not self.jobs:
            print("No jobs found.")
            return
        for job in self.jobs.values():
            job.display()

    def search_job(self):
        jid = input("Enter Job ID to search: ").strip()
        job = self.jobs.get(jid)
        if job:
            job.display()
        else:
            print("Job not found.")

    def update_job(self):
        jid = input("Enter Job ID to update: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Job not found.")
            return
        if job.status != "Open":
            print(f"Cannot edit job details once job status is '{job.status}'.")
            return

        print("Leave blank to keep existing value.")
        title = input(f"New Title [{job.title}]: ").strip()
        desc = input(f"New Description [{job.description}]: ").strip()
        cat = input(f"New Category [{job.category}]: ").strip()
        budget_str = input(f"New Budget [{job.budget}]: ").strip()

        if title: job.title = title
        if desc: job.description = desc
        if cat: job.category = cat
        if budget_str:
            try:
                job.budget = float(budget_str)
            except ValueError:
                print("Invalid budget input. Kept old value.")
        print("Job updated successfully!")

    def delete_job(self):
        jid = input("Enter Job ID to delete: ").strip()
        if jid in self.jobs:
            del self.jobs[jid]
            print("Job deleted successfully.")
        else:
            print("Job not found.")

    def accept_job(self):
        jid = input("Enter Job ID to accept: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Job not found.")
            return
        if job.status != "Open":
            print(f"Error: Job cannot be accepted because status is '{job.status}'.")
            return

        tid = input("Enter Tailor ID accepting this job: ").strip()
        if tid not in self.tailors:
            print("Error: Tailor ID does not exist.")
            return

        job.tailor_id = tid
        job.status = "Accepted"
        print(f"Job [{job.job_id}] accepted by Tailor [{tid}]. Status updated to Accepted.")

    def reject_job(self):
        jid = input("Enter Job ID to reject: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Job not found.")
            return
        if job.status != "Open":
            print(f"Error: Cannot reject job with status '{job.status}'.")
            return
        job.status = "Rejected"
        print(f"Job [{job.job_id}] status updated to Rejected.")

    def start_job(self):
        jid = input("Enter Job ID to start: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Job not found.")
            return
        if job.status != "Accepted":
            print(f"Error: Job must be in 'Accepted' status to start. Current status: '{job.status}'.")
            return
        job.status = "In Progress"
        print(f"Job [{job.job_id}] is now In Progress.")

    def complete_job(self):
        jid = input("Enter Job ID to complete: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Job not found.")
            return
        if job.status != "In Progress":
            print(f"Error: Job must be 'In Progress' to complete. Current status: '{job.status}'.")
            return
        job.status = "Completed"
        print(f"Job [{job.job_id}] marked as Completed!")

    def cancel_job(self):
        jid = input("Enter Job ID to cancel: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Job not found.")
            return
        if job.status == "Completed":
            print("Error: Cannot cancel an already completed job.")
            return
        job.status = "Cancelled"
        print(f"Job [{job.job_id}] marked as Cancelled.")

    def available_jobs(self):
        print("\n--- Available Open Jobs ---")
        open_jobs = [j for j in self.jobs.values() if j.status == "Open"]
        if not open_jobs:
            print("No open jobs available.")
            return
        for job in open_jobs:
            job.display()

    def customer_jobs(self):
        cid = input("Enter Customer ID: ").strip()
        print(f"\n--- Jobs for Customer [{cid}] ---")
        user_jobs = [j for j in self.jobs.values() if j.customer_id == cid]
        if not user_jobs:
            print("No jobs found for this customer.")
            return
        for job in user_jobs:
            job.display()

    def tailor_jobs(self):
        tid = input("Enter Tailor ID: ").strip()
        print(f"\n--- Jobs assigned to Tailor [{tid}] ---")
        assigned_jobs = [j for j in self.jobs.values() if j.tailor_id == tid]
        if not assigned_jobs:
            print("No jobs assigned to this tailor.")
            return
        for job in assigned_jobs:
            job.display()

    # ------------------------------------------------------------
    # MESSAGING FUNCTIONS
    # ------------------------------------------------------------
    def send_message(self):
        print("\n--- Send Direct Message ---")
        mid = input("Enter Message ID: ").strip()
        if mid in self.messages:
            print("Error: Message ID already exists!")
            return
        sender = input("Sender ID (Customer or Tailor ID): ").strip()
        receiver = input("Receiver ID (Customer or Tailor ID): ").strip()
        content = input("Message Content: ").strip()

        self.messages[mid] = Message(mid, sender, receiver, content)
        print("Message sent successfully!")

    def view_messages(self):
        print("\n--- Message Box ---")
        uid = input("Enter your User ID to view messages: ").strip()
        user_msgs = [m for m in self.messages.values() if m.sender == uid or m.receiver == uid]
        if not user_msgs:
            print("No messages found.")
            return
        for msg in user_msgs:
            msg.display()

    # ------------------------------------------------------------
    # ORDER MANAGEMENT & WORKFLOW
    # ------------------------------------------------------------
    def create_order(self):
        print("\n--- Convert Accepted Job to Order ---")
        oid = input("Enter New Order ID: ").strip()
        if oid in self.orders:
            print("Error: Order ID already exists!")
            return
        jid = input("Enter Job ID: ").strip()
        job = self.jobs.get(jid)
        if not job:
            print("Error: Job not found.")
            return
        if job.status not in ["Accepted", "In Progress", "Completed"]:
            print(f"Error: Orders can only be created for jobs that are Accepted or further. Current status: '{job.status}'.")
            return

        try:
            agreed_price = float(input(f"Enter Agreed Price (Job Budget: ${job.budget:.2f}): "))
        except ValueError:
            print("Invalid price.")
            return

        self.orders[oid] = Order(oid, jid, job.customer_id, job.tailor_id, agreed_price)
        print(f"Order [{oid}] created successfully!")

    def view_orders(self):
        print("\n--- All Orders ---")
        if not self.orders:
            print("No orders recorded.")
            return
        for order in self.orders.values():
            order.display()

    def search_order(self):
        oid = input("Enter Order ID to search: ").strip()
        order = self.orders.get(oid)
        if order:
            order.display()
        else:
            print("Order not found.")

    def update_order_status(self):
        oid = input("Enter Order ID to update: ").strip()
        order = self.orders.get(oid)
        if not order:
            print("Order not found.")
            return

        print("Select New Status:")
        print("1. In Progress\n2. Ready\n3. Completed\n4. Cancelled")
        choice = input("Enter choice (1-4): ").strip()
        status_map = {"1": "In Progress", "2": "Ready", "3": "Completed", "4": "Cancelled"}

        if choice in status_map:
            order.status = status_map[choice]
            print(f"Order [{oid}] status updated to '{order.status}'.")
        else:
            print("Invalid status choice.")

    def completed_orders(self):
        print("\n--- Completed Orders ---")
        done_orders = [o for o in self.orders.values() if o.status == "Completed"]
        if not done_orders:
            print("No completed orders found.")
            return
        for order in done_orders:
            order.display()

    # ------------------------------------------------------------
    # DASHBOARD
    # ------------------------------------------------------------
    def dashboard(self):
        print("\n============================================================")
        print("                SEWLINK MARKETPLACE DASHBOARD               ")
        print("============================================================")
        total_customers = len(self.customers)
        total_tailors = len(self.tailors)
        total_jobs = len(self.jobs)
        open_jobs = sum(1 for j in self.jobs.values() if j.status == "Open")
        accepted_jobs = sum(1 for j in self.jobs.values() if j.status == "Accepted")
        in_progress_jobs = sum(1 for j in self.jobs.values() if j.status == "In Progress")
        completed_jobs = sum(1 for j in self.jobs.values() if j.status == "Completed")
        
        total_orders = len(self.orders)
        completed_orders = sum(1 for o in self.orders.values() if o.status == "Completed")

        print(f" Total Customers    : {total_customers}")
        print(f" Total Tailors      : {total_tailors}")
        print(" ----------------------------------------------------------")
        print(f" Total Jobs         : {total_jobs}")
        print(f"   - Open Jobs      : {open_jobs}")
        print(f"   - Accepted Jobs  : {accepted_jobs}")
        print(f"   - In Progress    : {in_progress_jobs}")
        print(f"   - Completed Jobs : {completed_jobs}")
        print(" ----------------------------------------------------------")
        print(f" Total Orders       : {total_orders}")
        print(f" Completed Orders   : {completed_orders}")
        print("============================================================")


# ============================================================
# SUB-MENUS & MAIN CONTROLLER
# ============================================================

def customer_menu(sewlink):
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Create Job")
        print("7. View My Jobs")
        print("8. View Tailors")
        print("9. Send Message")
        print("10. View Messages")
        print("11. View Orders")
        print("12. Exit to Main Menu")

        choice = input("Select an option (1-12): ").strip()

        if choice == "1": sewlink.add_customer()
        elif choice == "2": sewlink.view_customers()
        elif choice == "3": sewlink.search_customer()
        elif choice == "4": sewlink.update_customer()
        elif choice == "5": sewlink.delete_customer()
        elif choice == "6": sewlink.create_job()
        elif choice == "7": sewlink.customer_jobs()
        elif choice == "8": sewlink.view_tailors()
        elif choice == "9": sewlink.send_message()
        elif choice == "10": sewlink.view_messages()
        elif choice == "11": sewlink.view_orders()
        elif choice == "12": break
        else: print("Invalid choice! Try again.")


def tailor_menu(sewlink):
    while True:
        print("\n--- TAILOR MENU ---")
        print("1. Add Tailor")
        print("2. View Tailors")
        print("3. Search Tailor")
        print("4. Update Tailor")
        print("5. Delete Tailor")
        print("6. View Available Jobs")
        print("7. View My Jobs")
        print("8. Accept Job")
        print("9. Reject Job")
        print("10. Start Job")
        print("11. Complete Job")
        print("12. Send Message")
        print("13. View Messages")
        print("14. View Orders")
        print("15. Exit to Main Menu")

        choice = input("Select an option (1-15): ").strip()

        if choice == "1": sewlink.add_tailor()
        elif choice == "2": sewlink.view_tailors()
        elif choice == "3": sewlink.search_tailor()
        elif choice == "4": sewlink.update_tailor()
        elif choice == "5": sewlink.delete_tailor()
        elif choice == "6": sewlink.available_jobs()
        elif choice == "7": sewlink.tailor_jobs()
        elif choice == "8": sewlink.accept_job()
        elif choice == "9": sewlink.reject_job()
        elif choice == "10": sewlink.start_job()
        elif choice == "11": sewlink.complete_job()
        elif choice == "12": sewlink.send_message()
        elif choice == "13": sewlink.view_messages()
        elif choice == "14": sewlink.view_orders()
        elif choice == "15": break
        else: print("Invalid choice! Try again.")


def display_menu():
    print("\n============================================================")
    print("                 SEWLINK MANAGEMENT SYSTEM                 ")
    print("============================================================")
    print("1. Customer Management")
    print("2. Tailor Management")
    print("3. Job Management")
    print("4. Messaging")
    print("5. Order Management")
    print("6. Dashboard")
    print("7. Exit")
    print("============================================================")


def main():
    sewlink = SewLink()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            customer_menu(sewlink)
        elif choice == "2":
            tailor_menu(sewlink)
        elif choice == "3":
            print("\n--- JOB MANAGEMENT SUBMENU ---")
            print("1. Create Job\n2. View Jobs\n3. Search Job\n4. Update Job\n5. Delete Job")
            print("6. Accept Job\n7. Reject Job\n8. Start Job\n9. Complete Job\n10. Cancel Job")
            j_choice = input("Select choice (1-10): ").strip()
            if j_choice == "1": sewlink.create_job()
            elif j_choice == "2": sewlink.view_jobs()
            elif j_choice == "3": sewlink.search_job()
            elif j_choice == "4": sewlink.update_job()
            elif j_choice == "5": sewlink.delete_job()
            elif j_choice == "6": sewlink.accept_job()
            elif j_choice == "7": sewlink.reject_job()
            elif j_choice == "8": sewlink.start_job()
            elif j_choice == "9": sewlink.complete_job()
            elif j_choice == "10": sewlink.cancel_job()
            else: print("Invalid job operation.")
        elif choice == "4":
            print("\n--- MESSAGING SUBMENU ---")
            print("1. Send Message\n2. View Messages")
            m_choice = input("Select choice (1-2): ").strip()
            if m_choice == "1": sewlink.send_message()
            elif m_choice == "2": sewlink.view_messages()
            else: print("Invalid choice.")
        elif choice == "5":
            print("\n--- ORDER MANAGEMENT SUBMENU ---")
            print("1. Create Order\n2. View Orders\n3. Search Order\n4. Update Order Status\n5. View Completed Orders")
            o_choice = input("Select choice (1-5): ").strip()
            if o_choice == "1": sewlink.create_order()
            elif o_choice == "2": sewlink.view_orders()
            elif o_choice == "3": sewlink.search_order()
            elif o_choice == "4": sewlink.update_order_status()
            elif o_choice == "5": sewlink.completed_orders()
            else: print("Invalid choice.")
        elif choice == "6":
            sewlink.dashboard()
        elif choice == "7":
            print("Exiting SewLink Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-7).")


if __name__ == "__main__":
    main()