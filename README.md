# 🍳 ChefGPT: AI Powered Recipe Generator Based on Your Pantry

ChefGPT is an **AI-powered recipe recommendation system** that helps users transform ingredients already available in their pantry into delicious, personalized meals.

Instead of ordering food from outside despite having groceries at home, ChefGPT intelligently suggests recipes based on available ingredients, cuisine preferences, dietary restrictions, serving sizes, and kitchen appliances.

🔗 **Live Demo:** https://chefgpt-m2dufmvegy9p7vb6zbrenf.streamlit.app/

---

## 📖 About the Project

The idea for ChefGPT originated from a real-life problem.

While living with my sister for a month, we often had groceries available at home but struggled to decide what to cook. After spending considerable time discussing meal ideas, we frequently ended up ordering food from outside, which was neither cost-effective nor healthy.

ChefGPT was developed to solve this problem by acting as an intelligent cooking assistant that recommends personalized recipes using ingredients users already have at home.

---

## ✨ Features

### 🤖 AI-Powered Conversational Assistant
- Interactive chatbot interface built using Streamlit
- Collects user preferences through natural conversation

### 🥕 Pantry-Based Recipe Generation
- Generates recipes based on ingredients already available
- Reduces food waste by maximizing ingredient utilization

### 🍽 Personalized Meal Recommendations
Considers:
- Meal Type (Breakfast, Lunch, Dinner, Dessert)
- Cuisine Preferences (Indian, Chinese, Japanese, Italian, etc.)
- Dietary Preferences (Vegetarian, Vegan, Jain, High Protein, etc.)
- Serving Size
- Difficulty Level

### 🔌 Appliance-Aware Suggestions
Recommends recipes based on available kitchen appliances:
- Stove
- Oven
- Microwave
- Air Fryer
- Rice Cooker
- Blender

### 💰 Budget-Friendly Missing Ingredients
- Allows recipes with missing ingredients
- Prioritizes inexpensive and commonly available ingredients

### 📋 Detailed Recipe Generation
Provides:
- Complete ingredient list
- Missing ingredients
- Required appliances
- Step-by-step cooking instructions
- Nutritional information
- Chef tips

### 🗂 Recipe History
- Stores generated recipes in Supabase
- Enables users to revisit previously generated recipes

### 📄 PDF Export
- Download recipes as PDF documents for offline access

### ☁ Cloud Deployment
- Fully deployed using Streamlit Community Cloud

---

## 🛠 Tech Stack

| Category               | Technologies Used         |
| ---------------------- | -------------------------- |
| Frontend               | Streamlit                 |
| AI Model               | Google Gemini API          |
| Backend Logic          | Python                     |
| Database               | Supabase                   |
| PDF Generation         | ReportLab                  |
| Environment Management | Python Dotenv              |
| Deployment             | Streamlit Community Cloud  |

---

## 🏗 System Architecture

```text
User
  ↓
Streamlit Chat Interface
  ↓
Collect User Preferences
  ↓
Google Gemini API
  ↓
Recipe Suggestions (3 Options)
  ↓
User Selects Recipe
  ↓
Detailed Recipe Generation
  ↓
Save Recipe → Supabase
  ↓
PDF Export & Recipe History
```

---

## 🚀 Live Application

Access ChefGPT here:

### 👉 [https://chefgpt-m2dufmvegy9p7vb6zbrenf.streamlit.app/](https://chefgpt-m2dufmvegy9p7vb6zbrenf.streamlit.app/)

---

## 📸 Application Workflow

1. Enter your username
2. Provide available pantry ingredients
3. Select meal type
4. Choose preferred cuisine
5. Specify number of servings
6. Indicate dietary preferences
7. Choose preferred difficulty level
8. Specify available appliances
9. Review AI-generated recipe suggestions
10. Select a recipe
11. Receive a detailed cooking guide
12. Download the recipe as a PDF or access it later from recipe history

---

## ⚙️ Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/architabajpai/ChefGPT.git
cd ChefGPT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
ChefGPT/
│
├── app.py
├── requirements.txt
├── .env
│
├── pages/
│   ├── history.py
│   └── about.py
│
├── utils/
│   ├── gemini_helper.py
│   ├── supabase_helper.py
│   └── pdf_generator.py
│
└── README.md
```

---

## 🎯 Future Enhancements

- Ingredient image recognition using Computer Vision
- Voice-enabled cooking assistant
- Weekly meal planning
- Grocery list generation
- Recipe rating and recommendation system
- Authentication and personalized dashboards
- Multi-language support

---

## 🌍 Impact

ChefGPT aims to:

- Reduce food waste by utilizing existing ingredients
- Promote healthier eating habits
- Decrease dependency on food delivery services
- Help users save money on unnecessary food expenses
- Simplify meal decision-making through AI assistance

---

## 🧠 Key Learnings

This project provided hands-on experience with:

- Prompt Engineering
- Generative AI Integration
- Full-Stack Application Development
- Cloud Database Management
- Streamlit Application Deployment
- User-Centric Product Design

---

## 👩‍💻 Author

**Archita Bajpai**

Computer Science Engineering Student | AI & Software Development Enthusiast

If you found this project interesting, consider giving it a ⭐ on GitHub!
