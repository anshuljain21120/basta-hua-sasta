import random

from django.contrib.auth.models import User

from orgproject.marketplace.models import Product


def cleanup():
    Product.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()

def create_users(usernames):
    return [
        User.objects.create_user(
            username=firstname.lower() + lastname.lower() + str(random.randint(1, 100)),
            first_name=firstname,
            last_name=lastname,
            email=firstname.lower() + lastname.lower() + '@gmail.com',
            password='pass@123'
        ) for firstname, lastname in usernames
    ]

def create_products(users_qs, title_iterator, n):
    return Product.objects.bulk_create([Product(title=next(title_iterator), price=random.random() * 1000,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sed turpis ac turpis placerat "
                    "condimentum. Quisque luctus est quis facilisis sodales. Vestibulum elementum massa ac nulla id.",
        owner=random.choice(users_qs), available_count=random.randint(1, 10),
        image_url=f"https://picsum.photos/id/{random.randint(1, 30)}/900/500") for i in range(n)])

def run():
    cleanup()
    users = create_users(usernames=[('Rohan', 'Sharma'), ('Anjali', 'Mathur'), ('Komal', 'Shah'), ('Pankaj', 'Kumar'),
        ('Robin', 'Singh'), ('Priya', 'Raj'), ('Avi', 'Kasliwal')])
    print(users)
    titles = iter(["Don Quixote", "Alice's Adventures in Wonderland", "The Adventures of Huckleberry Finn",
                   "The Adventures of Tom Sawyer", "Treasure Island", "Pride and Prejudice", "Wuthering Heights",
                   "Jane Eyre", "Moby Dick", "The Scarlet Letter", "Gulliver's Travels", "The Pilgrim's Progress",
                   "A Christmas Carol", "David Copperfield", "A Tale of Two Cities", "Little Women",
                   "Great Expectations", "The Hobbit, or, There and Back Again",
                   "Frankenstein, or, the Modern Prometheus", "Oliver Twist", "Uncle Tom's Cabin",
                   "Crime and Punishment", "Madame Bovary: Patterns of Provincial life", "The Return of the King",
                   "Dracula", "The Three Musketeers", "Brave New World", "War and Peace", "To Kill a Mockingbird",
                   "The Wizard of Oz", "Les Misérables", "The Secret Garden", "Animal Farm", "The Great Gatsby",
                   "The Little Prince", "The Call of the Wild", "20,000 Leagues Under the Sea", "Anna Karenina",
                   "The Wind in the Willows", "The Picture of Dorian Gray", "The Grapes of Wrath",
                   "Sense and Sensibility", "The Last of the Mohicans", "Tess of the d'Urbervilles",
                   "Harry Potter and the Sorcerer's Stone", "Heidi", "Ulysses", "The Complete Sherlock Holmes",
                   "The Count of Monte Cristo", "The Old Man and the Sea", "The Lion, the Witch, and the Wardrobe",
                   "The Hunchback of Notre Dame", "Pinocchio", "One Hundred Years of Solitude", "Ivanhoe",
                   "The Red Badge of Courage", "Anne of Green Gables", "Black Beauty", "Peter Pan",
                   "A Farewell to Arms", "The House of the Seven Gables", "Lord of the Flies",
                   "The Prince and the Pauper", "A Portrait of the Artist as a Young Man", "Lord Jim",
                   "Harry Potter and the Chamber of Secrets", "The Red & the Black", "The Stranger", "The Trial",
                   "Lady Chatterley's Lover", "Kidnapped: The Adventures of David Balfour", "The Catcher in the Rye",
                   "Fahrenheit 451", "A Journey to the Center of the Earth", "Vanity Fair",
                   "All Quiet on the Western Front", "Gone with the Wind", "My Ántonia", "Of Mice and Men",
                   "The Vicar of Wakefield", "A Connecticut Yankee in King Arthur's Court", "White Fang",
                   "Fathers and Sons", "Doctor Zhivago", "The Decameron", "Nineteen Eighty-Four", "The Jungle",
                   "The Da Vinci Code", "Persuasion", "Mansfield Park", "Candide", "For Whom the Bell Tolls",
                   "Far from the Madding Crowd", "The Fellowship of the Ring", "The Return of the Native",
                   "Sons and Lovers", "Charlotte's Web", "The Swiss Family Robinson", "Bleak House", "Père Goriot",
                   "Utopia", "The History of Tom Jones, a Foundling", "Harry Potter and the Prisoner of Azkaban", "Kim",
                   "The Sound and the Fury", "Harry Potter and the Goblet of Fire", "The Mill on the Floss",
                   "A Wrinkle in Time", "The Hound of the Baskervilles", "The Two Towers", "The War of the Worlds",
                   "Middlemarch", "The Age of Innocence", "The Color Purple", "Northanger Abbey", "East of Eden",
                   "On the Road", "Catch-22", "Around the World in Eighty Days", "Hard Times", "Beloved",
                   "Mrs. Dalloway", "To the Lighthouse", "The Magician's Nephew",
                   "Harry Potter and the Order of the Phoenix", "The Sun Also Rises", "The Good Earth", "Silas Marner",
                   "Love in the Time of Cholera", "Rebecca", "Jude the Obscure", "Twilight", "A Passage to India",
                   "The Plague", "Nicholas Nickleby", "The Pearl", "Ethan Frome", "The Tale of Genji", "The Giver",
                   "The Alchemist", "The Strange Case of Dr. Jekyll and Mr. Hyde", "Robinson Crusoe",
                   "Tender is the Night", "The Idiot", "Hatchet", "The Kite Runner", "One Flew Over the Cuckoo's Nest",
                   "The Portrait of a Lady", "The Outsiders", "Ben-Hur", "The Mayor of Casterbridge",
                   "Cry, The Beloved Country", "The Last Battle", "Captains Courageous", "The Castle",
                   "The Metamorphosis", "The Magic Mountain (Der Zauberberg)", "James and the Giant Peach",
                   "The Horse and His Boy", "Angels & Demons", "The Voyage of the Dawn Treader", "The Bell Jar",
                   "Women in Love", "The Yearling", "O Pioneers!", "The Handmaid's Tale", "The Moonstone",
                   "The Old Curiosity Shop", "Little Dorrit", "Prince Caspian: The Return to Narnia", "Sister Carrie",
                   "The Silver Chair", "The Hunger Games", "This Side of Paradise", "Eugénie Grandet",
                   "Of Human Bondage", "Dream of the Red Chamber", "Life of Pi", "Harry Potter and the Deathly Hallows",
                   "Invisible Man", "Steppenwolf", "The Sorrows of Young Werther"])
    products = create_products(users, titles, n=30)
    print(products)
