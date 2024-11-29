from robocorp.tasks import task
from robocorp import browser,http

from RPA.Tables import Tables
from RPA.PDF import PDF
from RPA.Archive import Archive

@task
def order_robots_from_RobotSpareBin():
        
        """   
        Orders robots from RobotSpareBin Industries Inc.
        Saves the order HTML receipt as a PDF file.
        Saves the screenshot of the ordered robot.
        Embeds the screenshot of the robot to the PDF receipt.
        Creates ZIP archive of the receipts and the images.
        """
        open_robot_order_website()
        orders = get_orders()
        for row in orders:
                fill_the_form(row)
        archieve_receipts()

def open_robot_order_website():
        # TODO: Implement your function here

def archieve_receipts():
        

