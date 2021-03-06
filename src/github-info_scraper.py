from tkinter import Tk, messagebox, Label, Entry, Button, END
import requests
import json 
from PIL import ImageTk, Image

class github_mate:
	def __init__(self, master):
		master.title("GitHub-Info-Scraper")
		master.geometry("500x620")
		master.resizable(False, False)

		self.image = ImageTk.PhotoImage(Image.open("../assets/github.png"))
		self.img = Label(image=self.image).grid(row = 0, column = 0, columnspan = 3)
		self.blank_label_one = Label(text = "").grid(row = 1, column = 0)
		self.username_label = Label(text = "Username:", font = "courier 20 bold").grid(row = 2, column = 0)
		self.username_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove")
		self.username_field.grid(row = 2, column = 1)
		self.username_field.focus_set()
		self.blank_label_two = Label(text = "").grid(row = 3, column = 0)
		self.name_label = Label(text="Name", font = "courier 20 bold").grid(row = 4, column = 0) 
		self.name_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove")
		self.name_field.bind("<Key>", lambda e: "break")
		self.name_field.grid(row = 4, column = 1)
		self.blank_label_three = Label(text = "").grid(row = 5, column = 0)
		self.repositories_label = Label(text = "Repositories:", font = "courier 20 bold").grid(row = 6, column = 0)
		self.repositories_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove")
		self.repositories_field.bind("<Key>", lambda e: "break")
		self.repositories_field.grid(row = 6, column = 1)
		self.blank_label_four = Label(text = "").grid(row = 7, column = 0)
		self.followers_label = Label(text = "Followers:", font = "courier 20 bold").grid(row = 8, column = 0)
		self.followers_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove")
		self.followers_field.bind("<Key>", lambda e: "break")
		self.followers_field.grid(row = 8, column = 1)
		self.blank_label_five = Label(text = "").grid(row = 9, column = 0)
		self.following_label = Label(text = "Following:", font = "courier 20 bold").grid(row = 10, column = 0)
		self.following_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove")
		self.following_field.bind("<Key>", lambda e: "break")
		self.following_field.grid(row = 10, column = 1)
		self.blank_label_six = Label(text = "").grid(row = 11, column = 0)
		self.gists_label = Label(text = "Gists:", font = "courier 20 bold").grid(row = 12, column = 0)
		self.gists_field = Entry(font = "cursive 16 bold", bd = 6, relief = "groove")
		self.gists_field.bind("<Key>", lambda e: "break")
		self.gists_field.grid(row = 12, column = 1)
		self.blank_label_seven = Label(text = "").grid(row = 13, column = 0)
		self.blank_label_eight = Label(text = "").grid(row = 14, column = 0)
		self.get_btn = Button(text = "Get", font="times 22 bold", fg = "blue", bd = 2, relief = "raised", command = self.btn_clicked).grid(row = 15, column = 0)
		self.clear_btn = Button(text = "Clear", font="times 22 bold", fg = "red", bd = 2, relief = "raised", command = self.clear_clicked).grid(row = 15, column = 1)
		
	def clear_clicked(self):

			self.username_field.delete(0, END)        
			self.name_field.delete(0, END)
			self.repositories_field.delete(0, END)
			self.followers_field.delete(0, END)
			self.following_field.delete(0, END)
			self.gists_field.delete(0, END)                

	def btn_clicked(self):
                
			self.name_field.delete(0, END)
			self.repositories_field.delete(0, END)
			self.followers_field.delete(0, END)
			self.following_field.delete(0, END)
			self.gists_field.delete(0, END)

			self.username = self.username_field.get()
			if self.username == "":
			   messagebox.showwarning("warning", "Kindly enter a username!")
			   return  			
			try:
			    self.request = requests.get('https://api.github.com/users/' + self.username)
			except:
			    messagebox.showwarning("warning", "Check your network connection!")
			    self.username_field.delete(0, END)
			    return
			
			if not self.request.ok:
			   messagebox.showwarning("Warning", "User doesn't exist!")	
			   return
			
			self.github_data = json.loads(self.request.content)
			if self.github_data['name'] != None:
				self.name_field.insert(0, self.github_data['name'])
			else:
				self.name_field.insert(0, "None")			
			self.repositories_field.insert(0, self.github_data['public_repos']) 
			self.followers_field.insert(0, self.github_data['followers'])
			self.following_field.insert(0, self.github_data['following'])
			self.gists_field.insert(0, self.github_data['public_gists'])

if __name__ == '__main__':
	root = Tk()
	app = github_mate(root)	  	
