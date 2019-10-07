# SmartPay

## Inspiration

Bank Card holders face a real problem: there are too many rewards and offers to keep up with. Reward Cards boast incentives and bonuses: some cards cycle money back to the users, others earn Flight Miles, still others offer flat discounts-- juggling which one to use when to get the most out of the savings can be a headache even for the most experienced bargain hunter. Our goal is simple: automate the process as much as possible to eliminate the headache of selecting the Reward Card with the best offer for a particular purchase. 

## What it does

SmartPay fetches the metadata of all the user cards, including the rewards and offers associated with that Bank Card, and then compares them to each other in a algorithm that decides the best Bank Card with the highest reward value for a particular purchase where purchase is defined by 'utility'. 

For example-- a user is buying groceries at Fry's. Fry's is defined as a 'grocery' utility. The user has three bank cards in their wallet. One card gives the user 2% cash back, the other gives 5% back but only to Target, and the third would net the user 200 airplane points. Smart-pay sorts through the available cards and associated offers, and because of the criteria, decides that the best value back is the airplane points. It then shows the user that card and prompts them to pay with it. 

## How we built it

We built it with Python modules sqlite, and tkinter along with an openCV library in order to achieve Optical Character Recognition(OCR) to fetch out all the details for a particular card.

## Challenges we ran into

We ran into a stumbling block due to the general lack of knowledge the teammates had about the American Banking System. While we could fetch out the details of a bank card using OCR, we ran into trouble accurately differentiating different kinds of reward cards from each other because of the high diversity of bank card design and bank card types. Because of this, some of the features initially planned for the prototype were not completed before we ran out of time, although we got partial functionality ready during the testing phases. We were testing out a lot of new concepts and programming languages during the project, which was a highly educational experience but slowed down the speed at which we were working. 

## Accomplishments that we're proud of

We are extremely proud of the idea of SmartPay, and that we were ultimately capable of collaborating successfully and creating a functional prototype. 

## What we learned

We learned a lot more about the American Banking System then we had previously been aware of. On a technical level, we learned Python modules and OCR. 

## What's next for SmartPay

Our vision is to fetch the best offers as per the GPS coordinates with a mapping of a particular vendor to a particular utility such as gas stations and grocery stores along with an augment reality based portal on educating people with different types of banking services.
