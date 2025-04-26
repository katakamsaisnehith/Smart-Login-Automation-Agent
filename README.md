# Smart-Login-Automation-Agent
This project showcases an AI Agent that automates the process of logging into a website using natural language prompts and browser control via the browser_use package, integrated with the Gemini Pro LLM.

 Project Summary
The agent is designed to:

Open the browser and navigate to https://www.farmley.com

Click on the "My Account" icon

Choose the "Login" option

Enter pre-defined login credentials

Attempt to complete the login

Validate if the user is successfully logged in

 Prompt Design Approach
The prompt for the agent was written in natural and stepwise instructions, allowing the LLM to understand the exact task flow. This structure improves clarity and enables the model to reason through the sequence of actions needed.

Sample prompt:

pgsql
Copy
Edit
1. Open the browser and go to https://www.farmley.com
2. Click on the 'My Account' icon at the top-right corner
3. Click on 'Login'
4. Enter the email as testuser@example.com
5. Enter the password as Test@1234
6. Click on 'Login' button
7. After login, validate that 'My Account' is visible
 Execution & Validation Logic
Execution: The agent uses a headless browser to perform each instruction using Gemini Pro’s understanding of the prompt.

Validation: After login, the agent checks the presence of visual cues (like "My Account") to confirm successful login.

 CAPTCHA Challenge
After submitting the login form, a CAPTCHA prompt is triggered, which the agent cannot bypass.

 Our Approach
The agent stops automatically at this step and prompts the user to manually solve the CAPTCHA.

This ensures compliance with ethical guidelines and website terms of service.

Once the CAPTCHA is solved, the validation continues.

 Note: Automating CAPTCHA would violate platform terms and legal boundaries. The decision to not automate this part is intentional and responsible.

 Challenges & Resolutions

Challenge	Resolution
CAPTCHA appearing post-login	Manual intervention added via input() prompt
LLM navigating unintended sites	Rewrote prompts with more context to stay on the correct domain
Element detection inconsistencies	Used visible identifiers and indexes carefully with fallback messaging
 Final Outcome
The agent successfully logs in (up to CAPTCHA).

Provides user-friendly prompts when manual steps are needed.

The project demonstrates end-to-end AI agent reasoning and execution in a safe and effective manner
