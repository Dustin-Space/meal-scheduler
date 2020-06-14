There are recipes.

For cooking a recipe, you need to have the right ingredients in the right amounts.

For example: to cook the "vegan chocolate ice cream" recipe for 2 people, you need 3 bananas and 4 tbsp of cocoa powder.

This program will, at any time, know:

* How much of which ingredients we have available right now
* How many people will want to cook in the next, say, week.

When we run it, it will generate a schedule of:

* What meals to cook in the future.
* What ingredients we need to order, and when will they be needed.

Constraints on the schedule:

* We need to be able to cook the scheduled recipes.
* Ingredients will be used before they expire.
  * Fresh ingredients: need to be used in a day or two after buying (e.g., fresh cilantro).
  * Durable ingredients: can stay OK for years (e.g., rice)
  * Canned ingredients: once opened, need to be consumed within, say, 2 weeks (e.g., canned coconut milk)
* Allow us to play with the schedule and automatically adjust - e.g., "hey I really want to cook eggs tomorrow" would make it recompute a plan, such that any orders that we currently have outstanding will be used.
* Compute and allow for optimizing the price.
* Satisficing for how much of what nutrients you should be getting.
* Prefer variety.

More features that would be nice:

* Some ingredients can be substituted - e.g., different types of rice, cow milk and rice milk, dried cranberries and raisins, etc.
