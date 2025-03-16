
# **Documentation Structure for M3L and GSS**

#### **1. Introduction**

- Overview of M3L and GSS.
- Purpose: Simplify UI/UX development with modularity and cross-application consistency.
- Key Features:
    - M3L defines page **structure** and **intents**.
    - GSS defines **styling**, **interactions**, and **accessibility**.

#### **2. Core Concepts**

- **M3L Basics**:
    - Meta Information (`title`, `description`, `author`).
    - `rating` table: `classification`, `public_approval`, `mimic_content_ID`.
    - Structure of the page (`layout`, `containers`, `content`).
- **GSS Basics**:
    - Global styles and themes.
    - Widget-specific styling.
    - Accessibility standards (e.g., tooltips, focus states).

#### **3. Intents and Events**

- **Intents in M3L**:
    - High-level actions (e.g., `accept`, `help`, `browse`).
    - How intents define **what** should happen.
- **Events in GSS**:
    - Mapping intents to user interactions (e.g., `on click`, `on hover`).
    - Input modality adaptability (mouse, touch, controller).

#### **4. Co-Chain Integration**

- How M3L connects with co-chains (e.g., SQeeL, Mimic).
- Resource links and dynamic updates.
- Examples:
    - Using SQeeL for asset grids.
    - Using Mimic for contextual guidance.

#### **5. Widgets**

- **Standard Widgets**:
    - `asset_grid`, `carousel`, `nav_menu`, `tooltip`, etc.
    - Required and optional fields.
- **Custom Widgets**:
    - How developers can define and integrate custom widgets.
- **State Management**:
    - Defining widget states (`active`, `disabled`, etc.) in M3L.

#### **6. Accessibility**

- Best practices for creating accessible GSS files.
- Examples:
    - Tooltips and focus management.
    - Color contrast recommendations.

#### **7. Examples**

- Full examples of M3L and GSS files:
    - Marketplace with carousel and asset grid.
    - Simple static content page with a hero section.
- Step-by-step walkthrough of building a page.

#### **8. Event Handling**

- How errors are managed via GSS (e.g., error widgets).
- How to style other types of events such as information, warning, confirmation (for purchases) and notification (for messages)
- How these various event types can be triggered
- Best practices for fallback behavior.

#### **9. Future Proofing**

- Placeholder fields for co-chains (e.g., `mimic_content_ID`).
- Suggestions for extending M3L and GSS (e.g., VR support, BMI (brain machine interface).

#### **10. AI-Assisted UI

- **Adaptive UI Adjustments**: AI optimizes widget placement, animations, and interface layout based on user behavior.
- **User Personalization**: The system learns from user interactions to adjust UI elements dynamically.
- **Contextual Assistance**: AI provides real-time recommendations and assists in navigation.
- **Privacy & Permissions**: AI features can be toggled in settings, ensuring user control over data and device access.
- **Integration**: AI parameters can be defined in M3L for UI customization and enhanced in GSS for styling preferences.

#### **11. Omni-Interface System**

- Seamless UI across multiple connected devices (desktop, mobile, wearables, AR/VR interfaces).
- Input modality detection (keyboard, mouse, controller, voice, haptic feedback, and future inputs like BMI).
- Adaptive widget reconfiguration based on the current input method.
- Cross-device synchronization for an uninterrupted user experience.

---

# Introduction to M3L and GSS

## Overview

M3L (Multi-Media Markup Language) and GSS (Global Style Sheets) are modular frameworks designed to simplify UI/UX development for decentralized applications (dApps), offering a seamless way to integrate structure and styling while ensuring compatibility with decentralized ecosystems. By separating structure and styling, M3L and GSS allow developers and designers to collaborate seamlessly while maintaining flexibility and performance.

### Purpose

- **M3L**: Defines the logical structure and functionality of the application. It focuses on the "what" by describing the page layout, widget configurations, and user intents.
- **GSS**: Manages the visual design and user interactions. It focuses on the "how" by defining styling, animations, and event mappings for different input modalities (mouse, touch, controller).

Together, M3L and GSS create a consistent and adaptable UI/UX environment across applications and devices.

### Key Features

#### **1. Separation of Structure and Styling**

M3L handles page layout and functionality, while GSS ensures consistent theming and interaction design. This separation allows:

- Developers to focus on application logic.
- Designers to focus on creating visually appealing and accessible designs.

#### **2. Modularity and Reusability**

- **M3L** defines high-level widgets like `asset_grid`, `carousel`, and `nav_menu` that can be reused across applications.
- **GSS** provides global styling rules, ensuring a consistent look and feel across all dApps using the same theme.

#### **3. Adaptability for Input Types**

GSS supports multiple input types (mouse, touch, controller) and allows developers to define how interactions are handled for each.

#### **4. Co-Chain Integration**

M3L seamlessly integrates with co-chains like SQeeL and Mimic:

- **SQeeL** handles data queries for widgets like `asset_grid`.
- **Mimic** provides contextual guidance and assistance.

#### **5. Performance Optimization**

- Once loaded, GSS files remain consistent across applications, reducing network traffic and computation.
- Shared styles enhance cross-application performance.

#### **6. Keyframe Animations**

- Special keyword used for all widgets `Keyframe` defines how an animation will take place (rather than relying on scripting). This is so it's more intuitive for designers to pick it up. 
- Keyframes are based off of our senses and can be expanded in the future at this time it does the following:
   1. Visual - Can be the target device or any visual element like an external smart light.
   2. Audio - Handles sound any sound effects that are to be played when a user is perform this action type.
   3. Haptic - Deals with tactile response of the system so users can feel the interface.
   4. Resistance - Also, touch based can adjust the resistance of a connected device. Think PS5 controller adjusting the resistance on a trigger button.
   5. External - This is for devices that are not connected to the computing device being used. Think smart lights, thermostats and blinds.

Example:

```toml
[confirmation_button.animation.on_click]
duration = "1.5s"
keyframes = [
  { percent = 0,
    visual = [
      { target = "self", scale = 0.9, opacity = 0.6, easing = "ease-in" },
      { target = "confirmation_popup", action = "prepare", easing = "ease-in" },
      { target = "app.background", blur = 5, easing = "ease-out" }
    ],
    audio = [
      { target = "speakers", file = "@confirm_start.wav", volume = 0.3, easing = "linear" },
      { target = "switch-controller.speaker", file = "@switch_beep.mp3", volume = 0.4 }
    ],
    haptic = [
      { target = "controller", intensity = 0.4, easing = "linear" },
      { target = "ps5-controller.left-grip", intensity = 0.6, easing = "ease-in" }
    ],
    resistance = [
      { target = "ps5-controller.R2", intensity = 0.0, easing = "ease-in" },
      { target = "xbox-controller.LT", intensity = 0.3 }
    ],
    external = [
      { target = "smart-light.office", state = "on", color = "blue", brightness = 50, easing = "ease-in" }
    ]
  },

  {
    percent = 50,
    visual = [
      { target = "self", scale = 1.1, opacity = 1.0 },
      { target = "confirmation_popup", action = "show", easing = "ease-out" }
    ],
    audio = [
      { target = "speakers", volume = 0.5 }
    ],
    haptic = [
      { target = "controller", intensity = 0.5, easing = "ease-in-out" },
      { target = "ps5-controller.left-grip", intensity = 0.3 }
    ],
    resistance = [
      { target = "ps5-controller.R2", intensity = 0.7, easing = "ease-in-out" }
    ],
    external = [
      { target = "smart-light.office", color = "green", brightness = 100, easing = "linear" }
    ]
  },

  {
    percent = 100,
    visual = [
      { target = "self", scale = 1.0, opacity = 1.0 },
      { target = "app.background", blur = 0, easing = "ease-in" }
    ],
    audio = [
      { target = "controller.speaker", file = "@confirm_end.wav", volume = 0.5, easing = "ease-out" }
    ],
    haptic = [
      { target = "controller", intensity = 0.0, easing = "ease-out" },
      { target = "ps5-controller.left-grip", intensity = 0.0 }
    ],
    resistance = [
      { target = "ps5-controller.R2", intensity = 0.0, easing = "ease-out" }
    ],
    external = [
      { target = "smart-light.office", brightness = 50, easing = "ease-out" }
    ]
  },

  {
    percent = 100,
    visual = [
      { target = "self", scale = 1.0 },
      { target = "confirmation_popup", action = "finalize" },
      { target = "app.background", blur = 0 }
    ]
  }
]
```

### Widget Overview

M3L and GSS support a diverse range of widgets, categorized into **Low-Level Widgets** and **High-Level Widgets**:

#### **Low-Level Widgets**

- **Entrance**: This widget is here to create an entrance animation for the GSS file that is being currently loaded. This could be as simple as a screen fade or as complex as the designer wishes. Primarily meant for when a user changes their GSS theme.
- **Exit**: Just like the Entrance widget, this one is designer for when users leave or want to change out their GSS theme. This is meant to create a friendly transition into the new environment or returning to their real desktop.
- **[Window](#window-widget)**: Creates a new widowed object within the virtual desktop so that users can contain a application.
- **Fullscreen**: Not sure if this should be a widget type, but could describe a system where we want to take a full screen to show widgets. Common use would be console, mobile and desktop environments.
- **[Frame](#frame-widget)**: A Frame widget is one that is meant to contain multiple widgets (including other frames). Types: Grid, Relative, Absolute and Flex.
- **[Side Bar](#side-bar-widget)**: This is a special type of frame widget that is designed to only take the area of a side of the screen: left or right.
- **[Primary Button](#primary-button-widget)**: This button is specifically designed as a call to action button, meaning you want the user to click this button over any other.
- **[Secondary Button](#secondary-button-widget)**: This is designed to complement the primary button for things like cancel, back or skip.
- **[Image Button](#image-button-widget)**: This button is designed for specific applications where the M3L developers wish to have a custom button that is not an icon.
- **[Confirmation Button](#confirmation-button-widget)**: This button is designed to confirm a major action or event by the user. Think purchasing an item or signing a contract. This could be a click and hold or a slide confirmation, depending on the GSS designer.
- **[Toggle Button](#toggle-button-widget)**: This button is designed as a true / false action type to indicate when a event is triggered or not. Think a light switch or a setting option that is either yes or no.
- **[FAB Button](#floating-action-button-widget)**: A Floating Action Button (FAB) is a prominent, circular button designed for a key action (e.g., “New Post,” “Compose,” or “Start Chat”). It often floats above other UI elements and can be draggable if desired.
- **[Header](header-widget)**: This classifies text styling for headers between H1 - H6, that brings emphasis to a page / UI.
- **[Paragraph](paragraph-widget)**: Used for normal inline text.
- **[List](list-widget)**: Used for both ordered and unordered text lists
- **[Highlight](highlight-widget)**: Emphasizes words or phrases with a background color.
- **[Hyperlink](hyperlink-widget)**: Handles inline and block-level links. Supports on-hover effects, tooltips, and external/internal links.
- **[Table](table-widget)**: Creates a table supporting header rows, column alignment, and cell customization.
- **[Line Break](line-break-widget)**: Allows for custom styling of section separators.
- **[Blockquote](blockquote-widget)**: Handles markdown-style blockquotes (>).
- **[Code Block](code-block-widget)**: Handles markdown-style code blocks (``` or `). Should have easy copy options for ease of use.
- **[Check Item](checkitem-widget)**: This is meant to create check boxes for things such as task list within text (not to be confused with check boxes which have their own dedicated widget).
- **[Markdown](markdown-widget)**: Widget that is capable of parsing markdown files to be displayed on screen.
- **Text Box**: Allows for single-line user input.
- **Text Area**: Multi-line input for larger text blocks.
- **Checkbox**: For binary selections, users can check one or more items.
- **Radio Button**: Allows a single selection from multiple options.
- **Navigation Box (Text Bar)**: A widget designed for displaying and interacting with breadcrumbs, helping users navigate hierarchical structures such as file systems, page directories, or web navigation paths.
- **Scroll Area**: Indicates additional content is available via scroll or pan.
- **Drop Menu**: A dropdown list of options.
- **Sliders**: For selecting a value or range within a spectrum.
- **Tooltip**: Provides contextual information when a user hovers or focuses on an element.
- **Progress Bar**: Visualizes progress toward a goal.
- **Cards**: Compact content containers often used for showcasing assets or information.
- **Posters**: Larger cards that dominate the view, particularly on mobile.
- **Banner**: A banner acts much the same as a card widget, however its designed in a horizontal format whereas cards are more vertical. Banners can fill the space in parent widget or you can have margin.
- **Screenshot**: A flexible draw area for custom shapes or graphics, which is useful when users need to share what they see on screen.
- **Carousel**: Automatically cycles through various content, like images or promotions.
- **Break**: A simple widget used to visually divide sections of content. Supports horizontal and vertical orientations with customizable styles.
- **Toolbar**: Houses multiple buttons or tools for modifying a target section.
- **Floating Menu**: Context-sensitive menu that activates on events (e.g., right-click, hover).
- **Graph (Interactive)**: Generates visualizations based on input data; allows interactions if the data is editable.
- **Timeline**: A graph-like structure for events over time, expanding only horizontally.
- **Waterfall Charts**: Displays a continuous stream of data over time, often used for visualizing RF signals, sensor data, or other time-based intensity variations.
- **Gantt Charts**: This widget allows the use of Gantt charts which inherits timeline widget.
- **Roadmap**: Widget that depicts a roadmap for a project. Contains markers that are designed for additional information.
- **Skill Tree**: this widget creates a skill tree like widget that allows nodes (cards) to be activated when the parent of that node is 'activated'
- **Badge**: This widget is meant to act between the an icon and a card. It allows more area that shows an icon and a name, but when 'viewed' can expand into a full description. It can also be 'unlocked'.
- **Spellcheck**: Highlights misspelled words with corrections shown in a tooltip. Need to also create an option for spell help, in order to teach users how to spell rather than do it for them...
- **Autocomplete**: Assists in writing by providing options to autocomplete words allowing for faster input. 
- **Item Grid**: Displays items in a controller-friendly layout.
- **Video**: Plays videos with predefined controls and settings.
- **Popup**: Creates modals for warnings, errors, confirmations, or informational messages.
- **Notification Panel**: This is a listing of notifications from the application being used.
- **Toast**: Close to a popup but is designed to only show up for a limited amount of time then disappear (stays in the notifications menu)
- **Achievement**: The Achievement widget is a type of toast message that can be used to track and reward user behavior within your application.
- **Date Picker**: Allows users to select dates.
- **Color Picker**: Allows users to select a color (normally vis a pallet)
- **Tree View**: Represents hierarchical data (e.g., directories).
- **Object Tree**: This works like a tree view with the exception that is meant for object. Useful in systems that need to maintain objects on screen.
- **Poll Widget**: Presents a multiple-choice question and shows aggregated results.
- **Rating Widget**: This widget type is meant to define a rating system. It must at least have two rating types but can be as much as defined in the M3L file. Most common is a 5 star system.
- **Classification Widget**: This widget is responsible to classifying content which is crucial on social system where user interaction suggests content. This is designed to show who is the intended audience. It also has a field allowing users to describe why they choose this classification.
- **Reaction Widget**: This widget provides a system that allows users to react to another widget. This can consist of emoji or GIFs.
- **Status Bar**: Displays relevant statistics or information at the bottom of the screen.
- **Split View**: Divides the screen into two or more resizable panels.
- **Docking Widget**: Allows UI elements to be draggable and dockable to predefined locations (top, left, right, bottom, or floating).
- **Context Menu**: A styled menu that appears around a focal point, providing quick access to tools and actions.
- **Kanban Board**: A drag-and-drop task management board that organizes items into columns representing different workflow states.
- **Form Builder**: Enables structured data entry with dynamic validation and multi-step capabilities.
- **Node Grid**: A grid-based system where users can place and connect nodes for flowcharting, visual programming, or logic structuring.
- **Shapes**: Allows users to draw and scale shapes on screen along with adding additional text to those widgets.
- **Chat Widget**: Supports real-time messaging, reactions, and user status indicators.
- **Hero Section**: Captures user attention with headers, sub-headers, and call-to-action buttons.
- **Settings**: This widget contains settings for the current application that a user can control per the M3L developer and GSS designer. 
- **Pause menu**: Opens a pause menu widget that allows users to select from multiple options. meant for controllers but could be used by K&M by pressing pause break.
- **TOS Widget**: The terms of service widget is a standardized widget specifically for TOS regarding agreements made (such as using a co-chain). Has a accept and reject button and a scroll requirement.
- **Find/Replace Widget**: This is meant to find text within a specified context. 
- **Clock/Schedular**: This is meant as a design system for a clock also serves as a scheduling agent.
- **Calendar Widget**: This is meant to draw a calendar on screen, meant for scheduling events. Users can have multiple calendars but all users have a personal calendar.
- **Scheduler Widget**: The scheduler widget complements the calendar widget so that users can scheduler events on a calendar. 
- **Affiliate Widget**: This is meant for referring other users to products or services. 
- **Ad Widget**: This is meant to be a quick easy way to create Ads for the Ad hub (a Ad hub is where users can generate AdCoin so they have an Ad free experience)
- **Onboarding Widget**: This widget type assists with onboarding new users to an application or interface. This is done by directing users attention to various widgets with pop-ups that explain what each element does.
- **Avatar Widget**: This is meant to showcase a users digital Avatar on UndChain. *This is something provided inside of Player2*

#### **High-Level Widgets**

- **Asset View**: Provides a comprehensive shopping experience with product grids, sorting tools, a shopping cart, and detailed asset sections.
- **Desktop**: This widget is really meant for the launch screen for UndChain, but it makes sense to also make this a Widget. Should have functions such as the coking widget for window management.
- **Home Screen**: This is mean to be a space where users can openly share media on their own dedicated page. Think music, videos, articles as well as things they like and posts made to SMACK.
- **Website**: Sets up a general website that can contain pre-defined sections. Allows for blank widgets so devs can make custom sections.
- **Spreadsheet**: A grid-like table supporting formulas, edits, and data visualization.
- **Text Editor**: Rich text editing with formatting tools, suggestions, and AI-powered generation.
- **IDE**: A code editor with syntax highlighting, debugging tools, and project navigation.
- **Content Area**: Combines a canvas, sidebars, and list views for CAD or visual editing tasks.
- **Map**: Displays geographic or abstract data with layers, POIs, and animations.
- **Forum Widget**: Enables threaded discussions for asynchronous communication.
- **Video Player**: Advanced media playback with interactivity, previews, and OSTR (On-Screen Text Reader).
- **Live View**: Allows interactive presentations or remote tutorials.
- **Wiki View**: Editable content area with permissions and collaboration tools.
- **News Feed**: Displays content in a scrollable feed with filters.
- **Wizard Widget**: Guides users through multi-step processes or settings.
- **Dashboard**: Aggregates widgets like graphs and spreadsheets for data visualization and navigation.
- **Paint**: High level paint widget that allows users to draw custom shapes on screen. Includes layers, a object panel, the ability to imagine using Mimic and save on chain.

### Why Use M3L and GSS?

1. **Simplicity**:
    
    - Clean, readable syntax makes it easy to define application structure and styling.
    - Developers no longer need to mix logic and presentation.
2. **Consistency**:
    
    - GSS themes provide a unified look and feel, ensuring user familiarity across different applications.
3. **Extensibility**:
    
    - M3L and GSS are designed to support future features like VR, voice input, and AI-driven interfaces. For example, Mimic could analyze user behavior and provide contextual guidance or suggestions, such as highlighting the best path through a shopping application based on previous preferences, or enabling advanced voice commands for navigation and data entry.
4. **Developer and Designer Collaboration**:
    
    - M3L defines what happens, while GSS defines how it happens, creating a clear boundary between development and design.

### Example Workflow

1. **Developer** creates an M3L file defining the structure and functionality of the page.
2. **Designer** writes a GSS file that applies global styling and interaction rules.
3. **Co-Chain Integration**:
    - The M3L file references resource links from co-chains like SQeeL or Mimic.
    - Co-chains provide dynamic content or contextual assistance as needed.

### Who Should Use This Documentation?

This documentation is intended for developers building applications with M3L and GSS. It provides:

- A technical understanding of how to define page structures and intents in M3L.
- Guidelines for creating consistent and accessible styling in GSS.
- Examples and best practices for integrating co-chains and handling dynamic content.

By the end of this documentation, you will have a clear understanding of how to build modular, scalable, and visually consistent applications using M3L and GSS.

---

# Core Concepts

## M3L Basics

M3L focuses on defining the logical structure and functionality of your application. It provides a clean, declarative syntax for laying out pages, configuring widgets, and specifying user intents.

### Key Components

#### **1. Meta Information**

Meta information is used to describe the overall purpose and categorization of the page. Common fields include:

```toml
[meta]
title = "Page Title"
description = "Brief description of the page."
author = "@username"

[rating]
classification = "Everyone"  # Content rating for audience suitability.
public_approval = 85          # Sentiment score based on user feedback ranges between 0 - 100. 0 means no rating.
mimic_content_ID = ""        # Placeholder for Mimic integration.
content_type = "marketplace" # Defines the type of page.
```

#### **2. Layout and Containers**

The `layout` section defines the structure of your page using containers. Containers are flexible, allowing you to group and organize content hierarchically.

```toml
[layout]
[[layout.container]]
id = "main"
type = "grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" },
    # { link = "@Auction_House/asset_list.csv", type = "grid_items" } # Uncomment for debugging with static data
]

[[layout.container]]
id = "footer"
type = "static_content"
source = "@Auction_House/promotions.md"
```

### Intents

Intents describe **what** an element is meant to do. They are high-level actions like `browse`, `accept`, or `navigate`. Intents are defined in the M3L file and mapped to specific events in the GSS file.

```toml
[[layout.container.content]]
type = "buy_button"
intention = "accept"
resources = [
    { link = "SQeeL://Auction_House/buy" },
    { link = "Mimic://User_Guide/buy_button" }
]
```

### Resources

Resources define the data or actions associated with a widget. These can come from co-chains like SQeeL or Mimic, or from pre-defined text sources such as a CSV file. For example, static resources can be used during development for debugging purposes or to create applications with fixed content.

```toml
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" },
    { link = "Mimic://Recommendations/asset_grid", type = "recommendations" }
]
```

## GSS Basics

GSS defines how elements in the M3L file are styled and how users interact with them. It supports global theming, event mappings, and accessibility features.

### Key Components

#### **1. Global Styling**

GSS files provide a consistent look and feel across applications by defining global styles for fonts, colors, and layouts.

```toml
[global]
body.font-family = "Orbitron, sans-serif"
body.background-color = "#f0f0f0"
body.color = "#333"
```

#### **2. Widget-Specific Styling**

Each widget type in M3L can have specific styles defined in GSS.

```toml
[buy_button]
background-color = "#007BFF"
color = "#fff"
padding = "10px"
border-radius = "5px"
hover.background-color = "#0056b3"
```

#### **3. Event Mapping**

Events map M3L intents to specific interactions based on input types (mouse, touch, controller). Generic button names such as `Action`, `Cancel`, and `Menu` allow developers to create device-independent mappings. This ensures that controllers can be dynamically remapped based on user preferences or device capabilities.

```toml
[buy_button.interactions]
accept.mouse = "on click"
accept.touch = "on long press"
accept.controller = "on button press:Action"
```

#### **4. Animations**

GSS can define animations for dynamic content and transitions.

```toml
[animations.fade_in]
type = "fade-in"
duration = "1s"
trigger = "on load"
target = "carousel.item"
```

#### **5. Accessibility Features**

Accessibility options ensure that all users can interact effectively with the application. For example, M3L widgets support keyboard navigation using `tab` and `enter`, while GSS can define properties like `aria-label` for screen readers. Accessibility options like tooltips and focus management can be defined in GSS.

```toml
[tooltip]
background-color = "#000"
color = "#fff"
font-size = "12px"
padding = "5px"
trigger.help.mouse = "on hover"
trigger.help.touch = "on tap"
```

### Summary

M3L and GSS work together to define the structure and styling of your application. M3L provides the logical foundation, while GSS ensures a consistent, accessible, and engaging user experience across all applications.

---

# Intents and Events

## Intents in M3L

Intents in M3L describe **what** a widget or element is meant to do. They are high-level actions that specify the purpose of a widget without prescribing how the interaction occurs. This abstraction allows developers to define functionality in a declarative manner, leaving the specifics of user interaction to GSS.

### Examples of Intents

- **`navigate`**: Directs the user to another page or section of the application, such as hyperlinks or buttons that jump to a different screen.
- **`accept`**: Represents a primary action, such as confirming a purchase or submitting a form.
- **`help`**: Indicates a need for contextual assistance, such as displaying a tooltip or triggering guidance from Mimic.
- **`browse`**: Used for navigational or exploratory actions, such as scrolling through a grid of assets.
- **`cancel`**: Represents actions to close or abort a process.
- **`toggle`**: Switches the state of a widget, such as turning a feature on or off.

Note: Intents also support Markdown as the standard format for text, allowing inline navigation links and resource integration. This ensures developers have a familiar and flexible way to manage text-based linking.
### Defining Intents in M3L

Intents can handle navigation by specifying links to other M3L pages or resources. This is common for buttons, hyperlinks, or navigation menus. Intents are specified within the `layout.container.content` section in an M3L file. Each intent is associated with a widget type and optional resources to define its behavior.

#### Examples:

**Primary Action (Accept Intent):**

```toml
[[layout.container.content]]
type = "buy_button"
intention = "accept"
resources = [
    { link = "SQeeL://Auction_House/buy" },
    { link = "Mimic://User_Guide/buy_button" }
]
```

In this example:

- The widget type is `buy_button`.
- The intent is `accept`, indicating a primary action.
- Resources link to co-chains that handle the associated functionality.

**Navigation (Navigate Intent):**

```toml
[[layout.container.content]]
type = "hyperlink"
intention = "navigate"
resources = [
    { link = "@Undline/my_assets.m3l" } # Points to another M3L page on the creator's site
]
text = "View all my assets"
```

In this example:

- The widget type is `hyperlink`.
- The intent is `navigate`, specifying that clicking the link will navigate to another page.
- The resource defines the destination of the link.

**In-Line Markdown Links:**

```markdown
For more details, [click here](@Undline/my_assets.m3l).
```

- Inline navigation links can use Markdown syntax to reference M3L pages or co-chain resources.

**Images with Markdown:**

```markdown
![Product Image](@Undline/assets/image.jpg)
```

- Images can reference local assets or external resources using similar Markdown conventions.
- The resource defines the destination of the link.

**Contextual Help (Help Intent):**

```toml
[[layout.container.content]]
type = "tooltip"
intention = "help"
description = "Hover here for more information."
resources = [
    { link = "Mimic://Help/tooltip_assistance" }
]
```

In this example:

- The widget type is `tooltip`.
- The intent is `help`, requesting contextual assistance.
- Resources link to co-chains like Mimic for guidance.

**Exploration (Browse Intent):**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
```

In this example:

- The widget type is `asset_grid`.
- The intent is `browse`, enabling users to explore the grid of assets.
- Resources provide the data for the grid items.

**Cancel Action (Cancel Intent):**

```toml
[[layout.container.content]]
type = "cancel_button"
intention = "cancel"
resources = [
    { link = "SQeeL://Auction_House/cancel_order" }
]
```

In this example:

- The widget type is `cancel_button`.
- The intent is `cancel`, allowing users to abort a process.
- Resources define the action for cancellation.

**State Toggle (Toggle Intent):**

```toml
[[layout.container.content]]
type = "switch"
intention = "toggle"
resources = [
    { link = "SQeeL://Settings/toggle_feature" }
]
```

In this example:

- The widget type is `switch`.
- The intent is `toggle`, enabling users to change a state.
- Resources handle the logic for the toggle action.

## Events in GSS

Events in GSS define **how** user interactions map to intents specified in M3L. This separation ensures flexibility, as developers can adapt interactions for different devices and input modalities.

### Event Mapping

Event mapping connects M3L intents to specific user interactions. GSS supports multiple input types, such as:

- **Mouse**: `on click`, `on hover`
- **Touch**: `on tap`, `on long press`
- **Controller**: `on button press:Action`

#### Example:

```toml
[buy_button.interactions]
accept.mouse = "on click"
accept.touch = "on long press"
accept.controller = "on button press:Action"
```

### Input Modality Adaptability

GSS enables developers to define device-independent interactions using generic input mappings, such as:

- **`Action`**: The primary button for confirmation or selection.
- **`Cancel`**: The secondary button for closing or dismissing.
- **`Menu`**: For accessing additional options.

This system allows for seamless remapping of controls and ensures consistent behavior across devices.

### Advanced Example with Multiple Intents

```toml
[tooltip.interactions]
help.mouse = "on hover"
help.touch = "on tap"
help.controller = "on button press:Menu"

[buy_button.interactions]
accept.mouse = "on click"
accept.touch = "on long press"
accept.controller = "on button press:Action"

[cancel_button.interactions]
cancel.mouse = "on click"
cancel.touch = "on double tap"
cancel.controller = "on button press:Cancel"
```

In this example:

- The `tooltip` widget responds to the `help` intent based on input type.
- The `buy_button` widget maps the `accept` intent to different interactions depending on the device.
- The `cancel_button` maps the `cancel` intent to device-specific interactions.

### Summary

- **M3L Intents**: Define high-level actions that describe **what** should happen.
- **GSS Events**: Map intents to specific interactions, defining **how** users perform those actions.

This separation of concerns enhances modularity, adaptability, and maintainability, making M3L and GSS ideal for modern, multi-device applications.

---

# Co-Chain Integration

## Overview

M3L and GSS seamlessly integrate with co-chains to provide dynamic content, contextual guidance, and enhanced functionality. By leveraging co-chain resource links, developers can create applications that pull data, interact with AI systems, and maintain real-time updates—all within a decentralized ecosystem.

### Key Co-Chains

1. **Pages**: The co-chain where M3L and GSS are created and managed. It acts as the backbone for content delivery and UI/UX definitions.
2. **SQeeL**: Handles data queries, enabling applications to fetch and display structured data in widgets like `asset_grid` or `spreadsheet`.
3. **Mimic**: Reads contextual information, such as tooltips, to provide AI-powered guidance and suggestions.
4. **Live**: Supports live streaming and interactive content, such as video tutorials or collaborative sessions.
5. **Code Ledger**: Acts as a decentralized repository framework for managing and editing codebases.

## Resource Links

Resource links in M3L are the foundation for co-chain integration. These links point to specific co-chain resources, enabling dynamic data retrieval or actions. The order in which co-chains are listed determines their priority. For example, if two co-chains attempt to act on the same widget, the first-listed co-chain has precedence.

### Example Resource Link:

```toml
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" },
    { link = "Mimic://Recommendations/asset_grid", type = "recommendations" }
]
```

- **`SQeeL://Auction_House/assets.db`**: Fetches asset data for the `asset_grid` widget.
- **`Mimic://Recommendations/asset_grid`**: Provides recommendations for displayed assets.

## Dynamic Updates

Dynamic updates allow widgets to refresh their content automatically based on changes in co-chain data or user actions. This ensures that applications remain responsive and up-to-date.

### Example: Dynamic Asset Grid

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
update_on = "filter_change"
```

- **`update_on`**: Triggers the grid to refresh when a filter is applied or modified.

## Examples of Co-Chain Integration

### **1. Using SQeeL for Asset Grids**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
```

- **Description**: The `asset_grid` widget fetches and displays data from the SQeeL co-chain. It supports sorting, filtering, and pagination based on the provided dataset.

### **2. Using Mimic for Contextual Guidance**

```toml
[[layout.container.content]]
type = "tooltip"
intention = "help"
description = "Hover here for more information."
resources = [
    { link = "Mimic://Help/tooltip_assistance" }
]
```

- **Description**: While the developer defines the tooltip content, Mimic can read this information to provide enhanced contextual guidance or suggestions to users.

### **3. Using Live for Video Streaming**

```toml
[[layout.container.content]]
type = "video_player"
intention = "browse"
resources = [
    { link = "Live://Tutorials/getting_started" }
]
```

- **Description**: The `video_player` widget integrates with the Live co-chain to deliver live or recorded video content, enabling tutorials, collaborative sessions, or presentations.

### **4. Using Code Ledger for Code Management**

```toml
[[layout.container.content]]
type = "ide"
intention = "edit"
resources = [
    { link = "CodeLedger://Projects/MyProject" }
]
```

- **Description**: The `ide` widget connects to the Code Ledger co-chain, allowing developers to manage, edit, and collaborate on codebases in a decentralized environment.

## Summary

- **Pages**: Hosts M3L and GSS, providing a decentralized environment for creating and managing content.
- **SQeeL**: Powers data-driven widgets with robust querying capabilities.
- **Mimic**: Reads contextual information like tooltips to enhance user interactions with AI-driven assistance.
- **Live**: Facilitates live streaming and video content for tutorials and collaborations.
- **Code Ledger**: Serves as a decentralized repository for managing and editing codebases.

By integrating co-chains, M3L and GSS enable applications to deliver dynamic, responsive, and intelligent experiences tailored to user needs.

---

# Widgets

## Overview

Widgets are the building blocks of M3L, defining the structure and functionality of an application’s user interface. M3L provides a set of **standard widgets** for common use cases and supports **custom widgets** for developers who need unique layout flexibility. Each widget can manage its state, ensuring interactivity and responsiveness, while the styling and feel are always controlled by GSS to maintain consistency.

---

## Standard Widgets

M3L includes a comprehensive library of standard widgets that cover a wide range of UI needs. These widgets come with required and optional fields, allowing developers to customize their behavior and appearance.

---

### Examples of Standard Widgets

#### **1. Asset Grid**

- **Description**: Displays a grid of assets for exploration or purchase.
- **Required Fields**:
    - `type`: Defines the widget type (`asset_grid`).
    - `resources`: Points to the data source for the grid.
- **Optional Fields**:
    - `update_on`: Specifies events that trigger content updates (e.g., `filter_change`).

**Example:**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
update_on = "filter_change"
```

---

#### **2. Carousel**

- **Description**: Cycles through images or content items, often used for promotions or highlights. A carousel can be as simple as a set of rotating images or as complex as a collection of cards with images, descriptions, and buttons.
- **Required Fields**:
    - `type`: Defines the widget type (`carousel`).
    - `resources`: Points to the content source.

**Example:**

```toml
[[layout.container.content]]
type = "carousel"
resources = [
    { link = "@Undline/assets/promotions.toml", type = "carousel_items" }
]
```

---

#### **3. Tooltip**

- **Description**: Provides contextual information when a user hovers or focuses on an element.
- **Required Fields**:
    - `type`: Defines the widget type (`tooltip`).
    - `description`: The text to display.

**Example:**

```toml
[[layout.container.content]]
type = "tooltip"
description = "Hover here for more information."
```

---

#### **4. Navigation Menu**

- **Description**: Creates a menu for navigating between sections or pages.
- **Required Fields**:
    - `type`: Defines the widget type (`nav_menu`).
    - `items`: A list of menu options and their associated links.

**Example:**

```toml
[[layout.container]]
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l" },
    { text = "Products", resource = "@Undline/products.m3l" }
]
```

---

## Custom Widgets

Custom widgets allow developers to modify the **layout** and **structure** of a widget when standard widgets do not meet their needs. **Styling and interaction rules remain strictly controlled by GSS**, ensuring consistency across applications.

### Defining a Custom Widget

Custom widgets can be added to M3L by specifying a new `type` and associating it with custom functionality in the application.

**Example:**

```toml
[[layout.container.content]]
type = "custom_widget"
intention = "analyze"
resources = [
    { link = "CustomChain://Analytics/Data" }
]
```

- **Important Note**: Custom widgets cannot redefine styles or interactions; those are handled in GSS.

---

## State Management

M3L supports defining and managing widget states, allowing developers to create interactive and responsive UIs. States can be used to indicate a widget’s current status, such as:

- **Focus**: The widget is currently in use or selected.
- **Disabled**: The widget is inactive and cannot be interacted with.
- **Highlighted**: The widget is visually emphasized.

### Defining States in M3L

Widget states are defined using the `state` property within a widget configuration.

**Example:**

```toml
[[layout.container.content]]
type = "button"
state = { focus = true, disabled = false, highlighted = true }
order = 1
```

- **Order Parameter**: The `order` parameter specifies the tab order for widgets, allowing seamless navigation for keyboard and controller users.

---

## Widget Reference Library

For a comprehensive list of all standard widgets, including their required and optional fields, see the **Widget Reference** section in the Appendix. This includes detailed descriptions, examples, and supported parameters for each widget type.

---

## Summary

Widgets in M3L are highly flexible, offering both standard components for common use cases and the ability to define custom ones. State management ensures that UIs remain interactive and responsive, while the `order` parameter provides enhanced navigation capabilities. By leveraging M3L’s widget system, developers can create modular, dynamic, and engaging applications tailored to user needs while maintaining a consistent look and feel through GSS.

---

# Accessibility

## Overview

Accessibility ensures that all users, regardless of their abilities or the devices they use, can effectively interact with applications built using M3L and GSS. By adhering to best practices, developers can create inclusive applications that meet usability standards while leveraging the flexibility of M3L and the styling power of GSS.

---

## Best Practices for Creating Accessible GSS Files

1. **Focus Management**:
    - Define clear focus states for interactive widgets using the `focus` property in M3L and corresponding visual cues in GSS.
    - Ensure focusable elements have an appropriate `order` to facilitate logical keyboard and controller navigation.

**Example:**

```toml
[[layout.container.content]]
type = "button"
state = { focus = false, disabled = false, highlighted = false }
order = 2
```

```toml
[button.focus]
border-color = "#007BFF"
border-width = "2px"
background-color = "#f0f8ff"
```

---

2. **Tooltips for Contextual Guidance**:
    - Include tooltips for elements that require additional explanation.
    - Use GSS to style tooltips for readability and ensure they are triggered appropriately based on user interaction (e.g., hover, focus).

**Example:**

```toml
[[layout.container.content]]
type = "tooltip"
description = "Press this button to confirm your action."
```

```toml
[tooltip]
background-color = "#000"
color = "#fff"
padding = "8px"
border-radius = "5px"
font-size = "12px"
trigger.help.mouse = "on hover"
trigger.help.focus = "on focus"
```

---

3. **Color Contrast**:
    - Ensure sufficient contrast between text and background colors to meet WCAG standards.
    - Use high-contrast modes for users with visual impairments.

**Example:**

```toml
[global]
body.background-color = "#ffffff"
body.color = "#000000"

[high_contrast]
body.background-color = "#000000"
body.color = "#ffffff"
```

---

4. **Keyboard and Controller Navigation**:
    - Use the `order` parameter to create logical navigation flows.
    - Ensure all interactive elements are reachable using a keyboard or controller.

**Example:**

```toml
[[layout.container.content]]
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l", order = 1 },
    { text = "Products", resource = "@Undline/products.m3l", order = 2 }
]
```

---

## Examples of Accessible Implementations

### **1. Tooltips and Focus Management**

Tooltips can provide additional context for users while maintaining visual clarity.

```toml
[[layout.container.content]]
type = "tooltip"
description = "Click here to learn more."
state = { focus = false }
```

```toml
[tooltip.focus]
border-color = "#00ff00"
background-color = "#333"
font-size = "14px"
```

### **2. High Contrast Modes**

Enable users to toggle between standard and high-contrast modes.

```toml
[[layout.container.content]]
type = "toggle"
intention = "toggle"
resources = [
    { link = "Settings://ToggleHighContrast" }
]
```

```toml
[high_contrast]
body.background-color = "#000"
body.color = "#fff"
```

---

## Future Integration

While M3L and GSS natively support accessibility features, co-chains like **Mimic** can enhance usability by providing contextual guidance or advanced interaction capabilities. For example, Mimic can analyze widget states and user behavior to suggest actions or streamline workflows.

Developers can also integrate any co-chain into the resource list of a widget to extend usability features. This ensures M3L remains open and adaptable for advanced environments, giving developers the freedom to innovate.

**Example with Multiple Co-Chains:**

```toml
[[layout.container.content]]
type = "tooltip"
description = "Click here for more information."
resources = [
    { link = "Mimic://Help/tooltip_assistance" }, # Mimic for AI guidance
    { link = "CustomChain://Usability/Help" }     # Custom co-chain for usability
]
```

---

## Summary

Accessibility in M3L and GSS is achieved through focus management, contextual guidance with tooltips, proper color contrast, and logical navigation flows. By following these best practices and leveraging co-chains like Mimic, developers can create applications that are inclusive, user-friendly, and compliant with accessibility standards while maintaining the flexibility to innovate with their own co-chains.

---

# Examples

## Overview

This section provides complete examples of M3L and GSS files to demonstrate how to build functional and visually consistent applications. Each example includes a step-by-step walkthrough to help developers understand the integration of widgets, co-chains, and styling. Additionally, a graphical editor is planned for the future to support developers who prefer visual tools over textual editing.

---

## Example 1: Marketplace with Carousel, Asset Grid, and Error Handling

### M3L File

```toml
[meta]
title = "Marketplace"
description = "A showcase of assets available for purchase."
author = "@Undline"

[rating]
classification = "Everyone"
public_approval = 95
content_type = "marketplace"

[layout]
[[layout.container]]
id = "header"
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l", order = 1 },
    { text = "Products", resource = "@Undline/products.m3l", order = 2 }
]

[[layout.container]]
id = "hero"
type = "carousel"
resources = [
    { link = "@Undline/assets/promotions.toml", type = "carousel_items" }
]

[[layout.container]]
id = "main"
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
update_on = "filter_change"

[[layout.container]]
id = "error"
type = "error_widget"
description = "Unable to load content. Please try again later."
```

### GSS File

```toml
[global] # Global styles for the entire page
body.font-family = "Roboto, sans-serif"
body.background-color = "#ffffff"
body.color = "#333"
body.font-size = "16px" # Root font size, used for rem units

[nav_menu] # Styles for the navigation menu
background-color = "#007BFF"
color = "#fff"
padding = "10px"

[carousel] # Styles for the carousel
item.margin = "1rem" # Using rem for consistent spacing
item.border-radius = "0.5rem"
item.shadow = "0 4px 6px rgba(0, 0, 0, 0.1)"
animation.type = "slide" # Adding an animation for carousel rotation
animation.duration = "2s"
animation.easing = "ease-in-out"

[asset_grid] # Styles for the asset grid
item.padding = "1.5em" # Using em for spacing relative to the font size of the grid item
item.border = "1px solid #ddd"
item.background-color = "#f9f9f9"
item.hover.border-color = "#007BFF"

[loading] # Sub-widget for loading states
animation.type = "fade" # Simple fade-in animation for loading state
animation.duration = "1s"
animation.easing = "linear"
content = "Loading..."

[error_widget] # Styles for error notifications
background-color = "#ffcccc"
color = "#900"
padding = "1em"
border-radius = "0.5rem"
font-size = "1rem"
position = "banner" # Options: banner, popup, toast
```

---

## Example 2: Simple Static Content Page with Hero Section

### M3L File

```toml
[meta]
title = "Welcome"
description = "A simple static page with a hero section."
author = "@Undline"

[rating]
classification = "Everyone"
public_approval = 90
content_type = "static_page"

[layout]
[[layout.container]]
id = "hero"
type = "hero_section"
header = "Welcome to Our Platform"
subheader = "Explore the best we have to offer."
cta_button = { text = "Get Started", resource = "@Undline/get_started.m3l" }
muted_button = { text = "Learn More", resource = "@Undline/learn_more.m3l" }

[[layout.container]]
id = "footer"
type = "static_content"
source = "@Undline/assets/footer_content.md"
```

### GSS File

```toml
[global] # Global styles for the entire page
body.font-family = "Arial, sans-serif"
body.background-color = "#f4f4f4"
body.color = "#333"
body.font-size = "16px" # Setting root font size for rem units

[hero_section] # Styles for the hero section
header.font-size = "2.5rem" # Using rem for scalable typography
header.color = "#007BFF"
subheader.font-size = "1.5rem"
subheader.color = "#555"
cta_button.background-color = "#007BFF"
cta_button.color = "#fff"
cta_button.padding = "0.625rem 1.25rem"
cta_button.border-radius = "0.3125rem"
muted_button.background-color = "#ddd"
muted_button.color = "#333"
muted_button.padding = "0.625rem 1.25rem"
muted_button.border-radius = "0.3125rem"

[footer] # Styles for the footer section
background-color = "#333"
color = "#fff"
padding = "1.25rem"
font-size = "0.9rem"
```

---

## Walkthrough: Building a Marketplace Page

### Step 1: Define the M3L Structure

1. Start with the metadata section to define the page’s purpose and audience.
2. Add layout containers for the navigation menu, carousel, and asset grid.
3. Specify resource links for dynamic content like the asset grid and promotions.
4. Include an error widget to handle content loading issues.

**Example Metadata and Layout:**

```toml
[meta]
title = "Marketplace"
description = "A showcase of assets available for purchase."
author = "@Undline"

[layout]
[[layout.container]]
id = "header"
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l", order = 1 },
    { text = "Products", resource = "@Undline/products.m3l", order = 2 }
]
```

---

### Step 2: Style the Page Using GSS

1. Define global styles for fonts and background colors.
2. Customize the appearance of each widget (e.g., `nav_menu`, `carousel`, `asset_grid`).
3. Add animations to enhance interactivity, such as carousel rotations or loading indicators.
4. Style the error widget to ensure visibility and usability.
5. Incorporate **em** and **rem** units for scalable and responsive designs.

**Example GSS Styles:**

```toml
[global] # Global styles
body.font-family = "Roboto, sans-serif"
body.background-color = "#ffffff"
body.color = "#333"
body.font-size = "16px"

[carousel] # Adding rotation animation
item.margin = "1rem"
animation.type = "slide"
animation.duration = "2s"
animation.easing = "ease-in-out"

[error_widget] # Error widget styling
background-color = "#ffcccc"
color = "#900"
padding = "1em"
border-radius = "0.5rem"
position = "popup"
```

---

### Step 3: Test and Iterate

1. Preview the page using the M3L engine to ensure dynamic content loads correctly.
2. Adjust styles, animations, and layout as needed for responsiveness and aesthetics.
3. Simulate error states to verify that the error widget behaves as expected.

---

## Summary

These examples demonstrate how M3L and GSS work together to create dynamic, styled, and accessible pages. Future graphical editors will simplify the process further, making it even easier for developers to build pages visually. By following these examples and walkthroughs, developers can leverage the full power of M3L, GSS, and co-chain integration to create robust applications.

---

# Event Handling

## Overview

Event handling in M3L and GSS allows developers to manage system and user-triggered events with precision and flexibility. These events include five primary types: **error**, **warning**, **information**, **confirmation**, and **notification**. Each event type has unique characteristics and can be styled to align with application design goals. Developers can also define how these events are triggered and implement fallback behaviors to ensure a seamless user experience.

---

## Event Types and Use Cases

### 1. **Error Events**

- **Purpose**: To inform users of a critical issue that requires immediate attention.
- **Common Uses**:
    - Failed form submissions.
    - Network connectivity issues.
    - Invalid data format received from a co-chain.

**Example M3L:**

```toml
[[layout.container.content]]
type = "error_widget"
description = "Unable to connect to the server. Please try again later."
```

**Example GSS:**

```toml
[error_widget]
background-color = "#ffcccc"
color = "#900"
padding = "1em"
border-radius = "0.5rem"
position = "popup"
font-size = "1rem"
```

---

### 2. **Warning Events**

- **Purpose**: To alert users about potential issues or risks.
- **Common Uses**:
    - Unsaved changes warnings.
    - Low disk space alerts.

**Example M3L:**

```toml
[[layout.container.content]]
type = "warning_widget"
description = "You have unsaved changes. Do you want to continue?"
```

**Example GSS:**

```toml
[warning_widget]
background-color = "#fff4cc"
color = "#856404"
padding = "1em"
border-radius = "0.5rem"
position = "banner"
font-size = "1rem"
```

---

### 3. **Information Events**

- **Purpose**: To provide users with non-critical updates or details.
- **Common Uses**:
    - Successful actions.
    - General system notifications.

**Example M3L:**

```toml
[[layout.container.content]]
type = "info_widget"
description = "Your profile has been updated successfully."
```

**Example GSS:**

```toml
[info_widget]
background-color = "#d1ecf1"
color = "#0c5460"
padding = "1em"
border-radius = "0.5rem"
position = "toast"
font-size = "1rem"
```

---

### 4. **Confirmation Events**

- **Purpose**: To request user approval for an action.
- **Common Uses**:
    - Deleting an item.
    - Submitting a payment.

**Example M3L:**

```toml
[[layout.container.content]]
type = "confirmation_widget"
description = "Are you sure you want to delete this item?"
cta_button = { text = "Yes", action = "delete_item" }
muted_button = { text = "No", action = "cancel" }
```

**Example GSS:**

```toml
[confirmation_widget]
background-color = "#e9ecef"
color = "#495057"
padding = "1em"
border-radius = "0.5rem"
position = "popup"
font-size = "1rem"
```

---

### 5. **Notification Events**

- **Purpose**: To keep users informed about background processes or general updates.
- **Common Uses**:
    - Download progress updates.
    - System maintenance reminders.

**Example M3L:**

```toml
[[layout.container.content]]
type = "notification_widget"
description = "Your download is 50% complete."
```

**Example GSS:**

```toml
[notification_widget]
background-color = "#e2e3e5"
color = "#383d41"
padding = "1em"
border-radius = "0.5rem"
position = "toast"
font-size = "1rem"
```

---

## Event Triggers and Widget-Specific Behavior

### Timeout Property

Developers can define a `timeout` property in the M3L file for widgets that interact with co-chains. If the co-chain does not respond within the specified time, the widget triggers a connection error. The default timeout is 44 seconds if not explicitly defined.

**Example M3L with Timeout:**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
timeout = 30 # Maximum wait time in seconds
```

**Example GSS for Timeout Handling:**

```toml
[asset_grid.loading]
animation.type = "fade"
animation.duration = "1s"
content = "Loading assets..."

[asset_grid.error]
description = "Unable to load assets within the allowed time."
icon = "timeout_error.png"
position = "banner"
```

---

### Widget-Driven Event States

Events are most commonly triggered by widgets based on their interactions with co-chains. For example:

- **Asset View Widget**: If the widget fails to receive data within the timeout, it triggers a connection error.
- **Form Widget**: Missing or invalid data results in an error returned by the co-chain.

**Example: Form Validation Error**

```toml
[form.error]
field-highlight = "#ffdddd"
dialog.message = "Phone number is required."
dialog.button = { text = "Fix Now", action = "focus_phone_field" }
```

### Data Parsing Error

If the data retrieved from a co-chain is in an invalid format, the widget attempts a retry. If the issue persists, an error is triggered, and a message is optionally sent back to the co-chain.

**Example:**

```toml
[asset_grid.error]
description = "Invalid data format received. Please contact support."
icon = "data_error.png"
position = "popup"
```

---

### Standardized Error Format

Co-chains are expected to return errors in a standardized format to ensure consistent handling across widgets. The required fields include:

- **Event Type**: Specifies the category (e.g., error, warning).
- **Event Name (Header)**: A concise title for the event.
- **Description**: A detailed explanation of the issue.

### Optional Fields

- **Icons or Images**: To visually represent the event.
- **Buttons**: To allow users to take corrective actions directly.

**Example of Standardized Error Response**:

```json
{
    "event_type": "error",
    "event_name": "Connection Timeout",
    "description": "Connection timed out while fetching assets.",
    "icon": "timeout_error.png",
    "buttons": [
        { "text": "Retry", "action": "retry_connection" }
    ]
}
```

---

## Best Practices for Fallback Behavior

1. **Default Styling**: Always provide default styles for event widgets to ensure usability if custom styles are missing.
2. **Graceful Degradation**: Ensure that events still display essential information even if advanced features fail.
3. **Retry Mechanisms**: Attempt automatic retries for transient issues, such as corrupted data or temporary network errors.
4. **Accessibility**: Ensure that event widgets are focusable and provide appropriate ARIA roles or labels for screen readers.

---

## Summary

Event handling in M3L and GSS is a robust system for managing user interactions and system notifications. By leveraging event types, dynamic triggers, and fallback behaviors, developers can create clear and responsive interfaces that keep users informed and engaged while maintaining accessibility and consistency.

---

# Future Proofing

## Overview

M3L and GSS are designed with extensibility in mind to ensure that applications can adapt to future technologies and user needs. By incorporating placeholder fields, encouraging modular design, and planning for advanced features like VR and BMI (brain-machine interface), the system remains flexible and robust over time.

---

## Placeholder Fields for Co-Chains

To ensure compatibility with future co-chains and advanced functionality, placeholder fields can be defined in the M3L file. These placeholders allow for seamless integration of upcoming features without requiring major changes to existing files. Placeholders should remain as `0` or `""` to indicate they are not yet in use.

**Example Placeholder for Mimic Integration:**

```toml
[meta]
mimic_content_ID = "" # Placeholder when Mimic is not yet live
```

**Example When Mimic is Live:**

```toml
[meta]
mimic_content_ID = "Mimic://Auction House/content ID" # Mimic integration for live contextual information
```

By maintaining placeholder fields, developers can future-proof their M3L files without risking malicious or unintended behavior. Only when explicitly updated should these fields hold active values.

---

## Suggestions for Extending M3L and GSS

### **1. Virtual Reality (VR) Support**

- **Goal**: Enable immersive user experiences by integrating VR-specific widgets and interactions.
- **Approach**:
    - Introduce spatial properties like `z-order` in GSS to manage depth and layering of widgets.
    - Expand M3L to support VR-specific attributes for enhanced 3D interactions.

**Possible Features:**

- `z-order` to control widget depth placement.
- Interaction models for VR controllers.

---

### **2. Brain-Machine Interface (BMI) Support**

- **Goal**: Facilitate hands-free interactions using brainwave-driven commands.
- **Approach**:
    - Extend M3L intents to include thought-based actions (e.g., `think_back` for page navigation).
    - Allow GSS to define visual feedback for BMI-triggered interactions.

**Possible Features:**

- Thought commands mapped to intents like `think_forward` or `think_select`.
- Integration of focus indicators tied to brainwave activity.

---

## High-Order Widget Compatibility

To ensure future high-order widgets remain compatible with existing GSS files, the design must include a listing of smaller widgets within each high-order widget. This ensures that:

1. **Backward Compatibility**: Widgets retain basic functionality and styling, even if the GSS file predates the widget.
2. **Comprehensive Styling**: New GSS files can fully implement styling for all widget components, improving user experience and visual consistency.
3. **Version Awareness**: If the M3L engine does not recognize a new high-order widget type, it will throw an error and attempt to fetch an updated version of the engine to interpret it.

**Example High-Order Widget Definition:**

```toml
[[layout.container.content]]
type = "dashboard"
components = ["graph", "text_editor", "button"]
```

**Example GSS Implementation:**

```toml
[dashboard]
background-color = "#f5f5f5"

[dashboard.graph]
border = "1px solid #ddd"

[dashboard.text_editor]
font-family = "Monospace"

[dashboard.button]
background-color = "#007BFF"
color = "#fff"
```

---

## Versioning in M3L Files

Every M3L file should include a version field in the `meta` table to indicate the version of M3L it was written with. This ensures compatibility checks and proper handling by the M3L engine.

**Example Meta Table with Version:**

```toml
[meta]
title = "Example Page"
author = "@Undline"
version = "2025.01.05.0" # Format: YYYY.MM.DD.subversion
```

---

## Auction House Promotion for Comprehensive GSS Files

GSS files that fully implement all available widgets in the current version of M3L will receive greater visibility in the Auction House. This ensures that developers prioritize keeping their GSS files updated and fully compatible with the latest features. Older GSS files that do not implement newer widgets will be ranked lower in search results to encourage adoption of comprehensive, future-proof designs.

**Example Note in Auction House:**

- **Featured GSS File**: "Cyberpunk Theme - Supports All Widgets"
    - Compatibility: Full
    - Accessibility: WCAG Compliant
    - Rating: 95%

---

## Summary

Future-proofing in M3L and GSS is achieved through thoughtful design choices, such as placeholder fields for co-chains, modular high-order widgets, versioning in M3L files, and incentives for comprehensive GSS files. By planning for advancements like VR and BMI support, the system remains adaptable and forward-looking, empowering developers to create applications that stand the test of time while maintaining strict security and consistency.

---

### **AI-Assisted UI: Revolutionizing User Interaction**

The **AI-Assisted UI** system is designed to enhance user interaction by dynamically adapting the interface based on behavior, preferences, and contextual needs. Unlike traditional static interfaces, this system evolves over time, learning from user activity while maintaining strict privacy controls.

---

## **Core AI Features**

### **Adaptive UI Adjustments**

- AI modifies widget placement, animations, and layout to improve usability.
- Dynamically resizes elements, highlights key actions, and simplifies complex interactions.
- Example: If a user consistently moves a toolbar to the left, AI suggests locking it there permanently.

### **Contextual Intelligence**

- AI tracks cursor movements, eye focus, and interaction history to determine user intent.
- Predictive assistance suggests shortcuts, form fills, or navigation hints before the user asks.
- Example: While typing a report, AI pulls relevant reference material from previous searches.

### **User Personalization & Learning**

- Adapts to user skill level, offering beginner-friendly or expert-level interfaces.
- Adjusts language complexity based on user expertise.
- Recommends interface tweaks based on past behavior, such as enlarging buttons for users who frequently misclick.

### **AI Debugging & UI Optimization**

- Detects usability bottlenecks and suggests UI fixes in real time.
- Automatically identifies and resolves layout inconsistencies.
- Example: If multiple users struggle to find a feature, AI suggests a more prominent placement.

---

## **Privacy & User Control**

### **Permission-Based AI**

- AI features can be toggled in the settings menu, allowing users to define data-sharing preferences.
- AI cannot override user input or make autonomous changes without approval.
- AI does not alter or interfere with the settings or pause menu to ensure a clear exit path if the system becomes intrusive.

### **AI Interruption & Override**

- The pause menu allows users to instantly disable AI assistance.
- Manual adjustments always override AI-generated suggestions.
- Example: AI repositions a button, but the user can revert it to its original placement.

---

## **Future Expansions & Considerations**

- AI-Assisted UI for AR/VR, enabling gesture-based and voice-controlled adaptive interfaces.
- AI-powered UI theme customization, allowing the system to generate UI themes based on user preferences.
- Advanced analytics to analyze user behavior trends, improving accessibility and personalization over time.

---

### **Final Thoughts**

The **AI-Assisted UI** system is a key feature designed to provide users with a seamless and intuitive experience by continuously adapting the interface to their needs. It ensures full user control, does not interfere with critical system functions, and offers a structured way to enhance accessibility and efficiency. This system sets a foundation for the future of intelligent UI design, balancing innovation with user autonomy. Expect this section to change as we evolve within M3L/GSS.

---

### **Omni-Interface System**

The **Omni-Interface System** system redefines how users interact with digital environments by enabling a **fluid, adaptive experience across multiple devices and input types**. Designed for flexibility, this system allows users to transition effortlessly between platforms while ensuring a consistent and optimized UI experience. This is the foundation of **Web4**, where digital environments adapt to users, creating a seamless, immersive experience beyond traditional computing.

---

## **Core Features**

### **1. Multi-Device Continuity**

- Supports **desktops, mobile devices, wearables, AR/VR interfaces, and emerging technologies**.
- Ensures a **seamless experience across multiple screens**, allowing users to switch between devices without losing progress.
- Enables **context-aware UI adjustments** based on the capabilities and constraints of the active device.
- **Example:** A user begins working on a desktop but moves to a tablet, where the interface adapts to touch-based input and screen size automatically.

### **2. Multi-Input Support**

- Detects **keyboard, mouse, controller, voice commands, haptic feedback, and biometric input (future-ready for BMI and neural interfaces)**.
- Dynamically adapts UI layouts and interactions based on the current input method.
- Allows **simultaneous multi-input**, enabling hybrid control schemes (e.g., voice and gesture-based navigation).
- **Example:** A user navigating with a controller can seamlessly switch to voice commands without disrupting workflow.

### **3. Multi-Output Device Integration**

- Supports **external smart devices** such as **smart bulbs, smart speakers, and haptic feedback systems** to extend UI interaction beyond traditional screens.
- Allows **real-time environmental adaptation**, such as adjusting room lighting based on the current application or providing **tactile feedback** for user actions.
- **Example:** When watching a movie, Omni-Interface can dim smart lights, adjust haptic chair vibrations during action scenes, and control external sound systems dynamically.

### **4. Cross-Device Synchronization**

- Ensures an uninterrupted user experience by synchronizing UI states and data across connected devices.
- Leverages **real-time network updates** to maintain consistency across screens.
- Supports **session persistence**, allowing users to resume tasks instantly when switching devices.
- **Example:** A paused media file on a desktop can instantly resume on a mobile device when picked up.

### **5. Dynamic UI Adaptation through GSS Media Queries**

- UI elements **resize, reposition, and reconfigure** dynamically based on screen size and aspect ratio, similar to CSS media queries.
- Enables **adaptive layout switching**, transforming the UI based on interaction needs.
- Prioritizes **essential features** for smaller screens while maintaining accessibility to full functionality.
- **Example:** A complex UI with multiple toolbars on a desktop transforms into a streamlined, gesture-based interface on a mobile device.

### **6. Context-Aware Customization**

- Provides **context-based UI modifications**, ensuring a user-centric interface that evolves with preferences.
- Implements **intelligent UI scaling** to enhance readability and usability without manual adjustments.
- **Example:** Users preferring high-contrast themes see automatic adjustments when moving to bright environments or different screens.

---

## **Privacy & User Control**

### **1. User-Defined Device Permissions**

- Users can specify which devices are allowed to interact within the Omni-Interface system.
- Ensures privacy by preventing unauthorized cross-device syncing.
- **Example:** A user can link their desktop and tablet for seamless transitions but restrict smart home devices from accessing sensitive applications.

### **2. Security & Data Synchronization**

- Maintains end-to-end encryption for all cross-device data transfers.
- Allows **fine-tuned privacy controls** over what information is shared across devices.
- **Example:** While a shopping cart syncs between devices, browsing history remains private unless explicitly enabled.

### **3. Adaptive AI-Assisted Interaction (Optional)**

- Can integrate with the **AI-Assisted UI system** to enhance responsiveness based on user preferences.
- AI can suggest **optimized layouts, preferred input methods, and accessibility enhancements**.
- Users can **toggle AI intervention** or revert to a traditional static UI approach.

---

## **Future Considerations & Expansion**

- **AR/VR Expansion**: Omni-Interface will extend to spatial computing, allowing users to interact with content in a fully immersive way.
- **Neural Interface Integration**: Future-proofing for **brain-machine interfaces (BMI)** to enable thought-driven navigation and commands.
- **Haptic & Sensory Feedback Support**: Enabling **touch-sensitive, resistive, and adaptive physical feedback** for richer interaction experiences.
- **Real-Time Collaborative Multi-Device Support**: Allowing multiple users to interact with shared UI elements across connected devices.

---

### **Final Thoughts**

The **Omni-Interface System** system is a **game-changer for digital interaction**, enabling a **seamless, responsive, and intelligent multi-device ecosystem**. Whether users switch between devices, combine input methods, or leverage AI for optimized interaction, **this system ensures a frictionless and future-ready experience**. This is the essence of **Web4**, where technology integrates seamlessly into daily life, responding dynamically to user needs and creating a truly **immersive digital environment**.

---
---

# Appendix: Widgets

## Overview
This appendix provides a comprehensive listing of all widgets supported by M3L and GSS, including their types, examples, and styling options. Widgets are categorized into **low-level widgets** (basic building blocks). Each widget includes a detailed description, example usage in M3L, and corresponding styling in GSS to help developers understand its purpose and implementation. 

**Note**: All setting and value entries are **not case-sensitive**; they are converted to lowercase during processing, ensuring consistent handling and easing development.

---

## Low-Level Widgets

### Window Widget

The **Window Widget** is a top-level UI container that provides a **draggable, resizable, and interactive** space for your M3L application. Each **window** can house child widgets (such as text, buttons, grids, etc.) while enabling advanced features like title bars, modal interactions, docking, and custom animations.

---

#### Core Features

1. **Title Bar and Controls**  
   - Displays a **title** and standard window controls (**close**, **minimize**, **maximize**, **pin**).  
   - **Optional**: You can hide or customize the title bar (`title_bar = false`).  
   - **Minimize** is **implicit** if the developer sets `minimize = true` under `controls`; the system automatically places the window into the **virtual desktop tray** when minimized.

2. **Layouts and Child Widgets**  
   - Embeds **child widgets** inside the window using any frame type (flex, grid, relative, absolute) if explicitly declared.  
   - Defaults to a **flex-based** layout if no explicit `layout` is specified.

3. **Draggability & Resizability**  
   - `draggable`: Lets users move the window by dragging the title bar.  
   - `resizable`: Lets users resize by dragging edges.  
   - `dockable`: Snaps the window to screen edges or other windows (the **docker** widget handles more advanced snapping).

4. **Modal Mode**  
   - `modal = true` blocks interaction outside this window until it’s closed, typically used for prompts or wizards.  
   - You can optionally define a rule like `modal_dismiss_on_outside_click = true` for automatically closing the modal if the user clicks outside.

5. **Animations & Transitions**  
   - **open**, **close**, and **resize** animations can be declared in GSS.  
   - Also supports advanced **keyframe** or **custom** animation files.  
   - Example: fade-in on open, custom `.ani` file on close, or keyframed shadow pulsation.

6. **Controls**  
   - A single property `controls = { ... }` toggles standard window buttons: `close`, `minimize`, `maximize`, `pin`.  
   - Style or replace them with custom designs in GSS.

7. **Multi-Device & Accessibility**  
   - **Keyboard navigation** (tab-focusing, arrow-key resizing), **touch** gestures, or **voice** commands via co-chains (like Mimic).  
   - Intelligent scaling for watch/mobile/console.  
   - Windows adapt to user preferences or device context in line with the **Omni-Interface System**.

8. **Nested Windows**  
   - Windows can be placed **inside other windows** for advanced layouts or subpanels.

9. **Window Dimensions**  
   - By default, a **Window** has a **default size** determined by the system (e.g., 60% of the parent’s width, 50% of its height).  
   - Override with `min_width`, `min_height`, `max_width`, `max_height`, `width`, `height`.  
   - These constraints can be manipulated by Pseudo or an AI system for dynamic layouts.

---

#### M3L Example

```toml
# -----------------------------------------------
#   M3L Snippet for Window Widget
# -----------------------------------------------

[window]
id = "settings_window"
title = "Application Settings"
title_bar = true
draggable = true
resizable = true
dockable = true
modal = false

# Window controls
controls = { close = true, minimize = true, maximize = true, pin = true }

[window.text]
id = "settings_text"
value = "Adjust your settings below..."

[window.button]
id = "save_button"
type = "CTA"
label = "Save Changes"
on_click = "UndChain/SettingsSave.psu"
```

**Notes on the M3L Section**:

- **Window ID**: `id = "settings_window"` is used for referencing or theming in GSS.  
- **Title**: “Application Settings” will appear in the title bar.  
- **draggable/resizable**: By default, both are `false`; we enable them here.  
- **Child Widgets**: We see a text widget (`settings_text`) and a button (`save_button`), each with an **id** for easy reference.  
- **Layout**: No explicit layout means the **Window** defaults to a **flex** frame internally.  
- **Minimize**: Because `controls.minimize = true`, the user can minimize to the tray at any time.

---

#### GSS Example

```toml
# ------------------------------------------------
#   GSS Snippet for Window Widget
# ------------------------------------------------

[window]
# If not defined, the default background color is #CCC
background = "/assets/window_bg.png"
border_radius = "8px"

# Demonstration of multiple shadows:
# We'll use an array of strings. Each string is one shadow definition.
# Negative blur => interpret as 'inset' or 'internal' shadow
shadow = [
  "5px 7px 15px rgba(0, 0, 0, 128)",
  "0px -5px -10px rgba(255, 0, 0, 96)"
]

[window.animation.shadow_pulse]
type = "keyframes"
steps = [
  {
    shadow = [
      "5px 7px 15px rgba(0, 0, 0, 64)",
      "0px -5px -10px rgba(255, 0, 0, 32)"
    ]
  },
  {
    shadow = [
      "5px 7px 15px rgba(0, 0, 0, 192)",
      "0px -5px -10px rgba(255, 0, 0, 128)"
    ]
  }
]
duration = "2s"
timing_function = "ease-in-out"
iteration_count = "infinite"

[window.titlebar]
height = "35px"
color = "#007BFF"
font = "bold 16px Arial"

[window.controls]
style = "flat"
icon_size = "14px"

[window.button]
font = "Poppins"
size = "1em"
bold = true

# Show a combined visual+audio open animation
[window.animation]
open = { 
  type = "fade-in", 
  audio = { 
    file = "pop_sound.wav", 
    delay = "0.2s" 
  }
}
close = "/custom_animations/window_rollup.ani"
resize = "smooth"
```

**Notes on the GSS Section**:

1. **Background**  
   - Demonstrates using a **local file** (`/assets/window_bg.png`). If not set, defaults to **#CCC**.

2. **Multiple Shadows via Array**  
   - `shadow` is defined as an **array** of strings; each string is one shadow.  
   - `5px 7px 15px rgba(0, 0, 0, 128)` means offsetX=5px, offsetY=7px, blur=15px, color=semi-black.  
   - `0px -5px -10px rgba(255, 0, 0, 96)` uses a **negative** blur (`-10px`) as a custom GSS rule to interpret it as an **internal/inset** shadow.  
   - This approach avoids multi-line strings and keeps everything cleaner in TOML.

3. **Shadow Animation**  
   - `shadow_pulse` keyframes: each step sets the entire array of shadow definitions.  
   - This can produce a pulsing effect, changing color or blur over time.  
   - Negative blur is an **inset** if that’s how your GSS engine interprets it.

4. **Open/Close Animations**  
   - **open**: fade-in plus an **audio** pop effect.  
   - **close**: points to a custom `.ani` file (`"window_rollup.ani"`).  
   - **resize**: the built-in `"smooth"` transition.

5. **Titlebar, Controls, Button**  
   - Basic styling for each region.  
   - `icon_size = "14px"` affects built-in close/minimize icons.

---

#### Advanced Considerations

1. **Docking Behavior**  
   - `dockable = true` integrates with a **docker** widget that auto-snaps windows to edges.  
   - Potential expansions: custom `snap_zones`, corner tiling, or multi-screen logic.

2. **Implicit Minimize**  
   - If `controls.minimize = true`, system automatically supports a tray minimize.  
   - Minimizing “pauses” the window except for priority tasks/alerts.

3. **Modal**  
   - `modal = true` ensures the window blocks background interactions.  
   - `modal_dismiss_on_outside_click = [true|false]` can allow auto-close if user clicks outside the window.

4. **Close vs. Hide**  
   - Close “destroys” the window and unsaved data.  
   - Minimizing or “hiding” keeps the UI state suspended.  
   - Future expansions might define `close_behavior = "destroy" | "hide"`.

5. **Omni-Interface Tie-In**  
   - Windows adapt across device types or input methods.  
   - Minimizing or resizing might behave differently on smaller or watch-like displays.

6. **Performance**  
   - Large multi-window setups can be memory-heavy—encourage devs to close or minimize windows not in active use.  
   - The system can auto-suspend windows after inactivity if desired.

---

#### Event Reference

| **Event**     | **Description**                                        |
|---------------|--------------------------------------------------------|
| `on_open`     | Fires once the window is displayed.                    |
| `on_close`    | Fires before the window is removed from display.       |
| `on_minimize` | Fires when minimized (if `controls.minimize = true`).  |
| `on_maximize` | Fires when maximized (if `controls.maximize = true`).  |
| `on_drag`     | Fires when the window is moved by the user.            |
| `on_resize`   | Fires each time the window’s edges are resized.        |
| `on_focus`    | Fires when the user’s focus returns to the window.     |
| `on_blur`     | (Optional) triggers when window loses focus.           |

**Tip**: You can define these events in your M3L or reference them from GSS (e.g., `[window.events.on_resize]`) for custom logic. If a future AI or Pseudo code needs to programmatically close/minimize a window, these parameters and events can be triggered or listened to.

---

#### Final Suggestions

- **Keep M3L Minimal**: Define structure & logic in M3L; push **visual** or **audio** definitions to GSS.  
- **Use Keyframes**: Animate **any** GSS property (shadows, backgrounds, transforms) for fluid UI transitions.  
- **Optimize for Accessibility**: Provide clear title bars, tab ordering, focus states.  
- **Test on Multiple Devices**: Confirm draggability/resizing works across desktop, mobile, watch contexts.  
- **Consider a Window Manager**: For advanced multi-window ecosystems (tray, layering, grouping, etc.).  

---

### **Frame Widget**

The **Frame Widget** serves as the foundation for organizing and structuring widgets within an M3L interface. Frames define how child widgets are positioned, aligned, and displayed within an application. **Frames can be nested within other frames**, enabling complex layouts while maintaining a clear and logical structure.

---

## **Core Concepts**

### **1. Frames vs. Windows**
- **Frame**: A structural container used to organize widgets within an application.
- **Window**: A simulated application environment that allows UI/UX testing and custom styling within a contained workspace.

**Frames do not manage application states (e.g., minimizing or closing) like Windows do; they focus purely on layout and positioning.**

### **2. Default Frame Behavior**
If an M3L developer does not specify a frame type, the system defaults to:
- **Frame Type**: `flex`
- **Alignment**: `center`
- **Padding**: `0`
- **Margin**: `0`

---

## **Frame Types & Properties**

### **1. Grid Frame**
Organizes widgets into a structured row/column layout.

#### **Fields**:
| **Field**    | **Description**                                               | **Example**           |
|--------------|---------------------------------------------------------------|-----------------------|
| `rows`       | Number of rows in the grid.                                   | `rows = 3`            |
| `columns`    | Number of columns in the grid.                                | `columns = 3`         |
| `gap`        | Spacing between rows and columns.                             | `gap = "10px"`        |
| `alignment`  | Aligns widgets in the grid (start, center, end, stretch).     | `alignment = "center"`|
| `margin`     | Spacing around the grid.                                      | `margin = "10px"`     |
| `padding`    | Spacing inside the grid container.                            | `padding = "5px"`     |
| `z_order`    | Stacking order of widgets within the grid (2D layering).      | `z_order = 1`         |
| `background_color` | Defines a background for the grid container.             | `background_color = "#eee"` |

#### **Example M3L Implementation**:
```toml
[frame]
type = "grid"
rows = 2
columns = 3
gap = "10px"
alignment = "center"
margin = "15px"
padding = "10px"
z_order = 0

[frame.button]
row = 2
col = 3
text = "Submit"
```

#### **GSS Styling Example**:
```toml
[frame.grid]
background_color = "#f5f5f5"
margin = "10px"
padding = "5px"
box_shadow = "0px 2px 5px rgba(0,0,0,0.1)"
```

---

### **2. Relative Frame**
Positions widgets dynamically based on an anchor point.

#### **Fields**:
| **Field**      | **Description**                                             | **Example**            |
|----------------|------------------------------------------------------------|------------------------|
| `anchor`       | Sets reference point (top-left, center, bottom-right).      | `anchor = "top-left"`  |
| `offset_x`     | Horizontal offset from the anchor.                         | `offset_x = "20px"`    |
| `offset_y`     | Vertical offset from the anchor.                           | `offset_y = "10px"`    |
| `background_image` | Optional background image for styling.                   | `background_image = "@Undline/assets/bg.png"` |

#### **Example M3L Implementation**:
```toml
[frame]
type = "relative"
anchor = "top-left"
offset_x = "20px"
offset_y = "10px"

[frame.image]
src = "@Undline/assets/logo.png"
```

---

### **3. Absolute Frame**
Allows precise positioning of widgets using x, y, and z coordinates.

#### **Fields**:
| **Field**      | **Description**                                             | **Example**          |
|----------------|------------------------------------------------------------|----------------------|
| `x`, `y`, `z`  | Exact placement within the parent container.               | `x = "50px", y = "100px", z = "1"` |

#### **Example M3L Implementation**:
```toml
[frame]
type = "absolute"
x = "50px"
y = "100px"
z = "1"

[frame.text]
content = "Welcome to M3L!"
```

---

### **4. Flex Frame**
Aligns widgets dynamically along an axis.

#### **Fields**:
| **Field**          | **Description**                                            | **Example**                |
|--------------------|------------------------------------------------------------|----------------------------|
| `direction`        | Specifies the axis for alignment (row or column).          | `direction = "row"`        |
| `wrap`             | Enables wrapping of widgets if space is insufficient.      | `wrap = true`              |
| `justify_content`  | Distributes space between widgets (start, center, end).    | `justify_content = "space-around"` |
| `align_items`      | Aligns widgets along the perpendicular axis.               | `align_items = "center"`   |

#### **Example M3L Implementation**:
```toml
[frame]
type = "flex"
direction = "row"
wrap = true
justify_content = "space-around"
align_items = "center"

[frame.button]
text = "Buy Now"
```

---

## **Key Features**
- **Nested Frames**: Frames can be nested within other frames for complex layouts.
- **Background Support**: Frames can have colors or images as backgrounds.
- **Padding & Margins**: Define spacing within and around frames.
- **Multiple Layouts**: Grid, Relative, Absolute, and Flex provide unique ways to structure widgets.
- **ID-Based Targeting**: Every frame (even when unnamed) has an implicit ID for easy reference.

---

## **Final Notes**
- Use `z_order` for future 3D layering support.
- Avoid deeply nested layouts beyond **three levels** for readability; external files are recommended after this point.
- Frames are fundamental in M3L UI design, and **choosing the right frame type ensures optimal user experience.**

---

### Side Bar Widget

A **Side Bar** is a dedicated container, pinned to the **left** or **right** edge of the screen (or parent window), typically for secondary navigation or additional tools. Internally, it behaves like a **Frame** (defaulting to a flex layout) so you can place child widgets easily.

---

#### Core Purpose
- A **Side Bar** organizes secondary navigation, filters, or extra tools outside the main workspace.
- Pinned to either **left** or **right**, it can be optional to **collapse** if screen real estate is needed.
- Because it’s essentially a **frame**, you can nest other widgets within it using any layout approach (but defaults to **flex**).

---

#### Core Fields

| Field        | Description                                                                    | Example                                  |
|--------------|--------------------------------------------------------------------------------|------------------------------------------|
| `id`         | Unique identifier for referencing in **Pseudo** or logic (not used by GSS).    | `id = "nav_side_bar"`                  |
| `side`       | Which edge the sidebar occupies (`left` or `right`).                           | `side = "left"`                        |
| `collapsible`| If `true`, allows the user to toggle the bar open/closed.                      | `collapsible = true`                     |
| `collapsed`  | Initial collapse state (true/false).                                           | `collapsed = false`                      |
| `resizable`  | If `true`, user can drag the sidebar’s edge to resize width.                   | `resizable = true`                       |
| `min_width`  | Minimum width if `resizable = true`.                                           | `min_width = "200px"`                  |
| `max_width`  | Maximum width if `resizable = true`.                                           | `max_width = "400px"`                  |
| `title`      | (Optional) Title displayed if the sidebar has a header area.                   | `title = "Navigation"`                 |
| `on_toggle`  | (Optional) Array of event actions triggered when the user collapses/expands.   | `on_toggle = [{ intent = "toggle_side_bar" }]` |
| `on_resize`  | (Optional) Array of event actions if the user resizes the bar.                 | `on_resize = [{ intent = "save_side_bar_width" }]` |

> **Note**: The side bar also hosts child widgets, e.g. `[side_bar.button]` or `[side_bar.list]`. If you don’t specify a layout, it defaults to **flex**.

---

#### Example M3L Snippet

```toml
# Minimal M3L snippet for the Side Bar widget

[side_bar]
id = "nav_side_bar"
side = "left"
collapsible = true
collapsed = false
resizable = true
min_width = "200px"
max_width = "400px"
title = "Navigation"

on_toggle = [
  { intent = "toggle_side_bar" }
]

on_resize = [
  { intent = "save_side_bar_width" }
]
```

**Explanation**:
- **side**: "left" or "right" decides which edge it anchors to.
- **collapsible** / **collapsed**: If `true`, user can hide or show the bar.
- **resizable**: `true` means user can drag an edge to change width, within `min_width` / `max_width`.
- **title**: (Optional) Shown if the sidebar has a header region.
- **on_toggle** / **on_resize**: Hooks into M3L event logic.

---

#### GSS Example

```toml
[side_bar]
background-color = "#F5F5F5"
color = "#333"
width = "250px" # default starting width
height = "100%"

# If you want a small border or shadow on the inside edge:
shadow = [ "-2px 0px 4px rgba(0,0,0,0.1)" ] # for left side

[side_bar.collapsed]
width = "0px"
overflow = "hidden" # or a minimal width if you prefer a small bar

[side_bar.resizable]
cursor = "col-resize" # only relevant at the boundary

[side_bar.titlebar]
height = "40px"
font-size = "1.1rem"
padding = "8px"
color = "#000"
background-color = "#E5E5E5"

[side_bar.animation.toggle]
# A simple transition for collapse/expand
property = "width"
duration = "0.3s"
timing_function = "ease-in-out"

[side_bar.animation.resize]
# If you want a smooth drag feedback or an after-drag snap.
property = "width"
duration = "0.2s"
timing_function = "linear"
```

**Explanation**:
1. `[side_bar]`: Default style, e.g., a light background, initial `width = "250px"`.
2. If anchored to the **right**, you might do a reversed shadow or define `[side_bar.side="right"]` scoping in GSS.
3. `[side_bar.collapsed]`: Force `width=0px` (or small) if user collapses it.
4. `[side_bar.resizable]`: Tells GSS to show a `col-resize` cursor at the boundary.
5. **Animations**: Use transitions or keyframes for toggling/resizing.

---

#### Advanced Considerations

1. **Layout Impact**: The side bar can push or overlay the main content. This might be a setting or GSS scoping (`overlay vs. push`).
2. **Collapsing Behavior**: If `collapsed = true`, do you show a small handle or an icon to expand it?
3. **Resizing**: Typically the user drags the boundary. The engine or your code might handle an `on_resize` event to store the new width.
4. **Title & Child Widgets**: If `title` is set, GSS can place a small title bar area. Child widgets `[side_bar.button]`, `[side_bar.list]`, etc., can populate the side bar contents.
5. **Side**: If `side = "left"`, you might define a right boundary for resizing; if `side = "right"`, the left boundary is the handle.
6. **Accessibility**: Provide keyboard or other means to collapse/expand.

---

#### Final Thoughts

A **Side Bar** is essentially a **specialized Frame** pinned to one screen edge, with optional **collapsing** and **resizing**. If you don’t specify a layout, it defaults to **flex**. M3L sets the basic fields (side, min/max width, collapsed), while GSS shapes its appearance and transition animations—maintaining clarity between structure and styling.

---

### Primary Button Widget

A **Primary Button** serves as a **prominent call-to-action** in an M3L interface. It is typically styled to stand out, indicating the most important or recommended action on a given screen—e.g., **“Submit,” “Proceed,”** or **“Buy Now.”**

#### Core Fields

|Field|Description|Example|
|---|---|---|
|`id`|Unique identifier for referencing the button in GSS or code.|`id = "submit_btn"`|
|`label`|Text displayed on the button face.|`label = "Submit"`|
|`icon`|Optional. Path to an icon or image if the button uses an icon.|`icon = "@Undline/assets/check.svg"`|
|`action`|A short string describing the button’s role or action.|`action = "submit_form"`|
|`target`|Resource, Pseudo script, or API call location.|`target = "@Undline/api/submit"`|
|`tooltip`|Text shown on hover/focus (if supported).|`tooltip = "Finalize submission"`|
|`disabled`|Disables interaction if `true`.|`disabled = false`|
|`loading`|Shows a loading state if `true`.|`loading = false`|
|`keyboard_shortcut`|Optional. Defines a key combo to trigger the button (if supported).|`keyboard_shortcut = "ctrl+s"`|
|`order`|Numeric ordering for keyboard or controller tab navigation. If none is provided, it’s auto-assigned (top-left to bottom-right).|`order = 1`|
|`on_click`|Specifies an array of event actions (intent, etc.).|`on_click = [{ intent = "submit_form" }]`|

> **Note**: We exclude styles (e.g., border, radius) from M3L to keep the markup minimal and push design to GSS.

---

#### Example M3L Snippet

```toml
# A minimal M3L snippet for the primary button widget

[primary_button]
id = "submit_btn"
label = "Submit"
action = "submit_form"
target = "@Undline/api/submit"
tooltip = "Click to finalize"
keyboard_shortcut = "ctrl+s"
order = 1

on_click = [
  { intent = "submit_form", target = "@Undline/api/submit" }
]
```

**Explanation**:

- **id**: "submit_btn" -> GSS or Pseudo references.
- **label**: "Submit" -> The textual face of the button.
- **action**: "submit_form" -> A short descriptor or link to internal logic.
- **target**: Could be a co-chain or local function.
- **tooltip**: Helps with a quick hint if your environment supports hover/focus tooltips.
- **keyboard_shortcut**: If the environment supports it, pressing "Ctrl+S" might trigger the button.
- **order**: Numeric priority used for tab or arrow navigation. Lower numbers get focus first.
- **on_click**: Ties into M3L event logic, calling "submit_form" on press.

---

#### GSS Example

```toml
[primary_button]
background-color = "#007BFF"
color = "#FFFFFF"
border-radius = "5px"
border = "1px solid #0056b3"
padding = "10px 20px"
font-family = "Arial, sans-serif"
font-size = "1rem"

[primary_button.hover]
background-color = "#0056b3"

[primary_button.disabled]
background-color = "#cccccc"
color = "#666666"
cursor = "not-allowed"

[primary_button.loading]
# Could show a spinner or change label
content = "Loading..."
cursor = "wait"

[primary_button.shadow]
# Note: You can define multiple shadow strings in this array if you want multiple shadows!
value = [ "2px 2px 4px rgba(0,0,0,128)" ]

[primary_button.animation.hover]
type = "scale-up"
duration = "0.3s"
timing_function = "ease-in-out"

[primary_button.animation.click]
type = "progress-fill"
duration = "0.5s"
timing_function = "ease-in"
```

**Explanation**:

1. `[primary_button]`: Declares style for this widget’s default state.
2. `[primary_button.hover]`, `[primary_button.disabled]`, `[primary_button.loading]`: Distinct states.
3. **Shadows**: Using an array-of-strings approach, if your GSS engine interprets each string as one shadow.
    - _You can list multiple strings to layer multiple shadows._
4. **Animations**: You can define separate animations ("hover", "click", etc.) referencing keyframes or built-in transitions.

---

#### Advanced Considerations

1. **Confirmation or Secondary Buttons**: For destructive or more cautious actions, consider a separate "confirmation" or secondary button widget.
2. **Disabled & Loading**: When `disabled = true`, all interactions are blocked. If `loading = true`, GSS can display a spinner or text override.
3. **Accessibility**: Provide `tooltip` or embed helper text for screen readers. Check keyboard focus states.
4. **Events**: `on_click` is the main event; you can add `on_focus`, `on_blur` in M3L or GSS if needed.
5. **Integration**: This widget can be embedded inside a window or frame, e.g. `[window.primary_button]`.
6. **Keyboard Shortcuts**: Not all environments may support `keyboard_shortcut`, but if they do, it’s a convenient way to speed up repeated actions.
7. **Tab Navigation**: The `order` field helps define which widget gets focus first when a user presses Tab or navigates via controller. If no order is specified, the system auto-assigns based on top-left to bottom-right scanning.

---

### Secondary Button Widget

A **Secondary Button** is used for supporting or less critical actions (e.g., "Cancel," "Back," or "Skip"). It typically blends into the interface more subtly than a primary button, but remains sufficiently noticeable for user interaction.

#### Core Fields

| Field             | Description                                                                                                    | Example                                     |
|-------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `id`              | Unique identifier for referencing in **Pseudo** or your own logic (not used by GSS).                          | `id = "cancel_btn"`                       |
| `label`           | Text displayed on the button face.                                                                             | `label = "Cancel"`                        |
| `icon`            | (Optional) Path to an icon or image if the button uses an icon.                                                | `icon = "@Undline/assets/close.svg"`      |
| `action`          | A short string describing the button’s role or action.                                                         | `action = "cancel_form"`                  |
| `target`          | Resource, Pseudo script, or API call location.                                                                 | `target = "@Undline/api/cancel"`         |
| `tooltip`         | Text shown on hover/focus (if supported).                                                                      | `tooltip = "Cancel and go back"`          |
| `disabled`        | Disables interaction if `true`.                                                                                | `disabled = false`                         |
| `loading`         | Shows a loading state if `true`.                                                                               | `loading = false`                          |
| `keyboard_shortcut` | (Optional) Defines a key combo to trigger the button (if supported).                                         | `keyboard_shortcut = "esc"`              |
| `order`           | Numeric ordering for keyboard/controller tab navigation. Defaults to auto if none given.                       | `order = 2`                                |
| `on_click`        | Specifies an array of event actions (intent, etc.).                                                            | `on_click = [{ intent = "cancel_form" }]`|

> **Note**: In M3L, we keep styling minimal. GSS is responsible for the visual aspects.

---

#### Example M3L Snippet

```toml
# A minimal M3L snippet for the secondary button widget

[secondary_button]
id = "cancel_btn"
label = "Cancel"
action = "cancel_form"
target = "@Undline/api/cancel"
tooltip = "Cancel and go back"
keyboard_shortcut = "esc"
order = 2

on_click = [
  { intent = "cancel_form", target = "@Undline/api/cancel" }
]
```

**Explanation**:
- **id**: "cancel_btn" is used for referencing in logic or Pseudo, not by GSS.
- **label**: "Cancel" is displayed on the button.
- **action**, **target**: Short descriptor plus resource pointer.
- **tooltip**: Quick user hint if environment supports hover/focus.
- **keyboard_shortcut**: Possibly triggers the same effect when pressing `esc`.
- **order**: The second button to focus during tab/arrow navigation.
- **on_click**: Ties into M3L event logic, e.g., "cancel_form".

---

#### GSS Example

```toml
[secondary_button]
background-color = "#CCCCCC"
color = "#333333"
border-radius = "4px"
border = "1px solid #999999"
padding = "8px 16px"
font-family = "Arial, sans-serif"
font-size = "1rem"

[secondary_button.hover]
background-color = "#BBBBBB"

[secondary_button.disabled]
background-color = "#eeeeee"
color = "#999999"
cursor = "not-allowed"

[secondary_button.loading]
# Could show a spinner or change the label
content = "Loading..."
cursor = "wait"

[secondary_button.shadow]
# Use an array-of-strings if you want multiple shadows.
value = [ "1px 1px 3px rgba(0,0,0,64)" ]

[secondary_button.animation.hover]
type = "scale-up"
duration = "0.3s"
timing_function = "ease-in-out"

[secondary_button.animation.click]
type = "pulse"
duration = "0.5s"
timing_function = "ease-in"
```

**Explanation**:
1. `[secondary_button]`: Declares styles for the default state (less vibrant than a primary button).
2. `[secondary_button.hover]`, `[secondary_button.disabled]`, `[secondary_button.loading]`: Specialized states.
3. **Shadows**: Insert multiple strings in the `value` array to layer multiple shadows.
4. **Animations**: Example includes a slight `scale-up` on hover and a `pulse` on click.

---

#### Advanced Considerations

1. **Custom Shapes**: If defining a custom polygon or 3D shape, some standard fields (e.g., `border-radius`) may not apply.
2. **Destructive vs. Non-Destructive**: If the action is destructive (e.g., "Delete"), a separate `destructive_button` might be warranted.
3. **Disabled & Loading**: Setting `disabled = true` or `loading = true` updates states in GSS accordingly.
4. **Keyboard Navigation**: The `order` field dictates tab or arrow focus. If omitted, the engine auto-assigns an order.
5. **Accessibility**: Provide `tooltip` or screenreader text. Confirm focus behavior if using unusual shapes.
6. **Integration**: This widget can appear inside `[window]`, `[frame]`, or other parent scopes.
   - **Parent Scoping**: GSS can apply different styles if you embed this inside `[card]`, e.g. `[card.secondary_button]`, which overrides or adds to the global `[secondary_button]` styling. This enables unique looks in different parent contexts without duplicating widgets.
7. **Keyboard Shortcuts**: Not all environments may honor `keyboard_shortcut`, but if they do, it’s a user-friendly timesaver.

---

#### Final Thoughts

A **Secondary Button** is a complementary control that provides a subdued but fully functional alternative to **Primary** or other call-to-action buttons. By storing styling in GSS while M3L focuses on logic fields, you maintain a clean architecture and consistent user experience.

---

### Image Button Widget

An **Image Button** primarily uses an image or icon as its face, but can also display **text** if desired (e.g., under or beside the icon). This makes it ideal for icon-based toolbars, but still flexible enough to include descriptive text where needed.

#### Core Fields

| Field              | Description                                                                                                      | Example                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| `id`               | Unique identifier for referencing in **Pseudo** or your own logic (not used by GSS).                            | `id = "music_icon_btn"`                  |
| `image`            | Path to an image or icon that forms the button face.                                                             | `image = "@Undline/assets/play_icon.svg"`|
| `label`            | (Optional) Text displayed alongside/under the image, depending on GSS.                                           | `label = "Play"`                          |
| `action`           | A short descriptor for the button’s role or action.                                                              | `action = "play_music"`                  |
| `target`           | Resource, Pseudo script, or API call location.                                                                   | `target = "@Undline/api/play"`           |
| `tooltip`          | Text shown on hover/focus (if supported).                                                                        | `tooltip = "Play Music"`                 |
| `disabled`         | Disables interaction if `true`.                                                                                  | `disabled = false`                         |
| `loading`          | Shows a loading state if `true`.                                                                                 | `loading = false`                          |
| `keyboard_shortcut`| (Optional) Defines a key combo to trigger the button (if supported).                                             | `keyboard_shortcut = "space"`            |
| `order`            | Numeric ordering for keyboard/controller tab navigation. Defaults to auto if none given.                         | `order = 3`                                |
| `on_click`         | Specifies an array of event actions (intent, etc.).                                                              | `on_click = [{ intent = "play_song" }]`  |

> **Note**: If you want purely an icon, omit `label`. If you want text as well, supply `label`. GSS determines how (or if) text is rendered.

---

#### Example M3L Snippet

```toml
# Minimal M3L snippet for the Image Button widget

[image_button]
id = "music_icon_btn"
image = "@Undline/assets/play_icon.svg"
label = "Play"   # Optional text
action = "play_music"
target = "@Undline/api/play"
tooltip = "Play Music"
keyboard_shortcut = "space"
order = 3

on_click = [
  { intent = "play_song", target = "@Undline/api/play" }
]
```

**Explanation**:
- **id**: Used for referencing in logic or Pseudo, not for GSS.
- **image**: The graphical face for the button.
- **label**: (Optional) If you want text near/under the icon.
- **action** / **target**: A short descriptor plus resource pointer.
- **tooltip**: Helpful for accessibility or clarifying icon meaning.
- **keyboard_shortcut**: Possibly triggers the button on a key press.
- **order**: Determines focus order for keyboard/controller.
- **on_click**: Ties into M3L event logic.

---

#### GSS Example

```toml
[image_button]
# Typically an icon or image, but you can arrange label if present.
background = "transparent"
border = "none"
cursor = "pointer"

[image_button.hover]
background = "rgba(255, 255, 255, 0.1)"

[image_button.disabled]
opacity = "0.5"
cursor = "not-allowed"

[image_button.loading]
opacity = "0.7"
cursor = "wait"

[image_button.shadow]
value = [ "2px 2px 4px rgba(0,0,0,64)" ]

[image_button.animation.hover]
type = "pulse"
duration = "0.3s"
timing_function = "ease-in-out"

[image_button.animation.click]
type = "zoom-in"
duration = "0.2s"
timing_function = "ease-in"
```

**Explanation**:
1. `[image_button]`: Minimal styling for a purely icon-based button.
2. If `label` is present, GSS designers might display it below or next to the image.
3. States like `[image_button.hover]`, `[image_button.disabled]`, `[image_button.loading]` match other button conventions.
4. **Animations**: Example includes `pulse` on hover, `zoom-in` on click.

---

#### Advanced Considerations

1. **Text + Icon Layout**: GSS can define how/where the `label` appears relative to the image. For instance, you can place the text below or to the right.
2. **Tooltips for Accessibility**: If no `label` is shown, tooltips or ARIA labels are crucial for screen readers.
3. **Shadows & Borders**: Optional, but can help the icon stand out. For custom shapes, you can ignore certain fields like `border-radius`.
4. **Disabled & Loading**: If `disabled = true` or `loading = true`, GSS can overlay spinners or reduce opacity.
5. **Keyboard Navigation**: `order` ensures the image button is in a logical place in the tab sequence.
6. **Parent Scoping**: If you embed in `[card]`, GSS can define `[card.image_button]` to override global `[image_button]` styles.
7. **Keyboard Shortcuts**: Not always supported, but if it is, pressing a specific key can replicate a click.

---

#### Final Thoughts

An **Image Button** offers a primarily graphical method of user interaction, with an optional label if you want partial text. By preserving separation of logic (M3L) and styling (GSS), you maintain flexibility, consistency, and accessibility—especially for purely icon-based UIs.

---

### Confirmation Button Widget

A **Confirmation Button** is used for **major or irreversible actions**, such as making a purchase or signing a contract. Unlike a standard button, it typically requires an **extra step** (like click-and-hold or swipe-to-confirm) so the user explicitly acknowledges the action.

#### Core Fields

| Field               | Description                                                                                                  | Example                                     |
|---------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `id`                | Unique identifier for referencing in **Pseudo** or logic (not used by GSS).                                 | `id = "purchase_btn"`                     |
| `label`             | Text displayed on the button face (e.g., "Confirm").                                                       | `label = "Confirm"`                       |
| `icon`              | (Optional) Path to an icon or image if the button uses an icon.                                             | `icon = "@Undline/assets/check.svg"`      |
| `action`            | A short descriptor for the button’s role or action.                                                         | `action = "confirm_purchase"`             |
| `target`            | Resource, Pseudo script, or API call location.                                                              | `target = "@Undline/api/checkout"`        |
| `tooltip`           | Text shown on hover/focus (if supported).                                                                   | `tooltip = "Click and Hold to Confirm"`   |
| `confirmation_mode` | Defines how the user must confirm (e.g. `click_and_hold`, `slide`, or other).                               | `confirmation_mode = "click_and_hold"`    |
| `hold_duration`     | If `confirmation_mode` = `click_and_hold`, the time in ms the user must hold before firing the event.       | `hold_duration = 2000`                      |
| `disabled`          | Disables interaction if `true`.                                                                             | `disabled = false`                         |
| `loading`           | Shows a loading state if `true`.                                                                            | `loading = false`                          |
| `keyboard_shortcut` | (Optional) Key combo to trigger the button (if supported).                                                  | `keyboard_shortcut = "ctrl+enter"`        |
| `order`             | Numeric ordering for keyboard/controller tab navigation. Defaults to auto if none given.                    | `order = 4`                                |
| `on_click`          | Specifies an array of event actions (intent, etc.).                                                         | `on_click = [{ intent = "finalize_deal" }]`|

> **Note**: If you want a simpler approach, consider a primary or secondary button. Confirmation Button is for big actions.

---

#### Example M3L Snippet

```toml
# Minimal M3L snippet for a Confirmation Button

[confirmation_button]
id = "purchase_btn"
label = "Buy Now"
action = "confirm_purchase"
target = "@Undline/api/checkout"
tooltip = "Click and hold 2s to confirm"
confirmation_mode = "click_and_hold"
hold_duration = 2000
order = 4

on_click = [
  { intent = "finalize_deal", target = "@Undline/api/checkout" }
]
```

**Explanation**:
- **id**: "purchase_btn" is for referencing in logic.
- **label**: "Buy Now" or "Confirm" is displayed.
- **confirmation_mode**: e.g. "click_and_hold" or "slide".
- **hold_duration**: If `confirmation_mode`= `click_and_hold`, the user must hold for 2s.
- **tooltip**: Nudges the user about the hold requirement.
- **on_click**: Ties into M3L event logic after confirmation.

---

#### GSS Example

```toml
[confirmation_button]
background-color = "#FFAA00"
color = "#000000"
border-radius = "6px"
border = "1px solid #FFA500"
padding = "12px 24px"
font-family = "Arial, sans-serif"
font-size = "1rem"
font-weight = "bold"

[confirmation_button.hover]
background-color = "#FF9900"

[confirmation_button.disabled]
background-color = "#dddddd"
color = "#999999"
cursor = "not-allowed"

[confirmation_button.loading]
content = "Processing..."
cursor = "wait"

[confirmation_button.shadow]
# Add a slightly stronger shadow for emphasis
value = [ "3px 3px 6px rgba(0,0,0,128)" ]

[confirmation_button.animation.hover]
type = "scale-up"
duration = "0.3s"
timing_function = "ease-in-out"

[confirmation_button.animation.click]
type = "slide-confirm"  # For a 'slide to confirm' effect.
duration = "1s"
timing_function = "ease-in"

[confirmation_button.animation.hold]
# Could define a radial fill or progress ring that completes in hold_duration ms
# This is up to the GSS engine's capabilities.
```

**Explanation**:
1. `[confirmation_button]`: A bright color (e.g. gold/orange) conveys importance.
2. `[confirmation_button.hover]`, `[confirmation_button.disabled]`, `[confirmation_button.loading]`: Each modifies visuals.
3. **Shadows**: Emphasize the significance of the action.
4. **Animations**:
   - `slide-confirm` is a hypothetical effect for swiping confirmation.
   - `hold` might visually show a timed progress if the user holds the button.

---

#### Advanced Considerations

1. **Confirmation Modes**: If `confirmation_mode = "slide"`, GSS can animate a slider the user drags. If `click_and_hold`, you might define a progress ring animation. Implementation details vary.
2. **Time & Safety**: Longer `hold_duration` (like 3000–5000 ms) if the action is extremely irreversible.
3. **Disabled & Loading**: If `disabled = true` or `loading = true`, interactions are limited or visually indicated.
4. **Keyboard Navigation**: `order` ensures your confirmation button has a consistent place in tabbing.
5. **Accessibility**: Provide `tooltip` or screenreader text. Confirm voice or keyboard input can also trigger the hold/slide logic.
6. **Integration**: `[confirmation_button]` can embed inside `[window]`, `[frame]`, `[card]`, etc.
7. **Parent Scoping**: If placed in a `card`, GSS can define `[card.confirmation_button]` for specialized looks.

---

#### Final Thoughts

A **Confirmation Button** enforces an *explicit* user action—such as a hold or slide—to prevent accidental clicks on critical steps. The M3L snippet sets up logic fields (`confirmation_mode`, `hold_duration`), while GSS handles the visual nuance (e.g., a progress ring or sliding track), ensuring a robust and user-friendly confirmation flow.

---

### Toggle Button Widget

A **Toggle Button** lets users switch between two states, such as **ON/OFF**, **Mute/Unmute**, or **Enable/Disable**. Rather than submitting an action once, the button retains and visually displays its current state.

#### Core Fields

| Field               | Description                                                                                                  | Example                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `id`                | Unique identifier for referencing in **Pseudo** or logic (not used by GSS).                                 | `id = "mute_toggle"`                    |
| `label_on`          | Text displayed when the toggle is in the "on" or "active" state.                                          | `label_on = "Unmuted"`                  |
| `label_off`         | Text displayed when the toggle is in the "off" or "inactive" state.                                       | `label_off = "Muted"`                   |
| `initial_state`     | The default state (`on` or `off`) if not otherwise set by logic.                                             | `initial_state = "off"`                 |
| `action_on`         | A short descriptor for the "on" action (e.g., unmute, enable).                                              | `action_on = "unmute_sound"`            |
| `action_off`        | A short descriptor for the "off" action (e.g., mute, disable).                                             | `action_off = "mute_sound"`             |
| `target`            | Resource, Pseudo script, or API call location for toggling on/off states.                                    | `target = "@Undline/api/sound_toggle"`  |
| `tooltip_on`        | (Optional) Hover/focus text when the toggle is `on`.                                                         | `tooltip_on = "Currently Unmuted"`       |
| `tooltip_off`       | (Optional) Hover/focus text when the toggle is `off`.                                                        | `tooltip_off = "Currently Muted"`        |
| `disabled`          | Disables interaction if `true`.                                                                              | `disabled = false`                        |
| `loading`           | Shows a loading state if toggling is in progress.                                                            | `loading = false`                         |
| `keyboard_shortcut` | (Optional) Key combo to toggle (if supported).                                                               | `keyboard_shortcut = "m"`               |
| `order`             | Numeric ordering for keyboard/controller tab navigation. Defaults to auto if none given.                     | `order = 5`                               |
| `on_toggle`         | Specifies an array of event actions for toggling. May pass a param indicating on/off.                        | `on_toggle = [{ intent = "toggle_sound" }]` |

> **Note**: Some devs prefer a single field `label` that changes dynamically. Others prefer separate `label_on` and `label_off` for clarity.

---

#### Example M3L Snippet

```toml
# Minimal M3L snippet for a Toggle Button widget

[toggle_button]
id = "mute_toggle"
label_on = "Unmute"
label_off = "Mute"
initial_state = "off"
action_on = "unmute_sound"
action_off = "mute_sound"
target = "@Undline/api/sound_toggle"
tooltip_on = "Currently Unmuted"
tooltip_off = "Currently Muted"
order = 5

on_toggle = [
  { intent = "toggle_sound", target = "@Undline/api/sound_toggle" }
]
```

**Explanation**:
- **id**: "mute_toggle" is used by logic or Pseudo.
- **label_on** / **label_off**: Text for each state.
- **initial_state**: By default, it starts in "off" (muted).
- **action_on**, **action_off**: Short descriptors for each toggle action.
- **tooltip_on**, **tooltip_off**: Optional hints to clarify the current state.
- **on_toggle**: Ties into M3L event logic (like toggling an API call). A param might be passed to differentiate on/off.

---

#### GSS Example

```toml
[toggle_button]
background-color = "#EEEEEE"
color = "#333333"
border-radius = "4px"
border = "1px solid #999999"
padding = "8px 16px"
font-family = "Arial, sans-serif"
font-size = "1rem"
cursor = "pointer"

# State: ON
[toggle_button.on]
background-color = "#00DD88"
color = "#FFFFFF"

# State: OFF
[toggle_button.off]
background-color = "#CC3333"
color = "#FFFFFF"

[toggle_button.hover]
background-color = "#DDDDDD"

[toggle_button.disabled]
background-color = "#eeeeee"
color = "#999999"
cursor = "not-allowed"

[toggle_button.loading]
content = "Switching..."
cursor = "wait"

[toggle_button.shadow]
value = [ "1px 1px 3px rgba(0,0,0,64)" ]

[toggle_button.animation.on]
# Suppose toggling ON has a quick fade-in
type = "fade-in"
duration = "0.3s"
timing_function = "ease"

[toggle_button.animation.off]
# Suppose toggling OFF has a quick fade-out
type = "fade-out"
duration = "0.3s"
timing_function = "ease"
```

**Explanation**:
1. `[toggle_button]`: Base style shared by both states.
2. `[toggle_button.on]` and `[toggle_button.off]` define distinctive looks (e.g., green for on, red for off). The engine picks which block applies based on the current toggle state.
3. Additional states like `[toggle_button.hover]`, `[toggle_button.disabled]`, `[toggle_button.loading]` remain consistent with other button types.
4. Animations can vary for switching ON vs. OFF.

---

#### Advanced Considerations

1. **State Changes**: The engine or Pseudo might store the toggle state. M3L’s `on_toggle` event can pass along `new_state` ("on" or "off").
2. **Labels & Tooltips**: GSS can show/hide `label_on` / `label_off` as needed, or even overlay icons.
3. **Disabled & Loading**: If `disabled = true` or `loading = true`, that might prevent toggling or show a wait cursor.
4. **Keyboard Navigation**: The `order` field ensures logical tabbing with other buttons.
5. **Parent Scoping**: If inside `[card]`, you can override `[toggle_button]` with `[card.toggle_button]` for a different look.
6. **Custom Shapes**: If you do a custom polygon or 3D shape, fields like `border-radius` might not apply.

---

#### Final Thoughts

A **Toggle Button** is ideal for two-state UI flows—like enabling/disabling features or muting/unmuting audio. M3L sets the fields (labels, actions, state), while GSS renders each state’s appearance (`on`, `off`, plus hover/disabled/loading). This maintains clarity between UI logic and design.

---

### Floating Action Button (FAB)

A **Floating Action Button** (FAB) is a **prominent, circular** button designed for a key action (e.g., “New Post,” “Compose,” or “Start Chat”). It often floats above other UI elements and can be draggable if desired.

#### Core Fields

| Field              | Description                                                                                       | Example                                   |
|--------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------|
| `id`               | Unique identifier for referencing in **Pseudo** or logic (not used by GSS).                      | `id = "fab_chat"`                       |
| `label`            | (Optional) Text label displayed near/under the FAB’s icon (if GSS chooses to show it).           | `label = "Chat"`                        |
| `icon`             | Path to an icon/image forming the main face of the FAB.                                          | `icon = "@Undline/assets/chat_icon.svg"`|
| `action`           | Short descriptor for the FAB’s primary role or action.                                           | `action = "new_chat"`                   |
| `target`           | Resource, Pseudo script, or API call location.                                                   | `target = "@Undline/api/start_chat"`    |
| `tooltip`          | Text shown on hover/focus (if supported).                                                        | `tooltip = "Start a New Chat"`          |
| `disabled`         | Disables interaction if `true`.                                                                   | `disabled = false`                        |
| `loading`          | Shows a loading state if `true`.                                                                  | `loading = false`                         |
| `draggable`        | Allows the FAB to be moved around the screen if `true`.                                          | `draggable = true`                       |
| `boundary`         | Defines how far the FAB can be dragged (top, bottom, left, right).                               | `boundary = { top = "0px", bottom = "0px", left = "0px", right = "0px" }` |
| `keyboard_shortcut`| (Optional) Key combo to trigger the FAB (if supported).                                          | `keyboard_shortcut = "ctrl+n"`          |
| `order`            | Numeric ordering for keyboard/controller tab navigation. Defaults to auto if none given.         | `order = 6`                              |
| `on_click`         | Specifies an array of event actions (intent, etc.).                                              | `on_click = [{ intent = "create_new_chat" }]` |

> **Note**: Typically a FAB is circular and stands out visually. GSS handles shape, size, and float layering.

---

#### Example M3L Snippet

```toml
# Minimal M3L snippet for a Floating Action Button

[fab_button]
id = "fab_chat"
label = "Chat"
icon = "@Undline/assets/chat_icon.svg"
action = "new_chat"
target = "@Undline/api/start_chat"
tooltip = "Start a New Chat"
draggable = true
boundary = { top = "0px", bottom = "0px", left = "0px", right = "0px" }
order = 6

on_click = [
  { intent = "create_new_chat", target = "@Undline/api/start_chat" }
]
```

**Explanation**:
- **id**: "fab_chat" for referencing in logic.
- **label**: (Optional) “Chat” if the GSS decides to show it under/next to the icon.
- **draggable**: `true` means the user can drag the FAB around.
- **boundary**: Restricts how far the FAB can move.
- **on_click**: Ties into M3L event logic.

---

#### GSS Example

```toml
[fab_button]
# Typically circular and floating above other elements
background-color = "#FF4081"
color = "#FFFFFF"
border-radius = "50%"
width = "56px"
height = "56px"
shadow = [ "2px 2px 6px rgba(0,0,0,128)" ]
cursor = "pointer"
position = { x = "calc(100% - 72px)", y = "calc(100% - 72px)" }

[fab_button.hover]
background-color = "#F50057"

[fab_button.disabled]
opacity = "0.6"
cursor = "not-allowed"

[fab_button.loading]
# Could overlay a spinner or make the icon partially transparent
opacity = "0.7"
cursor = "wait"

[fab_button.draggable]
# If draggable, you might define a 'grab' cursor on hover or logic for drag states
cursor = "grab"

[fab_button.animation.hover]
type = "scale-up"
duration = "0.3s"
timing_function = "ease-in-out"

[fab_button.animation.click]
type = "bounce"
duration = "0.4s"
timing_function = "ease"
```

**Explanation**:
1. `[fab_button]`: Typically circular, sized ~56px (common in mobile design), with a strong shadow.
2. `position = { x = "calc(100% - 72px)", y = "calc(100% - 72px)" }`: Example of anchoring near bottom-right corner. Real usage depends on your layout.
3. `[fab_button.draggable]`: GSS might show a `grab` cursor, though actual drag logic is engine- or JS-level.
4. Animations on hover or click for a satisfying user experience.

---

#### Advanced Considerations

1. **Drag Logic**: If `draggable = true`, M3L or your engine might handle the actual drag events. GSS just sets the visual style (like `cursor = "grab"`).
2. **Label Placement**: If `label` is provided, GSS can position text below or next to the icon. Sometimes it’s hidden until hover.
3. **Disabled & Loading**: Setting these fields changes the look accordingly (lower opacity, cursor changes, etc.).
4. **Keyboard Navigation**: The `order` field ensures it fits among other buttons in tab or arrow focus.
5. **Parent Scoping**: If inside `[window]` or `[frame]`, GSS can do `[window.fab_button]` for a unique style.
6. **Custom Shapes**: If you want a non-circular shape, define your own shape or 3D illusions. `border-radius` might be ignored in that case.

---

#### Final Thoughts

A **Floating Action Button** stands out for critical or central actions—commonly used in mobile or modern UIs. By storing shape, size, and float position in GSS while M3L handles logic fields (`label`, `draggable`, etc.), you maintain a clear separation of concerns and a smooth user experience.

---

### Header Widget

A **Header Widget** displays a **single heading** (e.g., H1–H6) to structure your content hierarchy. These headings mirror **HTML heading elements** (H1 through H6). Although H6 is less commonly used, it can be important in deeply nested sections.

---

## Why a Dedicated Header Widget?
- **Focus**: Instead of handling headings among various text types, the Header Widget emphasizes one heading level at a time.
- **Clarity**: Developers can quickly see which level they're using—H1 for main titles, down to H6 for deeper subheadings.
- **Customization**: GSS can style each heading level differently, ensuring consistent yet flexible typography.
- **Parity with HTML**: Aligns with standard HTML heading elements, making the system more intuitive.

---

## Heading Levels & Typical Usage
Below are common, unofficial conventions for each heading level in HTML:

| Heading | Common Usage (Unofficial but typical)                     |
| ------- | --------------------------------------------------------- |
| **H1**  | Main page or document title (often used once per page).   |
| **H2**  | Major section heading.                                    |
| **H3**  | Sub-section under H2.                                     |
| **H4**  | Sub-sub-section; used for further nested headings.        |
| **H5**  | Minor heading; rarely used unless deeper nesting needed.  |
| **H6**  | The smallest heading; typically used for very nested or nuanced headings.

---

## Core Fields

| Field      | Description                                                                                                                            | Example                                     |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `id`       | Unique identifier for referencing in logic (not used by GSS).                                                                         | `id = "main_title"`                       |
| `level`    | The heading level: `H1`, `H2`, `H3`, `H4`, `H5`, or `H6`.                                                                             | `level = "H2"`                            |
| `content`  | The text string or external reference. Typically direct text, but can reference a chain file.                                         | `content = "Welcome to My App"`           |
| `disabled` | (Optional) If `true`, heading might appear grayed out or ignore click events if it’s interactive.                                     | `disabled = false`                         |
| `order`    | (Optional) If the heading is interactive, numeric ordering for keyboard/controller tab navigation. If omitted, the heading is skipped in tab focus. | `order = 3`                       |
| `on_click` | (Optional) Array of event actions if the heading is clickable.                                                                        | `on_click = [{ intent = "scroll_to_top" }]` |

> **Note**: For multi-line or advanced formatting, consider sub-widgets or a broader text system.

**Important**: If `order` is **not** provided, the header does **not** receive a position in the focus cycle and is ignored when the user tabs through widgets.

---

## Example M3L Snippet

```toml
# Minimal M3L snippet for a Header Widget

[header]
id = "main_title"
level = "H2"
content = "Welcome to the Dashboard"
order = 1

on_click = [
  { intent = "scroll_to_top" }
]
```

**Explanation**:
- **id**: "main_title" for referencing in Pseudo or events.
- **level**: "H2" for a second-level heading.
- **content**: The actual heading text.
- **order**: Places the heading in tab focus if it’s clickable. If omitted, it won't appear in the focus cycle.
- **on_click**: If you want the heading to do something on click.

---

## GSS Example

```toml
[header.H1]
font-size = "2.25rem"
font-weight = "bold"
line-height = "1.2"
letter-spacing = "0.02em"

[header.H2]
font-size = "1.75rem"
font-weight = "bold"
line-height = "1.3"
letter-spacing = "0.01em"

[header.H3]
font-size = "1.5rem"
font-weight = "bold"

[header.H4]
font-size = "1.25rem"
font-weight = "bold"

[header.H5]
font-size = "1.1rem"
font-weight = "bold"

[header.H6]
font-size = "1rem"
font-weight = "bold"

[header.disabled]
opacity = "0.5"
cursor = "not-allowed"

[header.animation.hover]
type = "underline"
duration = "0.2s"

[header.animation.click]
type = "pulse"
```

**Explanation**:
1. **`[header.H1]`** through **`[header.H6]`**: Distinct style blocks for each heading level.
2. **`[header.disabled]`**: If heading is flagged as disabled.
3. **Animations**: If heading is interactive, define hover or click animations.

---

## Advanced Considerations
1. **Inline vs. Block**: Headings are typically block-level. Overriding display in GSS can make them inline if needed.
2. **Disabled / Loading**: If headings are not clickable, these states may not matter. But if used interactively, they can apply.
3. **Keyboard Navigation**: If your heading is interactive, `order` sets the focus order. **No `order` means no tab focus**.
4. **Integration with Markdown**: If a Markdown file has headings, a parser might dynamically create multiple `[header]` widgets.

---

## Final Thoughts

A **Header Widget** focuses on **one** heading element (`H1`–`H6`), offering clarity and modularity for top-level text structure. M3L sets the heading level and content, while GSS handles font size, weight, spacing, etc. This ensures a straightforward, consistent system for headings across your application.

---

### Paragraph Widget

A **Paragraph Widget** provides a block of text for articles, descriptions, or general body content. It’s designed as a separate widget from headings, ensuring clear separation of concerns in your layout.

---

## Why a Paragraph Widget?
- **Focus**: Instead of a multi-purpose text widget, this focuses on *paragraph content*. Complex features like lists, table data, or code blocks belong to other widgets.
- **Simplicity**: Enforces consistent structure and styling (e.g., line height, letter spacing) for normal text blocks.
- **Modularity**: Aligns with how we separated heading, button, etc.

---

## Core Fields

| Field        | Description                                                                                                     | Example                                      |
|--------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `id`         | Unique identifier for referencing in logic (not used by GSS).                                                   | `id = "intro_paragraph"`                   |
| `content`    | The main text string or reference to external chain file.                                                       | `content = "This is a paragraph..."`        |
| `alignment`  | (Optional) Text alignment (left, center, right, justify).                                                      | `alignment = "justify"`                    |
| `disabled`   | (Optional) If `true`, paragraph might appear grayed out or block interactions if it’s clickable.               | `disabled = false`                          |
| `order`      | (Optional) If the paragraph is interactive, numeric ordering for keyboard/controller tab navigation. If omitted, it’s skipped in tab focus. | `order = 2`  |
| `on_click`   | (Optional) Array of event actions if the paragraph is clickable.                                               | `on_click = [{ intent = "expand_paragraph" }]` |
| `line_spacing`  | (Optional) Adjusts line spacing for text.                                                                   | `line_spacing = "1.5"`                     |
| `letter_spacing`| (Optional) Adjusts spacing between letters.                                                                 | `letter_spacing = "0.01em"`                |

> **Note**: For multiple paragraphs, devs can either create multiple paragraph widgets or a single widget with an internal approach (like Markdown). If you want lists or code blocks, see dedicated widgets.

---

## Example M3L Snippet

```toml
[paragraph]
id = "intro_paragraph"
content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
alignment = "justify"
line_spacing = "1.6"
letter_spacing = "0.01em"
order = 2

on_click = [
  { intent = "expand_paragraph" }
]
```

**Explanation**:
- **id**: "intro_paragraph" for referencing in logic.
- **content**: The textual content.
- **alignment**: "justify" for an aligned block.
- **line_spacing** / **letter_spacing**: For better readability.
- **on_click**: If you want it to respond to user clicks (e.g., expanding or toggling something).
- **order**: Places it in tab order if you want it focusable.

---

## GSS Example

```toml
[paragraph]
font-family = "Arial, sans-serif"
font-size = "1rem"
color = "#333"
line-height = "1.5"
letter-spacing = "0.01em"

[paragraph.disabled]
opacity = "0.5"
cursor = "not-allowed"

[paragraph.animation.hover]
type = "highlight"
duration = "0.2s"

[paragraph.animation.click]
type = "pulse"
```

**Explanation**:
1. `[paragraph]`: Basic styling for paragraphs. Font family, size, color, line spacing.
2. `[paragraph.disabled]`: If the paragraph is flagged as disabled.
3. Animations: Possibly highlight on hover or pulse on click.

---

## Advanced Considerations

1. **Inline vs. Block**: Paragraphs are typically block-level. Overriding display in GSS can force them inline if needed.
2. **Disabled / Loading**: Usually paragraphs are not interactive, but if you do so, these states can matter.
3. **Keyboard Navigation**: If the paragraph is interactive, `order` sets focus order. No `order` => no tab focus.
4. **Large Text Blocks**: For bigger text sections or multi-paragraph content, consider multiple `[paragraph]` widgets or a **Markdown** widget.
5. **Integration**: `[frame.paragraph]` or `[window.paragraph]` scoping in GSS can create context-specific styles.

---

## Final Thoughts

A **Paragraph Widget** handles plain textual content in a simple, block-level format. By keeping headings, lists, code blocks, etc., in separate widgets, you maintain a modular approach. M3L sets paragraph logic (content, alignment, etc.), while GSS shapes its look (fonts, spacing, etc.). This fosters a clean, consistent typography system for your application.

---

### List Widget

A **List Widget** displays a collection of items in an **ordered** or **unordered** format. It’s a dedicated widget rather than mixing list logic into a generic text widget, ensuring clarity and modular design.

---

## Why a List Widget?
- **Focus**: Separates list behavior (markers, ordering, nesting) from other text types.
- **Customization**: GSS can define bullet styles for unordered lists, numbering or alpha markers for ordered lists, etc.
- **Consistency**: Aligns with how we handle heading, paragraph, and other specialized widgets.

---

## Core Fields

| Field         | Description                                                                      | Example                                     |
|---------------|----------------------------------------------------------------------------------|---------------------------------------------|
| `id`          | Unique identifier for referencing in logic (not used by GSS).                    | `id = "shopping_list"`                    |
| `list_style`  | Specifies `ordered` or `unordered`.                                              | `list_style = "ordered"`                  |
| `items`       | An array of text items for the list.                                             | `items = ["Milk", "Eggs", "Bread"]`      |
| `disabled`    | (Optional) If `true`, list might appear grayed out or ignore clicks if it’s interactive. | `disabled = false`                      |
| `selectable`  | (Optional) If `true`, items might be individually selectable or highlightable.   | `selectable = true`                        |
| `order`       | (Optional) If the list is interactive, numeric ordering for tab navigation. If omitted, it’s skipped in tab focus. | `order = 4`  |
| `on_item_click` | (Optional) Array of event actions when an item is clicked, often receiving an index or content param. | `on_item_click = [{ intent = "remove_item" }]` |

> **Note**: For nested lists, devs might create multiple `[list]` widgets or rely on a “list of lists.”

---

## Example M3L Snippet

```toml
[list]
id = "shopping_list"
list_style = "unordered"
items = [
  "Milk",
  "Eggs",
  "Bread"
]
selectable = true
order = 4

on_item_click = [
  { intent = "remove_item", param = "@index" } # hypothetical param to identify which was clicked
]
```

**Explanation**:
- **id**: For referencing in logic or Pseudo.
- **list_style**: "unordered" => bullet points.
- **items**: The text items in the list.
- **selectable**: Possibly highlights items on hover/click.
- **order**: If the entire list is considered a focusable element.
- **on_item_click**: Hypothetically fires an event for each item, passing `@index` or similar param.

---

## GSS Example

```toml
[list.unordered]
list-style-type = "disc"
padding-left = "1.5rem"

[list.ordered]
list-style-type = "decimal"
padding-left = "1.5rem"

[list.disabled]
opacity = "0.5"
cursor = "not-allowed"

[list.selectable]
# Could define hover or selected states for each item

[list.animation.hover]
type = "highlight"
duration = "0.2s"

[list.animation.click]
type = "pulse"
```

**Explanation**:
1. **`[list.unordered]`** and **`[list.ordered]`**: Distinct styles for bullet vs. numeric.
2. **`[list.disabled]`**: If the list is flagged as disabled.
3. **`[list.selectable]`**: If items can be hovered/clicked individually, GSS can style them.
4. Animations: e.g., highlight on hover.

---

## Advanced Considerations
1. **Nesting**: If you want sub-lists, consider multiple `[list]` widgets or a structured approach.
2. **Item Customization**: If items need more than plain text (like icons or multi-line paragraphs), you could embed child widgets.
3. **Keyboard Navigation**: If you want to individually tab through each item, you might create sub-widgets or treat each item as a separate focusable object.
4. **on_item_click**: Implementation details vary—some engines pass an index or content param to identify which item was clicked.
5. **Styling**: `[list.unordered]` might define bullet shapes, `[list.ordered]` might define decimal, alpha, or Roman markers.

---

## Final Thoughts

A **List Widget** provides an elegant, dedicated way to display items with ordering or bullet points. M3L defines the list style (ordered/unordered), plus each item’s text, while GSS handles bullet shapes, spacing, and interaction states. This keeps your app’s textual structure organized and consistent.

---

### Highlight Widget

A **Highlight Widget** emphasizes a specific word, phrase, or small block of text by applying a background color or other visual effect. It’s an alternative to mixing highlight logic into a larger text widget, ensuring a clean and modular approach.

---

## Why a Highlight Widget?
- **Modularity**: Instead of adding highlight fields to a broader text widget, we have a dedicated widget for emphasis.
- **Flexibility**: GSS can define custom background colors, animations, or transitions specific to highlights.
- **Interactive**: If needed, the highlight can be clickable or have tooltip interactions.

---

## Core Fields

| Field             | Description                                                                                                    | Example                                        |
|-------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `id`              | Unique identifier for referencing in logic (not used by GSS).                                                  | `id = "urgent_notice"`                       |
| `content`         | The text to be highlighted.                                                                                    | `content = "Important Note"`                 |
| `highlight_color` | (Optional) Color for the highlight background, e.g. `#FFFF00AA`.                                               | `highlight_color = "#FFD700"`                |
| `disabled`        | (Optional) If `true`, highlight might appear grayed out or ignore clicks if it’s interactive.                  | `disabled = false`                            |
| `order`           | (Optional) If the highlight is interactive, numeric ordering for tab navigation. If omitted, it’s skipped.     | `order = 5`                                   |
| `on_click`        | (Optional) Array of event actions if the highlight is clickable.                                               | `on_click = [{ intent = "show_tooltip" }]`   |

> **Note**: If you want multi-line or block-level highlight, consider a different approach or an embedded child widget.

---

## Example M3L Snippet

```toml
[highlight]
id = "urgent_notice"
content = "Server Maintenance at 2AM"
highlight_color = "#FFE600"
order = 5

on_click = [
  { intent = "show_tooltip", param = "Maintenance Info" }
]
```

**Explanation**:
- **id**: "urgent_notice" for referencing in logic.
- **content**: "Server Maintenance at 2AM" is the emphasized text.
- **highlight_color**: Yellow shade for the background.
- **order**: If you want it in the tab cycle.
- **on_click**: Could open a tooltip or show more details.

---

## GSS Example

```toml
[highlight]
background-color = "#FFFF00"  # fallback if highlight_color not set
color = "#000"
padding = "2px 4px"  # small padding to emphasize highlight

[highlight.disabled]
opacity = "0.5"
cursor = "not-allowed"

[highlight.animation.hover]
type = "glow"
duration = "0.3s"

[highlight.animation.click]
type = "pulse"
```

**Explanation**:
1. **[highlight]**: Basic styling. A default background color for highlight.
2. **[highlight.disabled]**: If set, it dims or disables.
3. **Animations**: Possibly glow on hover or pulse on click.

---

## Advanced Considerations
1. **Inline vs. Block**: Typically highlight is inline. If you want block-level highlighting for an entire paragraph, see a different approach or nested widgets.
2. **Disabled / Loading**: If not interactive, these states may not matter.
3. **Keyboard Navigation**: If interactive, `order` sets the tab focus. No `order` => no focus.
4. **Integration with Markdown**: A parser might convert `==some text==` or `::some text::` to a highlight widget.

---

## Final Thoughts

A **Highlight Widget** focuses on emphasizing a short inline text snippet, letting M3L define the content and highlight color while GSS styles the background and interactions. This separation promotes clarity and consistency across your UI.

---

### Hyperlink Widget

A **Hyperlink Widget** provides a dedicated mechanism for performing **intents** (e.g., opening a file, scrolling to a section, or scrolling to top) upon interacting with link text. The separation of **intent** (what to do) from **events** (how/when it’s triggered) ensures design flexibility.

---

## Why a Hyperlink Widget?

- **Focus**: Keeps link logic separate from paragraphs, headings, and other text widgets.
- **Customization**: GSS can define how events are triggered (click, double-click, hover, etc.).
- **Versatility**: The `intent` array can include actions like opening documents, scrolling to specific sections, or jumping to top.
- **Consistency**: Aligns with other specialized widgets (buttons, headings) while paralleling anchor elements in HTML.

---

## Core Fields

| Field      | Description                                                                                                                                           | Example                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `id`       | Unique identifier for referencing in logic (not used by GSS).                                                                                       | `id = "docs_link"`                                                |
| `text`     | The visible text (or label) for the hyperlink.                                                                                                        | `text = "View Documentation"`                                      |
| `order`    | (Optional) If the link is interactive, numeric ordering for keyboard/controller tab nav. If omitted, it’s skipped in tab focus.                     | `order = 2`                                                         |
| `intent`   | An array of objects describing the action(s) to be performed, e.g. `{ open = "@Undline/docs/readme.m3l" }`, `{ scroll_to_section = "#part2" }`, `{ scroll_to_top = true }`. | `intent = [{ open = "@Undline/docs/readme.m3l" }, { scroll_to_top = true }]`  |
| `disabled` | (Optional) If `true`, hyperlink might appear grayed out or ignore interactions if it’s intended to be inactive.                                      | `disabled = false`                                                  |
| `visited`  | (Optional) Whether the link is considered "visited" (some systems track this to style visited links).                                               | `visited = false`                                                   |
| `tooltip`  | (Optional) Hover/focus text to explain the link or show a preview.                                                                                    | `tooltip = "Opens the docs page."`                                 |

> **Note**: In M3L, `intent` declares the desired action(s). For instance, `scroll_to_section` can jump to a specific anchor, or `scroll_to_top` can jump to the top of the page. **How** those actions get triggered (on single-click, double-click, timed hover, etc.) is up to GSS or environment logic.

---

## Example M3L Snippet

```toml
[hyperlink]
id = "docs_link"
text = "View Documentation"
order = 2

intent = [
  { open = "@Undline/docs/readme.m3l" },
  { scroll_to_section = "#part2" },
  { scroll_to_top = true }
]
```

**Explanation**:
- **id**: "docs_link" for referencing in logic.
- **text**: The link’s label.
- **order**: If set, the link is included in tab focus. If omitted, it’s skipped.
- **intent**: Multiple objects. e.g., `open` for an external doc, `scroll_to_section` for an anchor, `scroll_to_top` to jump up.
- The environment or GSS decides how these are triggered.

---

## GSS Example

```toml
[hyperlink]
color = "#007BFF"
text-decoration = "underline"
cursor = "pointer"

[hyperlink.hover]
color = "#0056b3"

[hyperlink.visited]
color = "#800080" # typical visited link color

[hyperlink.disabled]
opacity = "0.5"
cursor = "not-allowed"

# Hypothetical approach to hooking user interactions for the multiple intents.
[hyperlink.intent.open]
on_click = 1       # single-click triggers open

[hyperlink.intent.scroll_to_section]
on_hover = 2      # if hovered 2 seconds, do scroll_to_section

[hyperlink.intent.scroll_to_top]
on_double_click = 1 # double-click triggers scroll_to_top

[hyperlink.animation.hover]
type = "fade-in"
duration = "0.2s"

[hyperlink.animation.loop]
# If you want a repeating effect
type = "glow"
repeat = "infinite"

[hyperlink.animation.click]
type = "pulse"
duration = "0.4s"
```

**Explanation**:
1. `[hyperlink]`: Default style for a normal link state (blue, underlined).
2. `[hyperlink.hover]`, `[hyperlink.visited]`, `[hyperlink.disabled]`: Distinct states.
3. `[hyperlink.intent.*]`: Each declared intent (e.g. `open`, `scroll_to_section`, `scroll_to_top`) can map to different user interactions: single-click, timed hover, double-click, etc.
4. **Animations**:
   - `fade-in` on hover,
   - Possibly `glow` in a loop,
   - `pulse` on click.

> This is conceptual. The GSS engine must support custom triggers, repeated animations, etc.

---

## Advanced Considerations
1. **Inline vs. Block**: Typically a link is inline. Overriding display in GSS can make it block-level.
2. **Disabled & Visited**: Some apps track visited states or disable a link if the user lacks permission.
3. **Keyboard Navigation**: If `order` is set, the link is focusable. Pressing Enter or Space might then fire one or more `intent` actions.
4. **Tooltips**: If `tooltip` is present, it can appear on hover/focus.
5. **Custom triggers**: Single-click, double-click, timed hover, or any advanced logic is declared in GSS `[hyperlink.intent.*]` blocks.
6. **Animations**: Repeated or indefinite animations (like glow) require GSS engine support.

---

## Final Thoughts

A **Hyperlink Widget** now supports multiple **intents**—including opening external docs, scrolling to specific sections, or jumping to top. M3L declares them, and GSS decides how/when they trigger. This approach fosters maximum design freedom and keeps link usage consistent and modular.

---

### Table Widget

A **Table Widget** displays structured data in rows and columns, supporting optional header rows, alignment options, custom styling for each cell, **and editing actions** (like adding/removing rows or columns). Rather than mixing table logic into a larger text or paragraph widget, this widget focuses on tabular content specifically.

---

## Why a Table Widget?
- **Focus**: Helps keep row/column logic separate from other text types.
- **Customization**: GSS can style headers, borders, alignment, zebra-striping, etc.
- **Editing**: By defining editable actions in M3L’s `intent` array, you allow GSS or environment logic to decide **how** users add rows/columns.
- **Clarity**: Each row and column is well-defined, and the M3L data structure remains straightforward.

---

## Core Fields

| Field         | Description                                                                                                                | Example                                                                 |
|---------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `id`          | Unique identifier for referencing in logic (not used by GSS).                                                              | `id = "scores_table"`                                                |
| `table_data`  | An array describing rows and their cells. Typically each row is `{ row = ["Cell1", "Cell2"] }`.                         | `table_data = [ { row = ["Name", "Score"] }, { row = ["Alice", "100"] } ]` |
| `has_header`  | (Optional) Indicates if the first row is treated as a header row.                                                           | `has_header = true`                                                    |
| `alignment`   | (Optional) Controls cell alignment (left, center, right). Could also be per-column.                                         | `alignment = "center"`                                                |
| `disabled`    | (Optional) If `true`, table might appear grayed out or ignore clicks if it’s interactive.                                   | `disabled = false`                                                     |
| `order`       | (Optional) If the table or its cells are interactive, numeric ordering for tab focus. If omitted, skip in tab nav.          | `order = 4`                                                            |
| `on_cell_click`| (Optional) Array of event actions if a user clicks a cell, with potential param indicating row/col.                        | `on_cell_click = [{ intent = "edit_cell", param = "@row,@col" }]`     |
| `intent`      | (Optional) Array of objects describing editing actions, e.g. `{ add_row = "@row" }` or `{ add_col = "@col" }`.           | `intent = [{ add_row = "@row" }, { add_col = "@col" }]`             |

> **Note**: For more advanced tables (nested widgets or multi-line cells), consider child widgets or custom logic. The new `intent` array can define additional behavior (like adding rows/columns), leaving GSS to decide **when** or **how** those are triggered.

---

## Example M3L Snippet

```toml
[table]
id = "scores_table"
table_data = [
  { row = ["Player", "Score"] },
  { row = ["Alice", "100"] },
  { row = ["Bob", "80"] }
]
has_header = true
alignment = "center"
order = 4

on_cell_click = [
  { intent = "edit_cell", param = "@row,@col" }
]

intent = [
  { add_row = "@row" },
  { add_col = "@col" }
]
```

**Explanation**:
- **id**: "scores_table" for referencing in logic.
- **table_data**: Each row is an object with a `row` array. The first row is used as the header.
- **has_header**: True => The first row is a header row.
- **alignment**: "center" aligns all cells.
- **on_cell_click**: If the user clicks a cell, it might fire an event with `@row,@col` placeholders for editing.
- **intent**: Additional editing actions, e.g. adding rows/columns. GSS can define **how** these happen (e.g., a plus button, context menu, etc.).
- **order**: If set, the table is focusable in tab navigation.

---

## GSS Example

```toml
[table]
border = "1px solid #333"
width = "auto"
font-size = "1rem"
color = "#333"

[table.header]
# Example styling for the header row
background-color = "#EEE"
font-weight = "bold"

[table.cell]
padding = "8px"

[table.cell.hover]
background-color = "#f0f0f0"

[table.disabled]
opacity = "0.5"
cursor = "not-allowed"

[table.animation.hover]
type = "highlight"
duration = "0.2s"

[table.animation.click]
type = "pulse"
duration = "0.3s"

# Hypothetical approach to hooking user interactions for the editing intent.
[table.intent.add_row]
on_click = 1        # single-click triggers add_row

[table.intent.add_col]
on_double_click = 1 # double-click triggers add_col
```

**Explanation**:
1. `[table]`: Basic table styling (border, width, color).
2. `[table.header]`: Special styles for the header row if `has_header = true`.
3. `[table.cell]`: Default cell styling (padding, etc.). `[table.cell.hover]` for a row or cell highlight.
4. `[table.disabled]`: If the table is flagged as disabled.
5. Animations: highlight on hover, pulse on click, etc.
6. `[table.intent.add_row]`, `[table.intent.add_col]`: Example of how each intent can be triggered differently.

---

## Advanced Considerations
1. **Row/Col Span**: If you need spanning cells, you might store extra info in `table_data` or use nested widgets.
2. **on_cell_click**: Implementation details can pass row/col indexes. If you want cell-by-cell focus, treat each cell as its own sub-widget.
3. **Alignment**: Per-column alignment could be stored in M3L or GSS. A simple approach is a single `alignment` property.
4. **Header**: If `has_header = true`, GSS or environment can apply `[table.header]` style to row 0.
5. **Keyboard Navigation**: If you want each cell to be focusable, consider sub-widgets or separate logic. If only the table as a whole is focusable, `order` suffices.
6. **Add/Remove Rows/Columns**: `intent` array can define new actions, leaving GSS to decide how to trigger them (click, double-click, context menu, etc.).

---

## Final Thoughts

A **Table Widget** now supports basic row/column additions via M3L `intent` (like `{ add_row = "@row" }` or `{ add_col = "@col" }`). The GSS or environment logic chooses how to trigger these (e.g., single-click, plus icon, context menu). This approach keeps your tabular data structure clear and your UI design flexible.

---

### Line Break Widget

A **Line Break Widget** provides a simple horizontal or vertical rule (divider) to separate sections of content. By creating a dedicated widget for breaks, you maintain a clean, modular approach, rather than mixing break logic into text or other widgets.

---

## Why a Line Break Widget?
- **Clarity**: Separates layout logic (where breaks occur) from text or paragraph widgets.
- **Customization**: GSS can define color, thickness, style (dotted, dashed, etc.), and orientation (horizontal or vertical).
- **Modularity**: Avoids mixing line breaks within text, ensuring each element has a clear, singular purpose.

---

## Core Fields

| Field          | Description                                                                                               | Example                               |
|----------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------|
| `id`           | Unique identifier for referencing in logic (not used by GSS).                                            | `id = "horizontal_divider"`         |
| `orientation`  | (Optional) Determines if the line break is `horizontal` or `vertical`. Default = `horizontal`.           | `orientation = "vertical"`           |
| `line_style`   | (Optional) Object defining style properties, e.g., color, thickness.                                     | `line_style = { color = "#333", thickness = "2px" }` |
| `disabled`     | (Optional) If `true`, might apply a dimmed or inactive style (in case the line break is interactive?).    | `disabled = false`                    |
| `order`        | (Optional) If you want to treat this break as a focusable element in tab navigation (rarely needed).     | `order = 10`                          |
| `on_click`     | (Optional) If you want an event on the line break (e.g., toggling orientation?), though unusual.         | `on_click = [{ intent = "toggle_orientation" }]` |

> **Note**: Typically, a line break is purely decorative and doesn’t need interactivity. However, you can define events if you want a special effect on click/hover.

---

## Example M3L Snippet

```toml
[line_break]
id = "horizontal_divider"
orientation = "horizontal"
line_style = { color = "#CCC", thickness = "2px" }

on_click = [
  { intent = "toggle_orientation" }
]
```

**Explanation**:
- **id**: Identifies the line break.
- **orientation**: Horizontal by default.
- **line_style**: A color of `#CCC` and thickness of `2px`.
- **on_click**: Potentially toggles orientation (just an example intent).

---

## GSS Example

```toml
[line_break]
margin = "1rem 0"  # some spacing above/below the line

[line_break.horizontal]
border-bottom = "2px solid #CCC"

[line_break.vertical]
border-left = "2px solid #CCC"

[line_break.disabled]
opacity = "0.5"
cursor = "not-allowed"

[line_break.animation.click]
type = "pulse"
duration = "0.3s"
```

**Explanation**:
1. `[line_break]`: Base style—margin can ensure spacing.
2. `[line_break.horizontal]`: A bottom border simulates a horizontal rule.
3. `[line_break.vertical]`: A left border simulates a vertical rule.
4. `[line_break.disabled]`: If we treat the line break as disabled, dim it.
5. **Animations**: Possibly pulse on click, though unusual for a divider.

---

## Advanced Considerations
1. **Vertical vs. Horizontal**: In most UIs, line breaks are horizontal. Vertical lines are occasionally used to separate columns.
2. **Styling**: Dotted or dashed lines can be achieved by customizing border style.
3. **Interactivity**: Rarely needed—use `[line_break]` purely decoratively unless you have special use cases.
4. **Accessibility**: Typically not focusable. If it conveys important structure, ensure screen readers can interpret it (e.g., role="separator").
5. **Dynamic or Collapsible**: Could be used to signal collapsible sections if GSS ties animations to an `intent`.

---

## Final Thoughts

A **Line Break Widget** is a simple but valuable part of UI layout, providing clear, consistent dividers. M3L sets orientation (`horizontal` or `vertical`) and optional styling parameters, while GSS handles the appearance and possible interactions (if any). This ensures a clean, modular approach to layout dividers.

---

### Block Quote Widget

A **Block Quote Widget** displays an excerpt or quotation in a visually distinct manner, often with additional metadata like a source or citation. By dedicating a widget to quotes, you keep quote logic and styling separate from standard paragraphs, ensuring a clear, modular design.

---

## Why a Block Quote Widget?
- **Focus**: Separates block quotes from generic paragraphs, offering unique styling and metadata handling.
- **Customization**: GSS can define distinctive formatting, such as background color, border, or stylized quotation marks.
- **Metadata**: M3L can store citation or source fields without mixing them into normal text.

---

## Core Fields

| Field         | Description                                                                                          | Example                                                      |
|---------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `id`          | Unique identifier for referencing in logic (not used by GSS).                                       | `id = "famous_quote"`                                      |
| `content`     | The quoted text.                                                                                    | `content = "Some inspiring words..."`                      |
| `source`      | (Optional) The author or source of the quote.                                                       | `source = "Albert Einstein"`                               |
| `citation`    | (Optional) Additional citation details (e.g., publication date, link).                              | `citation = "NY Times, 1947"`                               |
| `style`       | (Optional) A label if you have multiple quote styles.                                               | `style = "testimony"`                                      |
| `disabled`    | (Optional) If `true`, might appear grayed out or ignore interactions (if interactive).             | `disabled = false`                                          |
| `order`       | (Optional) If interactive, numeric ordering for keyboard/controller tab nav. If omitted, skip it.   | `order = 5`                                                 |
| `on_click`    | (Optional) Array of event actions if the quote is clicked (e.g., to expand more context).           | `on_click = [{ intent = "show_details" }]`                 |

> **Note**: Typically block quotes are static, but you can define events if you want expansions, toggles, or other behaviors.

---

## Example M3L Snippet

```toml
[blockquote]
id = "famous_quote"
content = "You never fail until you stop trying." # Example text
source = "Albert Einstein"
citation = "Interview, 1947"
order = 5

on_click = [
  { intent = "show_details" }
]
```

**Explanation**:
- **id**: "famous_quote" for referencing in logic.
- **content**: The actual quote.
- **source**: "Albert Einstein."
- **citation**: Additional info, e.g., "Interview, 1947."
- **order**: If you want it in tab navigation.
- **on_click**: Could show more context or open a link.

---

## GSS Example

```toml
[blockquote]
border-left = "4px solid #CCC"
padding = "1rem"
font-style = "italic"
background-color = "#f9f9f9"

[blockquote.source]
font-style = "normal"
font-weight = "bold"

[blockquote.citation]
font-size = "0.9rem"
color = "#666"

[blockquote.disabled]
opacity = "0.5"
cursor = "not-allowed"

[blockquote.animation.click]
type = "pulse"
duration = "0.3s"
```

**Explanation**:
1. `[blockquote]`: Applies a subtle left border, italic text, and light background.
2. `[blockquote.source]`: Distinct style for the source name.
3. `[blockquote.citation]`: Possibly smaller text for references.
4. `[blockquote.disabled]`: Dim or ignore clicks.
5. **Animation**: On click, a slight "pulse." Could tie in with `on_click` in M3L.

---

## Advanced Considerations
1. **Multi-Line Content**: If the quote is long, it may wrap. That’s normal for a block quote.
2. **Interactive Quotes**: Rare, but you could embed child widgets or toggles if you want expansions.
3. **Dynamic Sourcing**: In some apps, `source` might be a link or reference to a database (co-chain integration?).
4. **Keyboard Navigation**: If `order` is set, pressing Enter/Space could fire `on_click` events.
5. **Optional Title**: Some might want a `title` or `subject` field to label the quote.

---

## Final Thoughts

A **Block Quote Widget** keeps quoted text distinct and well-styled, letting M3L define the quote, source, or citation, while GSS handles aesthetic details—like a left border or italic font. If needed, you can add interaction or advanced co-chain references, but often a block quote is purely visual. This ensures a clean, expressive UI for quoting content throughout your app.

---

### Code Block Widget

A **Code Block Widget** displays code snippets in a stylized format and optionally supports copying code, syntax highlighting, and collapsible sections. By dedicating a widget to code display, you maintain clarity and separation from other text or paragraph widgets.

---

## Why a Code Block Widget?

- **Focus**: Keeps code display logic separate from normal text, ensuring consistent styling for code snippets.
- **Customization**: GSS can define syntax highlighting, background color, line numbers, and copy-button styling.
- **Interactive**: M3L can define an `intent` for copying or toggling collapsibility, leaving GSS to decide how/when it occurs.  

---

## Core Fields

| Field          | Description                                                                                      | Example                                            |
| -------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| `id`           | Unique identifier for referencing in logic (not used by GSS).                                    | `id = "example_code_snippet"`                      |
| `content`      | The code text to be displayed.                                                                   | `content = "function greet() { return 'Hello'; }"` |
| `language`     | (Optional) Language label for syntax highlighting. E.g., "Pseudo", "python". Defaults to "text". | `language = "Pseudo"`                              |
| `line_numbers` | (Optional) If `true`, shows line numbering.                                                      | `line_numbers = true`                              |
| `collapsible`  | (Optional) If `true`, code can be collapsed or expanded.                                         | `collapsible = false`                              |
| `order`        | (Optional) If interactive, numeric ordering for tab nav.                                         | `order = 5`                                        |
| `intent`       | (Optional) Array of objects describing actions, e.g. `{ copy_code = true }`.                     | `intent = [{ copy_code = true }]`                  |
| `disabled`     | (Optional) If `true`, code might appear grayed out or ignore events if it’s interactive.         | `disabled = false`                                 |

> **Note**: `language` helps GSS or environment code with syntax highlighting. `intent` can define copying or toggling actions.

---

## Example M3L Snippet

```toml
[code_block]
id = "example_code_snippet"
content = "function greet() {\n  return 'Hello';\n}\n"
language = "Pseudo"
order = 5

intent = [
  { copy_code = true },
  { toggle_section = "collapse" }
]
```

**Explanation**:

- **content**: A small Pseudo function.
- **language**: "Pseudo" (for potential syntax highlighting).
- **intent**: We have two possible actions—`copy_code` and `toggle_section`. GSS can define how/when these occur (clicking a copy button, etc.).
- **order**: If set, the code block can be part of tab focus.

---

## GSS Example

```toml
[code_block]
background-color = "#2d2d2d"
color = "#ccc"
font-family = "Consolas, 'Courier New', monospace"
font-size = "0.9rem"
padding = "1rem"
line_numbers = true
collapsible = true

[code_block.line_numbers]
# Hypothetical approach—some environment might inject line numbers
color = "#999"

[code_block.collapsible]
# If the code block is collapsible, maybe show a toggle icon or button
toggle.icon = "@assets/toggle.svg"

[code_block.disabled]
opacity = "0.5"
cursor = "not-allowed"

[code_block.intent.copy_code]
on_click = 1       # single-click triggers the copying

[code_block.intent.toggle_section]
on_click = 2      # double-click toggles collapse/expand

[code_block.animation.hover]
type = "highlight"
duration = "0.2s"

[code_block.animation.click]
type = "pulse"
duration = "0.3s"

```

**Explanation**:

1. **line_numbers**: `true` => GSS can show line numbering.
2. **collapsible**: `true` => code can be expanded/collapsed if GSS or environment wants that.
3. `[code_block]`: Basic styling: dark background, monospace font, etc.
4. `[code_block.line_numbers]`: Potential approach to styling line numbers.
5. `[code_block.collapsible]`: If collapsible, GSS can define or show a toggle icon.
6. `[code_block.disabled]`: Dim the code block if it’s inactive.
7. `[code_block.intent.copy_code]`: For single-click copying.
8. `[code_block.intent.toggle_section]`: For double-click toggling collapse/expand.
9. **Animations**: Possibly highlight on hover or pulse on click.

---

## Advanced Considerations

1. **Syntax Highlighting**: Could be done by GSS or environment logic referencing `language`. Some systems might do server-side highlighting, others client-side.
2. **Line Wrapping**: GSS or environment might define whether lines wrap or scroll horizontally.
3. **Collapsibility**: If `collapsible = true`, environment decides how to store collapsed state.
4. **Keyboard Navigation**: If `order` is set, pressing Enter or Space might copy code or toggle.
5. **Copy Behavior**: Usually you’d have a button in the top-right corner or a small icon. By separating `intent.copy_code` in M3L from the actual event in GSS, you remain flexible.

---

## Final Thoughts

A **Code Block Widget** is ideal for neatly displaying code snippets with optional highlighting, line numbers, collapsibility, and copy-to-clipboard functionality. M3L defines the code, language, and potential actions (`copy_code`, etc.), while GSS or environment logic handles styling, interactivity, and animations. This ensures consistency and clarity when sharing code throughout your application.

---

# CheckItem Widget

A **CheckItem Widget** represents an item with a checkbox (checked/unchecked) and a label, usually for to-do lists or tasks. In Markdown, this maps to GitHub-style task-list syntax, such as:

```
- [ ] Write documentation
- [x] Test code
```

When the Markdown parser sees lines like the above, it can produce one `[checkitem]` per line, setting `checked` to `false` or `true` accordingly.

---

## Why a CheckItem Widget?

- **Task-List Support**: Gives a proper UI element for tasks (checked/unchecked) in your M3 environment.
- **Interactivity**: If you want toggling or triggers when a box changes state, define an `intent` pointing to a script.
- **Styling**: GSS can define how checked items appear (e.g., line-through text, color changes) or whether disabled items can be interacted with.

---

## Core Fields

| Field      | Description                                                                                | Example                                                |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| `id`       | Unique identifier for referencing in logic (not used by GSS).                              | `id = "todo_item1"`                                    |
| `label`    | The text or label that appears beside the checkbox.                                        | `label = "Write documentation"`                        |
| `checked`  | Boolean indicating whether the item is checked (`true`) or unchecked (`false`).            | `checked = false`                                      |
| `disabled` | (Optional) If `true`, grays out or prevents toggling.                                      | `disabled = false`                                     |
| `order`    | (Optional) Numeric order in tab navigation. If omitted, the widget is skipped in tab flow. | `order = 2`                                            |
| `intent`   | (Optional) An array describing actions triggered when the checkbox toggles.                | `intent = [ { checked = "@UndChain/checkitem.psu" } ]` |

**Note**: If your system automatically calls a script when `checked` changes, you can set `intent = [ { checked = "@UndChain/script.psu" } ].` That script can handle further logic (e.g. marking the item complete in a database). Sadly this is not default behavior for markdown so there won't be anything called if you pull your source from a markdown file.

---

## Example M3L Snippet

```toml
[checkitem]
id = "todo_item1"
label = "Write documentation"
checked = false
order = 2
intent = [
  { checked = "@UndChain/checkitem.psu" }
]

[checkitem]
id = "todo_item2"
label = "Test code"
checked = true
# This intent is left blank showing that intents only trigger special events
```

**Explanation**:

- **`label`**: The text displayed beside the box.
- **`checked = false`** (for the first item) means it starts unchecked.
- **`intent`**: When the user toggles the checkbox, it triggers a script at `@UndChain/checkitem.psu` to handle updates or logic.
- The second `[checkitem]` shows a pre-checked item (`checked = true`).

---

## GSS Example

```toml
[checkitem]
font-family = "Arial, sans-serif"
font-size = "1rem"
padding = "0.25rem 0"

[checkitem.checked.true]
# If the widget is flagged as checked
text-decoration = "line-through"
color = "#aaa"

[checkitem.disabled]
opacity = "0.5"
cursor = "not-allowed"

[checkitem.animation.toggle]
type = "pulse"
duration = "0.3s"
```

**Key Points**:

1. **`[checkitem.checked.true]`**: If your engine notes `checked = true`, it could apply a line-through and lighter color.
2. **`[checkitem.disabled]`**: Dims or removes interactivity if `disabled = true`.
3. **Animations**: On toggle, you might pulse the text or show some highlight effect.

---

## Parsing from Markdown

For lines like:

```
- [ ] Write documentation
- [x] Test code
```

- The parser sees `- [ ]` or `- [x]`. If ` ` is empty, `checked = false`; if `x`, `checked = true`.
- The remainder is the label (e.g. `"Write documentation"`).
- Create a `[checkitem]` with those fields. If you want toggles to call a script, set `intent = [ { checked = "@UndChain/checkitem.psu" } ]`.

---

## Final Thoughts

A **CheckItem Widget** is ideal for to-do lists or simple tasks in Markdown. By mapping "- [ ]" or "- [x]" lines to `[checkitem]` objects, you get an interactive, stylable component. GSS can handle the checked vs. unchecked visuals, and if you’d like back-end updates or side effects, the `intent` array can point to a script that runs whenever the checkbox state changes.

---

# Markdown Widget

The **Markdown Widget** is responsible for loading `.md` content from a file or string and rendering it into the specialized M3L text widgets (e.g. `[header]`, `[paragraph]`, `[list]`, `[code_block]`, etc.). This allows developers to author content in Markdown while preserving the modular, structured approach of M3L.

---

## Core Fields

| Field       | Description                                                                                                                | Example                                             |
|-------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `id`        | A unique identifier for referencing in logic (not used by GSS).                                                            | `id = "release_notes"`                             |
| `source`    | The path to a `.md` file or inline content (e.g., `@Undline/docs/readme.md`).                                              | `source = "@Undline/docs/guide.md"`               |
| `lazy_load` | (Optional) If `true`, only loads/parses the visible portion of the Markdown, ideal for large files. Defaults to `false`.    | `lazy_load = true`                                  |
| `border`    | (Optional) A boolean indicating whether to display a border around the rendered Markdown area. Defaults to `false`.         | `border = true`                                     |
| `disabled`  | (Optional) If `true`, dims or prevents interaction (such as hyperlink clicks).                                              | `disabled = false`                                  |
| `order`     | (Optional) Numeric order for keyboard/controller tab navigation. If omitted, the widget (and its sub-widgets) are skipped.  | `order = 3`                                         |
| `on_error`  | (Optional) An array of actions to perform if parsing or loading fails (e.g. show an error message).                         | `on_error = [{ intent = "show_error" }]`          |

**Note**: Animations, loading indicators, and related UI/UX details are handled entirely by GSS. The M3L portion only defines structure and logic. For example, `lazy_load` determines whether content is fetched incrementally, but the specifics of displaying a spinner or fade-in effect are left to GSS.

---

## Example M3L Snippet

```toml
[markdown]
id = "release_notes"
source = "@Undline/docs/release_notes.md"
lazy_load = true
border = true
order = 3

on_error = [
  { intent = "show_error" }
]
```

**Explanation**:
- **`source`**: Points to the `.md` file containing content.
- **`lazy_load`**: If `true`, only the visible sections are fetched/parsed at a time.
- **`border`**: Instructs GSS to style a border around the Markdown container.
- **`order`**: The position for keyboard/controller focus.
- **`on_error`**: Fallback actions if the content fails to load or parse.

---

## GSS Integration

GSS can define how the Markdown widget appears in various states:

```toml
[markdown]
background-color = "#fff"
color = "#333"
padding = "1rem"

[markdown.border.true]
border = "1px solid #CCC"
padding = "1rem" # Extra padding when a border is shown

[markdown.disabled]
opacity = "0.5"
cursor = "not-allowed"

# Hypothetical styles to manage loading, loaded, and error states.
[markdown.loading]
background-image = "@assets/spinner.gif"
background-repeat = "no-repeat"
background-position = "center"

[markdown.loaded]
animation = "fade-in"
animation.duration = "0.5s"

[markdown.error]
animation = "shake"
animation.duration = "0.3s"
```

**Key Points**:
- **`border = true`** in M3L prompts `[markdown.border.true]` styling.
- **`[markdown.loading]`** or `[markdown.loaded]` can be applied dynamically by the engine if it tracks loading state.
- **`[markdown.error]`** can visually indicate an error, e.g. parse failure.

---

## Typical Rendering Flow
1. **Initialization**: M3L sees `source`, `lazy_load`, and `border` fields.
2. **Loading**: The system fetches `.md` content. If large and `lazy_load` is true, it only fetches/ parses portions as needed.
3. **Parsing**: Markdown is converted into sub-widgets (`[header]`, `[paragraph]`, `[list]`, etc.).
4. **Displaying**: Each sub-widget follows its own GSS styling. If GSS detects a loading or loaded state, it can apply transitions (e.g. spinners, fade-in).
5. **Error Handling**: If file retrieval or parsing fails, `on_error` triggers and GSS may display `[markdown.error]` styling.

---

## Why Use a Markdown Widget?
- **Separation of Content and Structure**: Authors can write `.md` files, while M3L automatically maps them to discrete widgets.
- **Consistency**: Headings, paragraphs, lists, and code blocks each follow their existing M3L/GSS rules.
- **Performance**: With `lazy_load`, large docs won’t slow down initial page load.
- **Flexibility**: GSS handles visual presentation and transitions, so developers can customize the look without altering M3L.

---

## Conclusion

The **Markdown Widget** allows you to load and parse Markdown content while preserving the structured, modular nature of M3L. By delegating animations and visual states entirely to GSS, it maintains a clean separation of concerns. Whether you’re showing short excerpts or entire documents, this approach helps keep your content easy to write and your UI easy to manage.

---

> **Stopping here to implement the parser and a simple engine based on these new formatting parameters. Will pick back up at this point!**

### **Text Box**
- **Description**: A text box allows users to input single-line text. This widget supports rich interactivity and validation through events and intents.
- **Use Cases**:
  - Collecting user input (e.g., usernames, emails).
  - Password entry with secure visibility controls.
  - Real-time validation (e.g., regex, min/max length).
  - Dynamic interactions (e.g., triggering co-chain requests).

---

#### **Core Fields**
| Field           | Description                                                                 | Example                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `label`         | A descriptive title or prompt for the text box. Rendered via GSS styling.  | `label = "Enter Username"`                                                                                                                  |
| `placeholder`   | Text displayed inside the box when it is empty.                            | `placeholder = "Enter your username"`                                                                                                       |
| `default_value` | Pre-fills the text box with initial data.                                   | `default_value = "JohnDoe123"`                                                                                                |
| `password`      | Masks the input text for secure password entry.                            | `password = true`                                                                                                                             |
| `integrated_button` | Adds an interactive button inside the text box (e.g., toggle password visibility). | `integrated_button = { icon = "@Undline/assets/show_icon.svg", action = "toggle_visibility" }`                                            |
| `mask_symbol`   | Allows customization of the masking symbol for password fields.            | `mask_symbol = "•" or `mask_symbol = "🔒"`                                                                                                |
| `autocomplete`  | Suggests previously entered values as the user types.                      | `autocomplete = true`                                                                                                                         |
| `spellcheck`    | Enables or disables spellchecking for the input field.                     | `spellcheck = true`                                                                                                                           |
| `read_only`     | Prevents the user from modifying the text box value.                       | `read_only = true`                                                                                                                            |
| `max_length`    | Limits the number of characters a user can enter.                          | `max_length = 100`                                                                                                                            |
| `min_length`    | Specifies the minimum number of characters required.                       | `min_length = 5`                                                                                                                              |
| `case_transform`| Automatically transforms the input (e.g., uppercase, lowercase).           | `case_transform = "uppercase"`                                                                                                              |
| `on_input`      | Triggers actions as the user types.                                         | `on_input = [{ validate = "regex", pattern = "^[a-zA-Z0-9_]+$" }, { after_idle = "2s", intent = "check_availability", target = "UndChain://UnaS/namecheck" }]` |
| `on_exit`       | Triggers actions when the user leaves the text box.                        | `on_exit = [{ validate = "regex", pattern = "^[^@\s]+@[^@\s]+\.[^@\s]+$" }]`                                                        |
| `on_enter`      | Fires when the text box gains focus.                                        | `on_enter = [{ show_help = "Enter a unique username." }]`                                                                                   |
| `on_next`       | Handles navigation to the next widget in the flow.                         | `on_next = "password_field"`                                                                                                                |
| `on_submit`     | Fires when the user confirms input (e.g., pressing Enter).                 | `on_submit = [{ validate = "min_length", value = 3 }, { intent = "search", target = "SQeeL://Auction_House/search" }]`                  |
| `on_error`      | Triggers actions when an error specific to the widget occurs.              | `on_error = [{ display = "tooltip", message = "This field is required." }]`                                                               |

---

#### **Core Styling Parameters**
| Parameter           | Description                                             | Example                                        |
|---------------------|---------------------------------------------------------|------------------------------------------------|
| `font-family`       | Defines the font of the text inside the box.            | `font-family = "Arial, sans-serif"`          |
| `font-size`         | Sets the size of the text.                              | `font-size = "1rem"`                         |
| `color`             | Sets the text color.                                    | `color = "#333"`                              |
| `background-color`  | Defines the background color of the text box.           | `background-color = "#fff"`                  |
| `border`            | Specifies the border style, width, and color.           | `border = "1px solid #ccc"`                  |
| `border-radius`     | Rounds the corners of the text box.                     | `border-radius = "5px"`                      |
| `padding`           | Defines the padding inside the text box.                | `padding = "0.5rem"`                         |
| `placeholder.color` | Sets the color of the placeholder text.                 | `placeholder.color = "#aaa"`                 |
| `mask_symbol.style` | Defines the styling for the mask symbol in password fields. | `mask_symbol.style = "font-size: 1.2rem; color: #444;"`             |

---

#### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "text_box"
label = "Password"
placeholder = "Enter your password"
default_value = ""
password = true
mask_symbol = "🔒"
autocomplete = true
spellcheck = false
read_only = false
max_length = 20
case_transform = "uppercase"
integrated_button = { icon = "@Undline/assets/show_icon.svg", action = "toggle_visibility" }
on_input = [
    { validate = "min_length", value = 8, error_message = "Password must be at least 8 characters." },
    { validate = "regex", pattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error_message = "Password must include letters and numbers." }
]
on_exit = [
    { validate = "regex", pattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error_message = "Password must include letters and numbers." }
]
on_submit = [
    { intent = "submit_password", target = "UndChain://Account/Create" }
]
on_error = [
    { display = "tooltip", message = "Password does not meet requirements." }
]
```

---

#### **Example GSS Implementation**
```toml
[text_box]
font-family = "Arial, sans-serif"
border = "1px solid #ccc"
border-radius = "5px"
padding = "0.5rem"
color = "#333"
background-color = "#fff"

[text_box.label]
font-size = "1rem"
color = "#444"
padding-bottom = "0.25rem"

[text_box.placeholder]
color = "#aaa"
font-style = "italic"

[text_box.valid]
border-color = "#00FF00"

[text_box.invalid]
border-color = "#FF0000"

[text_box.waiting]
background-image = "loading_spinner.gif"

[text_box.integrated_button]
position = "absolute"
right = "1rem"
top = "50%"
transform = "translateY(-50%)"
width = "1.5rem"
height = "1.5rem"
cursor = "pointer"

[text_box.mask_symbol]
font-size = "1.2rem"
color = "#444"

[text_box.error.tooltip]
background-color = "#FFDDDD"
color = "#FF0000"
padding = "0.25rem"
border-radius = "3px"
```

---

### **Key Features**
- **Rich Event Handling**: Leverage `on_input`, `on_exit`, `on_enter`, `on_next`, `on_submit` and `on_error` for dynamic interactions and seamless user experiences.
- **Password Handling**: Use the `password` field for secure input, the `mask_symbol` for custom masking, and integrated buttons for toggling visibility.
- **Validation Options**: Support for client-side and co-chain validation ensures flexibility and scalability.
- **Dynamic Feedback**: Integrate GSS rules for valid, invalid, and waiting states to provide real-time feedback.
- **Accessibility**: Use ARIA roles and descriptions to enhance usability for assistive technologies.

---

### **Text Area**
- **Description**: A text area allows users to input multi-line text, making it ideal for feedback, comments, or larger bodies of text. This widget supports dynamic interactivity, validation, and user-friendly features like auto-expansion.
- **Use Cases**:
  - Collecting detailed user feedback or comments.
  - Enabling users to write multi-line notes or descriptions.
  - Integrating dynamic features like autosave or live character count.

---

#### **Core Fields**
| **Field**           | **Description**                                                                 | **Example**                                                                                                                         |
|---------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `label`             | A descriptive title or prompt for the text area. Rendered via GSS styling.      | `label = "Write Your Feedback"`                                                                                                   |
| `placeholder`       | Text displayed when the area is empty.                                          | `placeholder = "Enter your feedback here..."`                                                                                     |
| `default_value`     | Pre-fills the text area with initial data.                                       | `default_value = "I love M3L and GSS!"`                                                                                            |
| `max_length`        | Limits the total number of characters allowed.                                  | `max_length = 500`                                                                                                                 |
| `min_length`        | Specifies the minimum number of characters required.                           | `min_length = 10`                                                                                                                  |
| `min_lines`         | Sets the minimum number of lines the text area displays initially.             | `min_lines = 1`                                                                                                                    |
| `resizable`         | Allows users to resize the text area.                                           | `resizable = true`                                                                                                                 |
| `scrollable`        | Adds scrollbars if the content overflows.                                       | `scrollable = true`                                                                                                                |
| `collapsed`         | Specifies whether the text area starts collapsed.                              | `collapsed = true`                                                                                                                 |
| `collapsed_lines`   | Defines the number of lines shown when collapsed.                               | `collapsed_lines = 3`                                                                                                              |
| `max_lines`         | Sets the maximum number of lines the text area can grow to when expanded.      | `max_lines = 10`                                                                                                                   |
| `spellcheck`        | Enables or disables spellchecking.                                              | `spellcheck = true`                                                                                                                |
| `read_only`         | Prevents the user from modifying the content.                                   | `read_only = true`                                                                                                                 |
| `case_transform`    | Automatically transforms input to uppercase, lowercase, or capitalize each word.| `case_transform = "capitalize"`                                                                                                    |
| `character_count`   | Displays a live character count below the text area.                           | `character_count = true`                                                                                                           |
| `autosave`          | Automatically saves content after a set interval.                              | `autosave = { interval = "5s", target = "SQeeL://Notes/Save" }`                                                                  |
| `undo_redo`         | Enables undo and redo functionality for the text area.                         | `undo_redo = true`                                                                                                                 |
| `on_input`          | Triggers actions as the user types.                                             | `on_input = [{ validate = "regex", pattern = "^[a-zA-Z0-9\s]+$" }]`                                                              |
| `on_submit`         | Fires when the user confirms input (e.g., pressing Enter with `submit = true`). | `on_submit = [{ intent = "submit_comment", target = "SQeeL://Comments/Submit" }]`                                                  |
| `on_error`          | Triggers actions when an error specific to the widget occurs.                  | `on_error = [{ display = "tooltip", message = "Comment must be at least 10 characters." }]`                                        |
| `onscreen_keyboard` | Activates an on-screen keyboard when the text area gains focus.                | `onscreen_keyboard = true`                                                                                                          |
| `on_enter`          | Triggers actions when the text area gains focus.                              | `on_enter = [{ highlight_border = true }]`                                                                                          |
| `on_exit`           | Fires actions when the text area loses focus.                                 | `on_exit = [{ autosave = true }]`                                                                                                   |
| `on_highlight`      | Detects when text within the area is highlighted and triggers an action.       | `on_highlight = [{ show_menu = "mini-menu" }]`                                                                                     |
| `on_next`           | Handles navigation to the next widget in the flow (e.g., via Tab key).         | `on_next = "next_widget_id"`                                                                                                       |

---

#### **Core Styling Parameters**
| **Parameter**          | **Description**                                              | **Example**                                    |
|------------------------|-------------------------------------------------------------|-----------------------------------------------|
| `font-family`          | Defines the font of the text inside the area.               | `font-family = "Verdana, sans-serif"`        |
| `font-size`            | Sets the size of the text.                                  | `font-size = "1rem"`                         |
| `font-color`           | Sets the font color of the text inside the area.            | `font-color = "#333"`                        |
| `background-color`     | Sets the background color of the area.                      | `background-color = "#fff"`                  |
| `border`               | Specifies the border style, width, and color.               | `border = "1px solid #ddd"`                  |
| `border-radius`        | Rounds the corners of the text area.                        | `border-radius = "8px"`                      |
| `padding`              | Sets the padding inside the area.                           | `padding = "1rem"`                           |
| `placeholder.color`    | Sets the color of the placeholder text.                     | `placeholder.color = "#aaa"`                 |
| `scrollbar.color`      | Sets the color of the scrollbar for scrollable areas.       | `scrollbar.color = "#ccc"`                   |
| `resize.handle.style`  | Styles the resize handle when `resizable = true`.           | `resize.handle.style = "width: 8px; color: #444;"` |
| `collapsed.height`     | Sets the height of the collapsed text area.                 | `collapsed.height = "3rem"`                  |
| `expanded.height`      | Sets the height of the expanded text area.                  | `expanded.height = "10rem"`                  |
| `character_count.style`| Styles the character count displayed below the text area.   | `character_count.style = "font-size: 0.9rem; color: #666;"` |
| `touch.focus_indicator`| Sets styling for when the text area is focused on touch devices. | `touch.focus_indicator = "border: 2px solid #007BFF;"` |

---

#### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "text_area"
label = "Write Your Feedback"
placeholder = "Enter your feedback here..."
default_value = ""
max_length = 500
min_length = 10
min_lines = 1
resizable = true
scrollable = true
collapsed = true
collapsed_lines = 3
max_lines = 10
spellcheck = true
character_count = true
autosave = { interval = "5s", target = "SQeeL://Feedback/Save" }
onscreen_keyboard = true
on_input = [
    { validate = "min_length", value = 10, error_message = "Feedback must be at least 10 characters." },
    { validate = "regex", pattern = "^[a-zA-Z0-9\s.,!?]+$", error_message = "Only alphanumeric characters, spaces, and punctuation are allowed." }
]
on_enter = [
    { highlight_border = true }
]
on_exit = [
    { autosave = true }
]
on_highlight = [
    { show_menu = "mini-menu" }
]
on_next = "next_widget_id"
on_submit = [
    { intent = "submit_feedback", target = "SQeeL://Feedback/Submit" }
]
on_error = [
    { display = "tooltip", message = "Feedback submission failed. Try again." }
]
```

---

#### **Example GSS Implementation**
```toml
[text_area]
font-family = "Verdana, sans-serif"
border = "1px solid #ddd"
border-radius = "8px"
padding = "1rem"
font-color = "#333"
background-color = "#fff"

[text_area.label]
font-size = "1rem"
color = "#444"
padding-bottom = "0.5rem"

[text_area.placeholder]
color = "#aaa"
font-style = "italic"

[text_area.character_count]
font-size = "0.9rem"
color = "#666"
margin-top = "0.25rem"

[text_area.valid]
border-color = "#00FF00"

[text_area.invalid]
border-color = "#FF0000"

[text_area.scrollbar]
color = "#ccc"

[text_area.resize.handle]
width = "8px"
color = "#444"

[text_area.collapsed]
height = "3rem"

[text_area.expanded]
height = "10rem"

[text_area.touch.focus_indicator]
border = "2px solid #007BFF"
background-color = "#f0f8ff"
```

---

### **Key Features**
- **Rich Event Handling**: Leverage `on_input`, `on_submit`, `on_error`, `on_enter`, `on_exit`, `on_highlight`, and `on_next` for dynamic interactions and seamless user experiences.
- **Collapsible Design**: Use the `collapsed` parameter to save space while still allowing expandable text entry.
- **Dynamic Feedback**: Integrate GSS rules for valid, invalid, and waiting states to provide real-time feedback.
- **Autosave and Undo/Redo**: Automatically save progress and allow users to undo/redo changes for better usability.
- **Accessibility**: Use ARIA roles and descriptions to enhance usability for assistive technologies.
- **Touch Optimization**: Parameters like `onscreen_keyboard` ensure smooth interaction on touch devices.

---

#### **Notes**
- **Width Behavior**: The width of the text area is defined by the total width of the widget's containing element.
- **Height Behavior**: If `min_lines` and `max_lines` are not defined, the height of the text area defaults to the height of the containing widget.

---

### **Checkbox Widget**

Checkboxes are versatile widgets for binary or ternary selections (checked, unchecked, and indeterminate). They support custom styling, animations, and advanced interactions for hierarchical structures (parent-child relationships).

---

### **Core Features**
1. **Customizable Check Style**:
   - GSS developers can define the appearance of the checkmark (e.g., ✔, X, custom icons, or even animations).
   - Option to use images or SVGs for the checkmark.

2. **State Management**:
   - **Checked**: Indicates the checkbox is selected.
   - **Unchecked**: Indicates the checkbox is unselected.
   - **Indeterminate**: Used for parent-child relationships when only some child checkboxes are selected.

3. **Keyboard Navigation**:
   - By default, the `spacebar` toggles the checkbox state, but GSS developers can override this behavior.

4. **Interactive Events**:
   - Supports events like `on_click`, `on_hover`, and `on_change`.

5. **Accessibility**:
   - Labels for screen readers (e.g., `aria-label` equivalent).
   - Fully operable with keyboard input.

---

### **Proposed Fields**
| **Field**       | **Description**                                                             | **Example**                              |
|-----------------|-----------------------------------------------------------------------------|------------------------------------------|
| `label`         | Text displayed next to the checkbox.                                        | `label = "Subscribe to newsletter"`      |
| `state`         | Current state of the checkbox (`checked`, `unchecked`, `indeterminate`).    | `state = "checked"`                      |
| `group`         | Groups multiple checkboxes for logical association.                        | `group = "preferences"`                  |
| `animations`    | Animations for state transitions (check/uncheck).                          | `animations = { check = "bounce", uncheck = "fade-out" }` |
| `tooltip`       | Tooltip displayed on hover.                                                | `tooltip = "Click to subscribe"`         |
| `disabled`      | Disables the checkbox, preventing interaction.                             | `disabled = true`                        |

---

### **GSS Styling Parameters**
| **Parameter**        | **Description**                                                      | **Example**                              |
|----------------------|----------------------------------------------------------------------|------------------------------------------|
| `font-family`        | Defines the font for the checkbox label.                            | `font-family = "Arial, sans-serif"`      |
| `font-size`          | Defines the size of the label text.                                 | `font-size = "1rem"`                     |
| `font-color`         | Color of the label text.                                            | `font-color = "#333"`                    |
| `checkmark`          | Defines the style of the checkmark (e.g., ✔, X, image).             | `checkmark = "✔"`                        |
| `checkmark.color`    | Color of the checkmark.                                             | `checkmark.color = "#007BFF"`            |
| `checkmark.size`     | Size of the checkmark relative to the box.                          | `checkmark.size = "80%"`                 |
| `box.size`           | Size of the checkbox itself.                                        | `box.size = "20px"`                      |
| `box.border`         | Border style of the checkbox.                                       | `box.border = "1px solid #333"`          |
| `box.background`     | Background color of the checkbox when unchecked.                   | `box.background = "#FFF"`                |
| `box.hover.background` | Background color of the checkbox on hover.                        | `box.hover.background = "#EEE"`          |
| `box.indeterminate`  | Styling for the indeterminate state (e.g., dash or icon).           | `box.indeterminate = "-"`                |
| `animations.check`   | Animation applied when the checkbox is checked.                    | `animations.check = "bounce"`            |
| `animations.uncheck` | Animation applied when the checkbox is unchecked.                  | `animations.uncheck = "fade-out"`        |

---

### **Example M3L Implementation**
#### **Parent-Child Group Example**
```toml
[[layout.container.content]]
id = "parent-checkbox"
type = "checkbox"
label = "All notifications"
state = "indeterminate"
children = [
    {
        id = "child-email",
        type = "checkbox",
        label = "Email notifications",
        state = "checked"
    },
    {
        id = "child-push",
        type = "checkbox",
        label = "Push notifications",
        state = "unchecked"
    }
]
```

---

### **Example GSS Implementation**
```toml
[checkbox]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"
box.size = "20px"
box.border = "1px solid #333"
box.background = "#FFF"
box.hover.background = "#EEE"

[checkbox.checkmark]
content = "✔"
color = "#007BFF"
size = "80%"

[checkbox.indeterminate]
content = "-"
color = "#FFA500"

[checkbox.animations]
check = "bounce"
uncheck = "fade-out"
```

---

### **Advanced Considerations**
1. **Parent-Child Relationships**:
   - Parent checkboxes automatically toggle all child checkboxes.
   - Indeterminate state updates dynamically based on child selections.

2. **Keyboard Navigation**:
   - By default, `spacebar` toggles the checkbox state. GSS developers can redefine this behavior for custom accessibility setups.

3. **Future Node Animation Placeholder**:
   - Parallel animations could enable dynamic effects (e.g., glow and bounce simultaneously).
   - **Example Hypothetical**:
     ```toml
     [checkbox.animations.parallel]
     nodes = [
         { type = "glow", color = "#007BFF", duration = "0.3s" },
         { type = "bounce", duration = "0.5s" }
     ]
     ```

---

### **Conclusion**
Checkboxes provide a flexible solution for binary and ternary selection scenarios. By supporting advanced features like animations, parent-child relationships, and customizable styling, they can adapt to various application needs. Future enhancements, such as node-based animations, promise even greater creative possibilities for GSS developers.

---

### **Radio Button Widget**

Radio buttons are versatile widgets that allow users to select a single option from multiple choices within a group. They share many similarities with checkboxes but are mutually exclusive within their group.

---

### **Core Features**
1. **Single Selection Per Group**:
   - Radio buttons within the same group allow only one selection at a time.

2. **Customizable Selection Style**:
   - GSS developers can define the appearance of the selection indicator (e.g., filled circle, checkmark, custom SVG).

3. **Keyboard Navigation**:
   - By default, `arrow keys` navigate between options, and `spacebar` selects an option.

4. **State Management**:
   - Tracks the currently selected option within a group.

5. **Interactive Events**:
   - Supports events like `on_click`, `on_hover`, `on_change`, `on_enter`, and `on_exit`.

6. **Accessibility**:
   - Labels for screen readers (e.g., `aria-label` equivalent).
   - Fully operable with keyboard input.

---

### **Proposed Fields**
| **Field**       | **Description**                                                | **Example**                              |
|-----------------|----------------------------------------------------------------|------------------------------------------|
| `label`         | Text displayed next to the radio button.                       | `label = "Option 1"`                     |
| `state`         | Current state of the radio button (`selected`, `unselected`).  | `state = "selected"`                     |
| `group`         | Defines the group the radio button belongs to.                | `group = "choices"`                      |
| `tooltip`       | Tooltip displayed on hover.                                   | `tooltip = "Select this option"`         |
| `disabled`      | Disables the radio button, preventing interaction.            | `disabled = true`                        |
| `animations`    | Animations for state transitions (select/unselect).           | `animations = { select = "pulse", unselect = "fade-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**          | **Description**                                                    | **Example**                              |
|------------------------|--------------------------------------------------------------------|------------------------------------------|
| `font-family`          | Defines the font for the radio button label.                      | `font-family = "Arial, sans-serif"`      |
| `font-size`            | Defines the size of the label text.                               | `font-size = "1rem"`                     |
| `font-color`           | Color of the label text.                                          | `font-color = "#333"`                    |
| `indicator`            | Defines the style of the selection indicator.                    | `indicator = "circle"`                   |
| `indicator.color`      | Color of the selection indicator.                                | `indicator.color = "#007BFF"`            |
| `indicator.size`       | Size of the indicator relative to the radio button.              | `indicator.size = "80%"`                 |
| `indicator.svg`        | Path to a custom SVG for the selection indicator.                | `indicator.svg = "@assets/selector.svg"` |
| `box.size`             | Size of the radio button itself.                                 | `box.size = "20px"`                      |
| `box.border`           | Border style of the radio button.                                | `box.border = "1px solid #333"`          |
| `box.background`       | Background color of the radio button when unselected.            | `box.background = "#FFF"`                |
| `box.hover.background` | Background color of the radio button on hover.                   | `box.hover.background = "#EEE"`          |
| `animations.select`    | Animation applied when the radio button is selected.             | `animations.select = "pulse"`            |
| `animations.unselect`  | Animation applied when the radio button is unselected.           | `animations.unselect = "fade-out"`       |
| `animations.enter`     | Animation triggered when the radio button gains focus.           | `animations.enter = "glow"`              |
| `animations.exit`      | Animation triggered when the radio button loses focus.           | `animations.exit = "fade-out"`           |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "radio_button"
group = "choices"
children = [
    {
        label = "Option 1",
        state = "selected",
        tooltip = "Select Option 1",
        animations = { select = "pulse", unselect = "fade-out", enter = "glow", exit = "fade-out" }
    },
    {
        label = "Option 2",
        state = "unselected",
        tooltip = "Select Option 2",
        animations = { select = "pulse", unselect = "fade-out", enter = "glow", exit = "fade-out" }
    },
    {
        label = "Option 3",
        state = "unselected",
        tooltip = "Select Option 3",
        animations = { select = "pulse", unselect = "fade-out", enter = "glow", exit = "fade-out" }
    }
]
```

---

### **Example GSS Implementation**
```toml
[radio_button]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"
box.size = "20px"
box.border = "1px solid #333"
box.background = "#FFF"
box.hover.background = "#EEE"

[radio_button.indicator]
style = "circle"
color = "#007BFF"
size = "80%"
svg = "@assets/selector.svg"

[radio_button.animations]
select = "pulse"
unselect = "fade-out"
enter = "glow"
exit = "fade-out"
```

---

### **Conclusion**
Radio buttons provide an intuitive solution for single-selection scenarios. With features like animations, custom indicators, and advanced accessibility options, they offer a highly customizable and interactive user experience.

---

### **Navigation Box Widget**

The Navigation Box Widget provides an intuitive and customizable interface for displaying breadcrumbs, helping users navigate hierarchical structures such as file systems, web directories, or dynamic folder paths.

---

### **Core Features**

1. **Breadcrumb Display**:

   - Dynamically generate breadcrumbs based on the current navigation path.
   - Each breadcrumb is customizable to be interactive, static, or styled for visual emphasis.

2. **Custom Separator Support**:

   - Allows designers to specify custom separators (e.g., `/`, `>`, `|`, icons, or SVGs).
   - Default separator: `/`.

3. **Truncation and Overflow Handling**:

   - Automatically truncates paths that exceed the character limit of the navigation bar.
   - Supports scrolling or a special "more" SVG/icon to indicate hidden paths.
   - Optional animation for truncation (e.g., sliding folders into the "more" area).

4. **Dynamic Data Integration**:

   - Supports fuzzy finding for user input when typing a path.
   - Dynamically updates breadcrumbs based on changes to the navigation path. Useful in cases where a folder or directory has many folders and users are manually typing out a path.

5. **Interactive Events**:

   - Supports events like `on_click`, `on_hover`, `on_focus`, `on_enter`, and `on_exit`.
   - Flexible enough to accommodate keyboard, mouse, touch, and controller inputs.

6. **Accessibility**:

   - Provides screen reader-friendly labels for breadcrumbs and separators.
   - Fully supports keyboard and controller navigation.

---

### **Proposed Fields**

| **Field**     | **Description**                                             | **Example**                                                                          |
| ------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `path`        | The current navigation path as an array of nodes.           | `path = ["@username", "Documents", "Projects"]`                                      |
| `separator`   | The character, icon, or SVG separating breadcrumbs.         | `separator = ">"`                                                                    |
| `interactive` | Determines if breadcrumbs are clickable or static.          | `interactive = true`                                                                 |
| `tooltip`     | Tooltip for each breadcrumb, showing additional context.    | `tooltip = "Click to return to Home"`                                                |
| `animations`  | Animations for adding, removing, or truncating breadcrumbs. | `animations = { enter = "slide-right", exit = "fade-out", truncate = "slide-left" }` |

---

### **GSS Styling Parameters**

| **Parameter**         | **Description**                                              | **Example**                                 |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| `font-family`         | Defines the font for breadcrumb text.                        | `font-family = "Arial, sans-serif"`         |
| `font-size`           | Defines the size of breadcrumb text.                         | `font-size = "1rem"`                        |
| `font-color`          | Color of breadcrumb text.                                    | `font-color = "#333"`                       |
| `hover.color`         | Color of breadcrumb text on hover.                           | `hover.color = "#007BFF"`                   |
| `separator.style`     | Style of the separator symbol (e.g., font, color, SVG path). | `separator.style = { font-color = "#999" }` |
| `animations.enter`    | Animation applied when a breadcrumb is added.                | `animations.enter = "slide-right"`          |
| `animations.exit`     | Animation applied when a breadcrumb is removed.              | `animations.exit = "fade-out"`              |
| `animations.truncate` | Animation applied when truncating breadcrumbs.               | `animations.truncate = "slide-left"`        |
| `overflow.icon`       | Icon or SVG used to indicate truncated paths.                | `overflow.icon = "@assets/more.svg"`        |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "navigation_box"
path = ["Home", "Documents", "Projects"]
separator = "/"
interactive = true
animations = { enter = "slide-right", exit = "fade-out", truncate = "slide-left" }
```

---

### **Example GSS Implementation**

```toml
[navigation_box]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"

[navigation_box.separator]
style = "/"
font-color = "#999"

[navigation_box.animations]
enter = "slide-right"
exit = "fade-out"
truncate = "slide-left"

[navigation_box.hover]
font-color = "#007BFF"

[navigation_box.overflow]
icon = "@assets/more.svg"
```

---

### **Advanced Considerations**

1. **Input Adaptability**:

   - GSS developers can redefine how users interact with breadcrumbs (e.g., clicking, hovering, or using keyboard/controller shortcuts).

2. **Dynamic Path Updates**:

   - Integration with co-chains (e.g., Pages) to fetch and update navigation paths dynamically.

3. **Fuzzy Finding**:

   - Enable users to type a path manually and suggest completions based on available folders.

4. **Truncation Enhancements**:

   - Allow users to interact with truncated paths by clicking the "more" icon to expand hidden breadcrumbs.

5. **Custom Separators**:

   - Support for SVGs or complex icons as separators for highly customized designs.

---

### **Conclusion**

The Navigation Box Widget provides an essential tool for hierarchical navigation. With support for advanced animations, custom separators, and dynamic updates, it adapts seamlessly to both static and dynamic navigation scenarios. The flexibility of GSS ensures a consistent yet customizable user experience across devices and input types.

---

### **Scroll Area Widget**

The Scroll Area Widget provides an intuitive way to navigate additional content within a limited space. It supports vertical, horizontal, or bidirectional scrolling and offers extensive customization options for behavior, appearance, and interactivity.

---

### **Core Features**
1. **Orientation**:
   - Supports vertical, horizontal, or both directions for scrolling.

2. **Customizable Scrollbars**:
   - Options for scrollbar visibility (always visible, auto-hide after inactivity, or hidden).
   - Styleable scrollbar appearance, including size, color, gradients, patterns, and even images with repeating patterns.
   - Supports active scrollbars that change visually based on scroll progress (e.g., gradients).

3. **Easing and Smooth Scrolling**:
   - Allows GSS designers to define easing effects for a custom scrolling feel.
   - Supports different easing curves (e.g., linear, ease-in, ease-out).

4. **Interactive Events**:
   - Events like `on_scroll`, `on_scroll_end`, `on_scroll_start`, `on_reach_end`, `on_enter`, and `on_exit`.
   - Example: `on_enter` could trigger a subtle wiggle animation to hint at scrollability.

5. **Infinite Scroll Support**:
   - Dynamically loads additional content as users scroll, with visual indicators for infinite scrolling.

6. **Responsive Design**:
   - Automatically adjusts to the available view area, ensuring compatibility across devices and orientations.

7. **Accessibility**:
   - Provides clear indicators for scrollable areas and supports keyboard and controller navigation.

---

### **Proposed Fields**
| **Field**          | **Description**                                                        | **Example**                            |
|--------------------|------------------------------------------------------------------------|----------------------------------------|
| `orientation`      | Defines the scroll direction (`vertical`, `horizontal`, or `both`).    | `orientation = "vertical"`             |
| `scrollbar`        | Configures scrollbar behavior (`visible`, `hidden`, or `auto-hide`).   | `scrollbar = "auto-hide"`              |
| `easing`           | Defines the easing effect for scrolling.                              | `easing = "ease-in-out"`               |
| `scroll_speed`     | Adjusts the speed of the scroll.                                       | `scroll_speed = "normal"`              |
| `infinite_scroll`  | Enables infinite scrolling, dynamically loading more content.          | `infinite_scroll = true`               |
| `padding`          | Padding around the scrollable content.                                | `padding = "10px"`                     |
| `margin`           | Margin around the scroll area container.                              | `margin = "15px"`                      |

---

### **GSS Styling Parameters**
| **Parameter**          | **Description**                                                    | **Example**                            |
|------------------------|--------------------------------------------------------------------|----------------------------------------|
| `scrollbar.size`       | Size (thickness) of the scrollbar.                                | `scrollbar.size = "8px"`               |
| `scrollbar.color`      | Color of the scrollbar.                                           | `scrollbar.color = "#333"`             |
| `scrollbar.track.color`| Color of the scrollbar track.                                     | `scrollbar.track.color = "#EEE"`       |
| `scrollbar.pattern`    | Image or pattern used for the scrollbar.                         | `scrollbar.pattern = "@assets/bar.png"`|
| `scrollbar.gradient`   | Gradient for the scrollbar that changes with scroll position.     | `scrollbar.gradient = "linear-gradient(to bottom, #007BFF, #FFF)"` |
| `easing`               | Defines the easing curve for scrolling behavior.                 | `easing = "ease-in-out"`               |
| `scrollbar.auto-hide`  | Duration before the scrollbar auto-hides (if enabled).            | `scrollbar.auto-hide = "2s"`           |
| `animations.enter`     | Animation applied when the scroll area is entered.                | `animations.enter = "wiggle"`          |
| `animations.exit`      | Animation applied when the scroll area is exited.                 | `animations.exit = "fade-out"`         |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "scroll_area"
orientation = "vertical"
scrollbar = "auto-hide"
easing = "ease-in-out"
scroll_speed = "normal"
infinite_scroll = true
padding = "10px"
margin = "15px"

children = [
    {
        type = "text",
        content = "This is some scrollable content.",
        style = "paragraph"
    },
    {
        type = "text",
        content = "Keep scrolling to see more.",
        style = "paragraph"
    }
]
```

---

### **Example GSS Implementation**
```toml
[scroll_area]
padding = "10px"
margin = "15px"

[scroll_area.scrollbar]
size = "8px"
color = "#333"
track.color = "#EEE"
pattern = "@assets/bar.png"
gradient = "linear-gradient(to bottom, #007BFF, #FFF)"
auto-hide = "2s"

[scroll_area.easing]
easing = "ease-in-out"

[scroll_area.animations]
enter = "wiggle"
exit = "fade-out"
```

---

### **Advanced Considerations**
1. **Infinite Scroll Enhancements**:
   - Allow visual indicators (e.g., "Loading..." or spinners) during content fetch.
   - GSS designers can customize styles for loading indicators.

2. **Custom Scrollbar Design**:
   - Include support for SVGs, animations, and dynamic patterns for the scrollbar.

3. **Truncation Enhancements**:
   - Automatically adjust the scroll area’s dimensions based on the parent container.

4. **Event Handling**:
   - Add support for events like:
     - `on_scroll_start`: Triggered when scrolling begins.
     - `on_scroll_end`: Triggered when scrolling stops.
     - `on_reach_end`: Triggered when the user scrolls to the end of the content.

5. **Cross-Device Compatibility**:
   - Ensure smooth and intuitive scrolling behavior across mouse, touch, and controller inputs.

---

### **Conclusion**
The Scroll Area Widget provides a versatile and visually appealing solution for handling overflow content. With advanced features like infinite scrolling, custom scrollbar designs, and dynamic interactions, it adapts seamlessly to diverse application needs and enhances the user experience across all input types.

---

### **Drop Menu Widget**

The Drop Menu Widget provides a versatile way to present a collapsible list of options for selection. It supports single or multi-option selection, dynamic content, advanced interactivity, and now includes both visual and audio animation support for enhanced engagement.

---

### **Core Features**
1. **Single or Multi-Select**:
   - Supports single-option or multi-option selection.
   - Multi-select menus can include checkboxes or toggles for selection.

2. **Grouped Options**:
   - Allows grouping of related options under headers.
   - Supports dividers for logical separation of option groups.

3. **Customizable Behavior**:
   - Define whether the menu opens on hover, click, or another interaction.
   - Optionally allow the menu to remain open after a selection.

4. **Dynamic Content**:
   - Fetch options dynamically from co-chains or APIs.
   - Auto-update when the data source changes.
   - Example: Place the co-chain link in the `options` field to fetch options dynamically.

5. **Searchable Menus**:
   - Auto-completes or jumps to options as the user begins typing.

6. **Images and Colors for Options**:
   - Allows options to include images or icons next to text.
   - Supports color-coded options or groups for better visual distinction.

7. **Animations (Visual and Audio)**:
   - Smooth animations for menu opening, closing, item highlighting, and selection.
   - Audio can be defined as a "parallel animation" within the animation configuration.

8. **Interactive Events**:
   - Events like `on_open`, `on_close`, `on_item_hover`, and `on_item_select` for granular interactivity.

9. **Accessibility**:
   - Keyboard and controller navigable.
   - Screen reader-friendly labels for each option.

10. **Overflow Handling**:
    - Automatically scrolls or truncates long option lists.

---

### **Proposed Fields**
| **Field**          | **Description**                                                        | **Example**                              |
|--------------------|------------------------------------------------------------------------|------------------------------------------|
| `options`          | An array of options or a link to a data source.                       | `options = ["Option 1", "Option 2"]`     |
| `multi_select`     | Enables multi-option selection.                                       | `multi_select = false`                   |
| `default`          | The default selected option(s).                                       | `default = "Option 1"`                   |
| `placeholder`      | Text displayed when no option is selected.                            | `placeholder = "Select an option"`       |
| `grouped_options`  | Logical grouping of options with headers or dividers.                 | `grouped_options = true`                 |
| `open_behavior`    | Defines the behavior for opening the menu (`hover`, `click`).         | `open_behavior = "click"`                |
| `animations`       | Animations for opening, closing, and highlighting, including audio.   | `animations = { open = { type = "fade-in", audio = "open.wav" }, close = { type = "fade-out", audio = "close.wav" }, on_item_hover = { type = "scale-up", audio = "hover.wav" }, on_item_select = { type = "pulse", audio = "select.wav" } }` |
| `searchable`       | Enables a search feature for large option sets.                      | `searchable = true`                      |
| `max_height`       | Maximum height for the dropdown menu before enabling scrolling.       | `max_height = "200px"`                   |
| `option_images`    | Includes images or icons next to text in options.                    | `option_images = true`                   |
| `option_colors`    | Assigns colors to specific options or groups.                        | `option_colors = true`                   |

---

### **GSS Styling Parameters**
| **Parameter**          | **Description**                                                    | **Example**                              |
|------------------------|--------------------------------------------------------------------|------------------------------------------|
| `menu.font-family`     | Defines the font for menu text.                                   | `menu.font-family = "Arial, sans-serif"` |
| `menu.font-size`       | Defines the size of menu text.                                    | `menu.font-size = "1rem"`                |
| `menu.background`      | Background color of the dropdown menu.                           | `menu.background = "#FFF"`               |
| `menu.border`          | Border style of the dropdown menu.                               | `menu.border = "1px solid #333"`         |
| `menu.hover.background`| Background color of menu items on hover.                         | `menu.hover.background = "#EEE"`         |
| `menu.selected.color`  | Color of selected menu items.                                     | `menu.selected.color = "#007BFF"`        |
| `menu.option.image`    | Styling for images/icons next to options.                        | `menu.option.image = { size = "16px" }`  |
| `menu.option.color`    | Styling for color-coded options.                                 | `menu.option.color = "#FF5733"`          |
| `group.header.style`   | Styling for grouped option headers.                              | `group.header.style = { font-weight = "bold" }` |
| `group.divider.style`  | Styling for dividers between option groups.                      | `group.divider.style = { color = "#CCC" }` |
| `animations.open`      | Animation applied when the menu opens.                           | `animations.open = { type = "fade-in", audio = "open.wav" }` |
| `animations.close`     | Animation applied when the menu closes.                          | `animations.close = { type = "fade-out", audio = "close.wav" }` |
| `animations.on_item_hover` | Animation applied when an item is hovered over.              | `animations.on_item_hover = { type = "scale-up", audio = "hover.wav" }` |
| `animations.on_item_select`| Animation applied when an item is selected.                  | `animations.on_item_select = { type = "pulse", audio = "select.wav" }` |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "drop_menu"
placeholder = "Select an option"
multi_select = true
default = ["Option 1"]
open_behavior = "click"
searchable = true
options = [
    { group = "Favorites", options = [
        { text = "Option 1", image = "@assets/icon1.png", color = "#FF5733" },
        { text = "Option 2", image = "@assets/icon2.png", color = "#33FF57" }
    ] },
    { group = "More Options", options = [
        { text = "Option 3", image = "@assets/icon3.png", color = "#3357FF" },
        { text = "Option 4", image = "@assets/icon4.png", color = "#5733FF" }
    ] }
]
animations = { open = { type = "fade-in", audio = "open.wav" }, close = { type = "fade-out", audio = "close.wav" }, on_item_hover = { type = "scale-up", audio = "hover.wav" }, on_item_select = { type = "pulse", audio = "select.wav" } }
```

---

### **Example GSS Implementation**
```toml
[drop_menu]
font-family = "Arial, sans-serif"
font-size = "1rem"
background = "#FFF"
border = "1px solid #333"

[drop_menu.menu.hover]
background = "#EEE"

[drop_menu.menu.selected]
color = "#007BFF"

[menu.option.image]
size = "16px"

[menu.option.color]
default = "#FF5733"
hover = "#007BFF"

[group.header]
style = { font-weight = "bold", font-size = "1.2rem" }

[group.divider]
style = { color = "#CCC", thickness = "1px" }

[drop_menu.animations]
open = { type = "fade-in", audio = "open.wav" }
close = { type = "fade-out", audio = "close.wav" }
on_item_hover = { type = "scale-up", audio = "hover.wav" }
on_item_select = { type = "pulse", audio = "select.wav" }
```

---

### **Advanced Considerations**
1. **Searchable Menus**:
   - Auto-completes or jumps to options as the user begins typing.

2. **Grouped Options**:
   - Logical separation for improved user clarity.
   - Dividers and headers to visually distinguish sections.

3. **Dynamic Content**:
   - Fetch menu options dynamically from co-chains or APIs.
   - Place the link in the `options` field to enable dynamic fetching.

4. **Custom Option Styling**:
   - Allow GSS developers to style individual options uniquely.
   - Include options for images/icons and color-coding.

5. **Multi-Device Compatibility**:
   - Ensure intuitive behavior across mouse, touch, and controller inputs.

6. **Audio Feedback as Parallel Animation**:
   - Integrate audio cues within the animation configuration for streamlined implementation and synchronized effects.

---

### **Conclusion**
The Drop Menu Widget offers a highly flexible and interactive solution for presenting selectable options. With features like grouping, animations, dynamic data, search capabilities, and visual/audio enhancements, it adapts seamlessly to various use cases while ensuring an engaging user experience across all devices and input methods.

---

### **Item Grid Widget**

The Item Grid Widget organizes items or elements into a grid layout, allowing users to interact with each cell. It is ideal for inventory systems, file management, or visual data organization and is designed to be intuitive across multiple input devices, including controllers.

---

### **Core Features**
1. **Grid Layout**:
   - Configurable rows and columns.
   - Dynamically adjusts based on available space or item count.

2. **Navigation**:
   - Fully navigable with keyboard, touch, and controller inputs.
   - Supports `on_focus`, `on_select`, and `on_hover` events for each grid cell.

3. **Cell Customization**:
   - Cells can contain images, icons, text, or interactive widgets (e.g., buttons or toggles).
   - Background colors for each cell to indicate specific asset types.

4. **Dynamic Updates**:
   - Add, remove, or rearrange items dynamically.
   - Option to load content from co-chains.
   - Includes loading animations to indicate asset retrieval.

5. **Grouping**:
   - Support for grouping items within bordered sections (e.g., digital asset categories).
   - Borders can be styled or colored for visual clarity.

6. **Accessibility**:
   - Provides labels or tooltips for each cell.
   - Supports focus management for screen readers.

7. **Animations**:
   - Smooth animations for item addition, removal, rearrangement, and loading.
   - Optional visual effects on selection or focus.

---

### **Proposed Fields**
| **Field**        | **Description**                                                     | **Example**                              |
|------------------|---------------------------------------------------------------------|------------------------------------------|
| `grid_size`      | Defines the number of rows and columns.                             | `grid_size = { rows = 4, columns = 5 }`  |
| `cell_size`      | Dimensions of each grid cell.                                       | `cell_size = "64px"`                   |
| `items`          | Array of items to display in the grid.                              | `items = ["sword.png", "shield.png"]` |
| `dynamic`        | Enables dynamic item management (e.g., add/remove items).           | `dynamic = true`                         |
| `loading_animation` | Animation shown while assets are loading.                        | `loading_animation = "spin"`           |
| `grouping`       | Defines groups of items with visual borders.                        | `grouping = true`                        |
| `navigation`     | Configures navigation behavior for controllers and keyboards.       | `navigation = "controller"`            |
| `animations`     | Animations for item interactions.                                   | `animations = { add = "fade-in", remove = "fade-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**         | **Description**                                                | **Example**                              |
|-----------------------|----------------------------------------------------------------|------------------------------------------|
| `grid.gap`            | Spacing between grid cells.                                    | `grid.gap = "10px"`                    |
| `grid.background`     | Background color of the grid.                                  | `grid.background = "#333"`             |
| `cell.border`         | Border style for each cell.                                    | `cell.border = "1px solid #FFF"`       |
| `cell.hover.effect`   | Visual effect on hover.                                        | `cell.hover.effect = "glow"`           |
| `cell.selected.effect`| Effect for selected cells.                                     | `cell.selected.effect = "scale-up"`    |
| `cell.loading.animation` | Animation for loading items into a cell.                   | `cell.loading.animation = "spin"`      |
| `cell.background.color` | Background color for individual cells (e.g., asset type).    | `cell.background.color = "#FF5733"`    |
| `group.border`        | Border style for item groups.                                  | `group.border = "2px solid #CCC"`      |
| `group.background`    | Background color for grouped areas.                           | `group.background = "#F0F0F0"`         |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "item_grid"
grid_size = { rows = 3, columns = 4 }
cell_size = "64px"
dynamic = true
loading_animation = "spin"
grouping = true
items = [
    { id = "1", image = "@assets/sword.png", tooltip = "Sword", background_color = "#FF5733" },
    { id = "2", image = "@assets/shield.png", tooltip = "Shield", background_color = "#33FF57" },
    { id = "3", image = "@assets/potion.png", tooltip = "Potion", background_color = "#3357FF" }
]
animations = { add = "fade-in", remove = "fade-out" }
```

---

### **Example GSS Implementation**
```toml
[item_grid]
grid.gap = "10px"
grid.background = "#333"

[cell]
border = "1px solid #FFF"
hover.effect = "glow"
selected.effect = "scale-up"
loading.animation = "spin"
background.color = "#FF5733"

[group]
border = "2px solid #CCC"
background = "#F0F0F0"
```

---

### **Advanced Considerations**
1. **Item Interaction**:
   - Support drag-and-drop for rearranging items.
   - Context menus for item-specific actions.

2. **Pagination**:
   - Include support for large grids that exceed the visible area.

3. **Dynamic Co-Chain Integration**:
   - Fetch item data dynamically, such as inventory updates from a co-chain.

4. **Custom Animations**:
   - Allow GSS designers to define unique animations for item interactions and loading effects.

5. **Enhanced Grouping**:
   - Provide detailed grouping with unique styles for each group (e.g., different borders, backgrounds).

---

### **Conclusion**
The Item Grid Widget offers a robust and interactive way to organize and manage items visually. With features like grouping, dynamic updates, custom animations, and accessibility, it caters to diverse use cases and ensures a seamless experience across input devices.

---

### **Slider Widget**

The Slider Widget is a versatile component for selecting values or ranges within a defined spectrum. It supports advanced interactivity, dynamic range updates, and input-specific behavior to enhance usability across devices.

---

### **Core Features**
1. **Single Value and Range Selection**:
   - Supports a single slider for choosing one value or a dual slider with multiple thumbs for defining ranges.

2. **Dynamic Ranges**:
   - Min and max values can be dynamically linked to external sources, such as UndChain locations.

3. **Custom Markers and Snapping**:
   - Allow custom markers or breaks on the slider track.
   - Enable snapping to predefined values for precision.

4. **Labels and Tooltips**:
   - Display current value(s) above the slider.
   - Optionally include labels for min, max, and intermediate values.

5. **Input-Specific Behavior**:
   - Tailored sensitivity and easing for controllers, keyboard arrow keys, mouse, and touch inputs.

6. **Visual, Audio, and Haptic Feedback**:
   - Optional audio cues for changes in value, such as clicks or tones.
   - Smooth animations for slider interactions, including entrance and exit effects.
   - Haptic feedback for compatible devices to enhance the tactile experience.

7. **Interactive Events**:
   - Events like `on_change`, `on_drag_start`, `on_drag_end`, `on_enter`, and `on_exit`.

8. **Accessibility**:
   - Fully keyboard and controller navigable.
   - Screen reader-friendly descriptions for values and labels.

---

### **Proposed Fields**
| **Field**          | **Description**                                                       | **Example**                               |
|--------------------|-----------------------------------------------------------------------|-------------------------------------------|
| `min`              | Minimum value for the slider.                                        | `min = 0`                                 |
| `max`              | Maximum value for the slider.                                        | `max = 100`                               |
| `step`             | Incremental step value for adjustments.                             | `step = 1`                                |
| `value`            | Current value of the slider (for single slider).                    | `value = 50`                              |
| `range`            | Current range values (for dual sliders).                            | `range = { start = 20, end = 80 }`        |
| `tooltip`          | Enables tooltips to display current value(s).                       | `tooltip = true`                          |
| `labels`           | Enables labels for min, max, and intermediate values.               | `labels = true`                           |
| `gradient_fill`    | Defines a color gradient for the slider track.                      | `gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"` |
| `markers`          | Predefined markers or breaks on the slider.                        | `markers = [0, 25, 50, 75, 100]`          |
| `snap_to_markers`  | Enables snapping to the nearest marker value.                       | `snap_to_markers = true`                  |
| `feedback`         | Feedback options including audio and haptics for interactions.       | `feedback = { audio = { change = "beep.wav" }, haptic = { intensity = "medium" } }` |
| `animations`       | Animations for slider interactions (e.g., entrance, exit, and thumb movement). | `animations = { entrance = "fade-in", exit = "fade-out", thumb_move = "ease-in-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**            | **Description**                                                   | **Example**                              |
|--------------------------|-------------------------------------------------------------------|------------------------------------------|
| `slider.track.height`    | Height of the slider track.                                       | `slider.track.height = "6px"`          |
| `slider.track.color`     | Default color of the slider track.                               | `slider.track.color = "#CCC"`          |
| `slider.fill.color`      | Color of the filled portion of the slider.                       | `slider.fill.color = "#007BFF"`        |
| `slider.thumb.size`      | Size of the slider thumb.                                        | `slider.thumb.size = "16px"`           |
| `slider.thumb.color`     | Color of the slider thumb.                                       | `slider.thumb.color = "#FFF"`          |
| `slider.thumb.hover`     | Hover effect for the slider thumb.                              | `slider.thumb.hover = "glow"`          |
| `tooltip.background`     | Background color of the tooltip.                                | `tooltip.background = "#000"`          |
| `tooltip.font.color`     | Font color of the tooltip.                                       | `tooltip.font.color = "#FFF"`          |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "slider"
min = 0
max = 100
step = 1
value = 50
tooltip = true
labels = true
gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"
markers = [0, 25, 50, 75, 100]
snap_to_markers = true
feedback = { audio = { change = "beep.wav" }, haptic = { intensity = "medium" } }
animations = { entrance = "fade-in", exit = "fade-out", thumb_move = "ease-in-out" }
```

---

### **Example GSS Implementation**
```toml
[slider.track]
height = "6px"
color = "#CCC"
fill.color = "#007BFF"

[slider.thumb]
size = "16px"
color = "#FFF"
hover = "glow"

[tooltip]
background = "#000"
font.color = "#FFF"
```

---

### **Advanced Considerations**
1. **Dynamic Range Updates**:
   - Min and max values can update dynamically by linking to external sources, such as co-chains on UndChain.

2. **Dual Sliders with Multiple Thumbs**:
   - Support for two or more thumbs to define multiple ranges.

3. **Custom Markers and Snapping**:
   - Allow snapping to predefined markers for precise selection.

4. **Input-Specific Behavior**:
   - Easing curves for keyboard arrow keys, controllers, and touch interactions.

5. **Enhanced Animations**:
   - Entrance and exit animations for smoother transitions.
   - Dynamic animations for thumb movement and snapping.

6. **Haptic Feedback Integration**:
   - Provide tactile responses for interactions to enhance user experience on compatible devices.

---

### **Conclusion**
The Slider Widget is a highly customizable and interactive component for selecting values or ranges. With features like dynamic ranges, custom markers, snapping, enhanced animations, and feedback options (audio and haptics), it adapts seamlessly to various use cases while ensuring an engaging user experience across all input devices.

---

### **Progress Bar Widget**

The Progress Bar Widget visually represents progress toward a goal. It is customizable for various use cases, such as task completion, loading indicators, or milestone tracking, with support for animations, tooltips, and dynamic updates.

---

### **Core Features**
1. **Single or Multi-Step Progress**:
   - Supports continuous progress bars for single tasks.
   - Multi-step progress bars with defined milestones or stages.

2. **Customizable Range and Precision**:
   - Define the minimum and maximum values for the progress.
   - Supports precision for fractional progress updates.

3. **Dynamic Updates**:
   - Real-time updates to reflect progress changes.
   - Can integrate with external sources for dynamic progress tracking.

4. **Visual Indicators**:
   - Color-coded segments to represent different stages or statuses.
   - Optional gradient fills for smoother transitions.

5. **Labels and Tooltips**:
   - Display the current progress percentage or value directly on the bar.
   - Tooltips to show additional context for progress.

6. **Input-Specific Feedback**:
   - Includes visual, audio, and haptic feedback for updates and completions.

7. **Interactive Events**:
   - Events like `on_start`, `on_progress`, and `on_complete`.

8. **Accessibility**:
   - Screen reader-friendly descriptions for progress updates.
   - Fully navigable and understandable for users with disabilities.

---

### **Proposed Fields**
| **Field**          | **Description**                                                       | **Example**                               |
|--------------------|-----------------------------------------------------------------------|-------------------------------------------|
| `min`              | Minimum value of the progress bar.                                   | `min = 0`                                 |
| `max`              | Maximum value of the progress bar.                                   | `max = 100`                               |
| `value`            | Current progress value.                                              | `value = 50`                              |
| `segments`         | Defines segments for multi-step progress bars.                      | `segments = [25, 50, 75, 100]`            |
| `tooltip`          | Enables tooltips to display progress details.                       | `tooltip = true`                          |
| `gradient_fill`    | Defines a color gradient for the progress bar.                      | `gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"` |
| `feedback`         | Feedback options including audio and haptics for updates.            | `feedback = { audio = { progress = "tick.wav" }, haptic = { intensity = "low" } }` |
| `animations`       | Animations for progress updates and completion.                     | `animations = { update = "smooth", completion = "pulse" }` |

---

### **GSS Styling Parameters**
| **Parameter**            | **Description**                                                   | **Example**                              |
|--------------------------|-------------------------------------------------------------------|------------------------------------------|
| `progress.bar.height`    | Height of the progress bar.                                       | `progress.bar.height = "10px"`          |
| `progress.bar.color`     | Default color of the progress bar.                               | `progress.bar.color = "#CCC"`          |
| `progress.fill.color`    | Color of the filled portion of the progress bar.                 | `progress.fill.color = "#007BFF"`      |
| `progress.segment.color` | Color for individual segments in a multi-step progress bar.      | `progress.segment.color = "#00FF00"`   |
| `tooltip.background`     | Background color of the tooltip.                                | `tooltip.background = "#000"`          |
| `tooltip.font.color`     | Font color of the tooltip.                                       | `tooltip.font.color = "#FFF"`          |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "progress_bar"
min = 0
max = 100
value = 50
tooltip = true
gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"
segments = [25, 50, 75, 100]
feedback = { audio = { progress = "tick.wav" }, haptic = { intensity = "low" } }
animations = { update = "smooth", completion = "pulse" }
```

---

### **Example GSS Implementation**
```toml
[progress.bar]
height = "10px"
color = "#CCC"
fill.color = "#007BFF"

[progress.segment]
color = "#00FF00"

[tooltip]
background = "#000"
font.color = "#FFF"
```

---

### **Advanced Considerations**
1. **Real-Time Updates**:
   - Fetch progress data dynamically from external sources or co-chains.

2. **Custom Completion Effects**:
   - Allow developers to customize animations and feedback for completed progress bars.

3. **Multi-Device Feedback**:
   - Provide consistent feedback across devices, including haptic responses on mobile and controller inputs.

4. **Segmented Progress Bars**:
   - Highlight milestones or stages within the progress bar.
   - Allow unique styles and effects for each segment.

---

### **Conclusion**
The Progress Bar Widget offers a customizable and dynamic way to visualize progress. With features like real-time updates, segmented progress, and feedback options (audio, visual, and haptics), it provides an engaging and accessible experience for diverse applications and devices.

---

### **Tooltip Widget**

The Tooltip Widget provides contextual information when a user hovers or focuses on an element. It enhances usability by displaying descriptions or additional details about a widget, offering guidance or feedback to users.

---

### **Core Features**
1. **Default Tooltip Behavior**:
   - Displays the description of each widget when no specific tooltip settings are provided.

2. **Customizable Appearance**:
   - Designers can define font, color, size, and other visual attributes of tooltips.

3. **Fly-In Animations**:
   - Includes animations for how the tooltip appears, such as fading, sliding, or scaling.

4. **Trigger Options**:
   - Tooltips can be triggered by hover, focus, touch, prolonged hover, or double-click input events.

5. **Placement Options**:
   - Configurable placement (top, bottom, left, right, or auto) relative to the widget.

6. **Dynamic Content**:
   - Can dynamically fetch and display content based on interactions or external data.

7. **Feedback Integration**:
   - Includes visual, audio, and haptic feedback when the tooltip is triggered.

8. **Duration Control**:
   - Configurable display duration for tooltips to remain visible.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `content`           | Text or content to display in the tooltip.                           | `content = "This is a tooltip."`        |
| `trigger`           | Defines what triggers the tooltip (`hover`, `focus`, `touch`, `prolonged_hover`, `double_click`). | `trigger = "hover"`                     |
| `placement`         | Position of the tooltip relative to the element.                    | `placement = "top"`                     |
| `animation`         | Animation type for the tooltip's appearance.                        | `animation = "fade-in"`                 |
| `feedback`          | Feedback options including audio and haptics.                       | `feedback = { audio = "tooltip.wav", haptic = "soft" }` |
| `duration`          | Duration in seconds for how long the tooltip remains visible.        | `duration = 5`                           |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `tooltip.background`      | Background color of the tooltip.                                 | `tooltip.background = "#000"`          |
| `tooltip.font.color`      | Font color of the tooltip.                                       | `tooltip.font.color = "#FFF"`          |
| `tooltip.font.size`       | Font size of the tooltip text.                                   | `tooltip.font.size = "14px"`           |
| `tooltip.border`          | Border style of the tooltip.                                     | `tooltip.border = "1px solid #FFF"`    |
| `tooltip.padding`         | Padding inside the tooltip.                                      | `tooltip.padding = "8px"`              |
| `tooltip.margin`          | Margin between the tooltip and the target element.              | `tooltip.margin = "5px"`               |
| `tooltip.shadow`          | Shadow effect for the tooltip.                                  | `tooltip.shadow = "2px 2px 5px rgba(0,0,0,0.5)"` |
| `tooltip.animation`       | Animation style for the tooltip's appearance.                   | `tooltip.animation = "fade-in"`        |
| `tooltip.duration`        | Time the tooltip remains visible before disappearing.            | `tooltip.duration = "5s"`              |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "tooltip"
content = "This is a helpful tooltip."
trigger = "hover"
placement = "top"
animation = "fade-in"
feedback = { audio = "tooltip.wav", haptic = "soft" }
duration = 5
```

---

### **Example GSS Implementation**
```toml
[tooltip]
background = "#000"
font.color = "#FFF"
font.size = "14px"
border = "1px solid #FFF"
padding = "8px"
margin = "5px"
shadow = "2px 2px 5px rgba(0,0,0,0.5)"
animation = "fade-in"
duration = "5s"
```

---

### **Advanced Considerations**
1. **Dynamic Content**:
   - Fetch tooltip content dynamically based on user interactions or external data sources.

2. **Interactive Tooltips**:
   - Allow interactive elements, such as buttons or links, within the tooltip.

3. **Accessibility Enhancements**:
   - Ensure tooltips are screen reader accessible and provide meaningful descriptions.

4. **Device-Specific Triggers**:
   - Adapt triggers based on the input type (e.g., touch vs. mouse).

5. **Custom Animations**:
   - Support for advanced animations, such as bounce or spin effects, for enhanced user engagement.

6. **Duration Controls**:
   - Define how long tooltips should stay visible and automatically disappear after the duration ends.

---

### **Conclusion**
The Tooltip Widget is a powerful tool for providing contextual information and enhancing user understanding. With customizable triggers, placements, animations, feedback, and duration controls, it adapts seamlessly to diverse use cases while maintaining accessibility and interactivity.

---

### **Card Widget**

The Card Widget is a versatile component used for compact content presentation. It can display information, include interactive elements, and support advanced transitions such as flipping or morphing into a poster.

---

### **Core Features**
1. **Card Types**:
   - **Informational Cards**: Static, text/image-focused.
   - **Interactive Cards**: Includes actionable elements like buttons or sliders.
   - **Data Cards**: Displays structured data like graphs or metrics.
   - **Hybrid Cards**: Combines informational and interactive elements, with support for flipping to reveal additional content.

2. **Customizable Layout**:
   - Supports layouts like `horizontal`, `vertical`, or `grid`.

3. **Morphing to Poster**:
   - Cards can transition into larger posters for detailed content presentation.
   - A dedicated button appears when `poster` is enabled, which can be styled by GSS developers.

4. **Dynamic Updates**:
   - Can fetch and update content dynamically (e.g., via co-chains).

5. **Interactive States**:
   - Includes `on_hover`, `on_click`, `on_expand`, and more.

6. **Styling Options**:
   - Fully customizable with borders, shadows, animations, and background styles.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `type`              | Defines the type of card (`informational`, `interactive`, etc.).      | `type = "interactive"`                 |
| `layout`            | Layout of the card (`horizontal`, `vertical`, `grid`).               | `layout = "vertical"`                  |
| `content`           | Array of widgets (text, images, buttons) within the card.            | `content = [ { type = "text", value = "Product Name" }, { type = "button", label = "Buy" } ]` |
| `border`            | Border styling for the card.                                         | `border = "1px solid #CCC"`            |
| `shadow`            | Shadow effect for the card.                                          | `shadow = "2px 2px 5px rgba(0,0,0,0.5)"` |
| `background`        | Background styling (color or gradient).                             | `background = "linear-gradient(to right, #FFF, #EEE)"` |
| `animation`         | Animations for hover, click, or expand.                             | `animation = { hover = "scale-up", expand = "fade-in" }` |
| `poster`            | Enables morphing the card into a larger poster.                     | `poster = true`                          |
| `poster_button`     | Enables a dedicated button for transitioning into the poster view.   | `poster_button = { label = "Expand", style = "primary" }` |
| `flip`              | Enables flipping the card to reveal additional content.             | `flip = { trigger = "on_click", animation = "rotate-y" }` |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `card.border`             | Border style for cards.                                           | `card.border = "1px solid #CCC"`      |
| `card.shadow`             | Shadow effect for cards.                                          | `card.shadow = "2px 2px 5px rgba(0,0,0,0.5)"` |
| `card.background`         | Background styling for cards.                                     | `card.background = "#FFF"`            |
| `card.layout`             | Layout direction (`horizontal`, `vertical`, `grid`).             | `card.layout = "vertical"`            |
| `card.animation.hover`    | Animation for hover interactions (e.g., raising the card).        | `card.animation.hover = "scale-up"`   |
| `card.animation.expand`   | Animation for expanding cards or morphing into posters.          | `card.animation.expand = "fade-in"`   |
| `poster.background`       | Background style for posters.                                    | `poster.background = "#FFF"`          |
| `poster.shadow`           | Shadow effect for posters.                                       | `poster.shadow = "5px 5px 10px rgba(0,0,0,0.3)"` |
| `poster.layout`           | Layout for the poster view.                                      | `poster.layout = "grid"`              |
| `poster.animation`        | Animation style for morphing cards into posters.                | `poster.animation = "scale-up"`       |
| `poster.button.style`     | Styling for the expand button in poster mode.                    | `poster.button.style = "primary"`     |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "card"
layout = "vertical"
type = "hybrid"
poster = true
poster_button = { label = "Expand", style = "primary" }
flip = { trigger = "on_hover", animation = "rotate-y" }
poster_animation = { morph = "scale-up", duration = "0.5s" }
content = [
    { type = "image", src = "@assets/product.jpg" },
    { type = "text", value = "Product Name" },
    { type = "button", label = "View Details" }
]
sides = [
    { side = "front", content = [{ type = "text", value = "Brief Description" }] },
    { side = "back", content = [{ type = "text", value = "Detailed Description" }] }
]
```

---

### **Example GSS Implementation**
```toml
[card]
layout = "vertical"
background = "#FFF"
shadow = "2px 2px 5px rgba(0,0,0,0.5)"

[card.animation]
hover = "scale-up"
expand = "fade-in"

[poster]
background = "#FFF"
shadow = "5px 5px 10px rgba(0,0,0,0.3)"
layout = "grid"
animation = "scale-up"

[poster.button]
style = "primary"
```

---

### **Advanced Considerations**
1. **Custom Templates**:
   - Allow developers to save card templates for reuse across applications.

2. **Dynamic Content**:
   - Fetch and update card content from co-chains or APIs.

3. **Device-Specific Behavior**:
   - Adjust layout and interaction style for different devices (e.g., mobile, controller).

4. **Accessibility Enhancements**:
   - Provide clear focus indicators and screen reader-friendly content.

5. **Poster Transitions**:
   - Enable smooth morphing between card and poster views for enhanced usability.

---

### **Conclusion**
The Card Widget offers a robust and flexible solution for content presentation. With options for flipping, expanding, and morphing into posters, along with extensive styling and animation capabilities, it adapts seamlessly to diverse use cases while maintaining accessibility and interactivity.

---

### **Poster Widget**

The Poster Widget is an extension of the Card Widget, designed to present detailed content in a larger format. Posters are particularly effective for immersive displays, dominating the view for greater emphasis, especially on mobile devices. Posters can also shrink to morph back into cards when needed.

---

### **Core Features**
1. **Expanded Content Presentation**:
   - Posters provide more space for detailed information, images, or actions.
   - Ideal for media-rich content or complex layouts.

2. **Morphing Behavior**:
   - Posters can morph into cards for compact presentation.
   - Includes animations for smooth transitions between poster and card states.

3. **Pre-Defined Poster Types**:
   - **Informational Posters**: Display large blocks of text or images.
   - **Interactive Posters**: Include interactive elements like forms, sliders, and buttons.
   - **Data Posters**: Show detailed charts, graphs, and tables.
   - **Media Posters**: Showcase videos, image galleries, or live streams.
   - **Hybrid Posters**: Combine static and interactive elements, with expandable sections.
   - **Hero Posters**: Highlight bold calls-to-action with layered text and visuals.
   - **Tutorial Posters**: Provide step-by-step instructions or guides.
   - **Split Posters**: Divide content into multiple sections for comparisons.
   - **Scrollable Posters**: Allow vertical or horizontal scrolling within the poster itself.

4. **Reusable Templates**:
   - Developers can use predefined templates for common poster types, simplifying M3L creation.

5. **Dynamic Layouts**:
   - Layouts can adapt based on screen size or input device.

6. **Interactive States**:
   - Supports `on_expand`, `on_collapse`, `on_hover`, `on_scroll`, and other events.

7. **Styling Options**:
   - Fully customizable with borders, shadows, animations, and background styles.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `type`              | Defines the poster type (e.g., `informational`, `media`, `split`).    | `type = "media"`                      |
| `layout`            | Layout for the poster (`grid`, `flex`, etc.).                        | `layout = "grid"`                      |
| `content`           | Array of widgets (text, images, buttons) within the poster.          | `content = [ { type = "text", value = "Detailed Info" }, { type = "button", label = "Action" } ]` |
| `border`            | Border styling for the poster.                                       | `border = "1px solid #CCC"`            |
| `shadow`            | Shadow effect for the poster.                                        | `shadow = "5px 5px 10px rgba(0,0,0,0.3)"` |
| `background`        | Background styling (color or gradient).                             | `background = "linear-gradient(to right, #FFF, #EEE)"` |
| `animation`         | Animations for morphing and other interactions.                     | `animation = { expand = "scale-up", collapse = "scale-down" }` |
| `card_morph`        | Enables morphing into a card.                                        | `card_morph = true`                      |
| `interactive_button`| Adds a button for collapsing the poster back into a card.            | `interactive_button = { label = "Collapse", style = "secondary" }` |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `poster.border`           | Border style for posters.                                         | `poster.border = "1px solid #CCC"`    |
| `poster.shadow`           | Shadow effect for posters.                                       | `poster.shadow = "5px 5px 10px rgba(0,0,0,0.3)"` |
| `poster.background`       | Background styling for posters.                                  | `poster.background = "#FFF"`          |
| `poster.layout`           | Layout direction (`grid`, `flex`, etc.).                         | `poster.layout = "grid"`              |
| `poster.animation.expand` | Animation for expanding the poster.                             | `poster.animation.expand = "scale-up"` |
| `poster.animation.collapse` | Animation for collapsing the poster into a card.               | `poster.animation.collapse = "scale-down"` |
| `poster.button.style`     | Styling for the collapse button.                                 | `poster.button.style = "secondary"`   |
| `poster.scrollbar.style`  | Styling for scrollable posters.                                  | `poster.scrollbar.style = "minimal"`  |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "poster"
layout = "grid"
type = "split"
border = "1px solid #CCC"
shadow = "5px 5px 10px rgba(0,0,0,0.3)"
background = "linear-gradient(to right, #FFF, #EEE)"
animation = { expand = "scale-up", collapse = "scale-down" }
card_morph = true
interactive_button = { label = "Collapse", style = "secondary" }
content = [
    { type = "image", src = "@assets/comparison_left.jpg" },
    { type = "image", src = "@assets/comparison_right.jpg" }
]
```

---

### **Example GSS Implementation**
```toml
[poster]
border = "1px solid #CCC"
shadow = "5px 5px 10px rgba(0,0,0,0.3)"
background = "#FFF"
layout = "grid"

[poster.animation]
expand = "scale-up"
collapse = "scale-down"

[poster.button]
style = "secondary"

[poster.scrollbar]
style = "minimal"
```

---

### **Advanced Considerations**
1. **Dynamic Adaptation**:
   - Adjust layouts and interactions based on device type (e.g., mobile vs. desktop).

2. **Custom Animations**:
   - Allow GSS developers to define unique animations for expanding and collapsing posters.

3. **Interactive Buttons**:
   - Provide clear controls for transitioning between poster and card states.

4. **Device-Specific Behavior**:
   - Optimize poster usability for touch, mouse, and controller inputs.

5. **Reusable Templates**:
   - Offer predefined templates for common poster types to streamline development.

6. **Scrollable Content**:
   - Enable smooth scrolling within posters, with customizable scrollbar styles.

---

### **Conclusion**
The Poster Widget builds on the flexibility of the Card Widget, offering a detailed and immersive way to present content. With support for morphing, dynamic layouts, reusable templates, and extensive styling, posters enhance user engagement and are ideal for media-rich or complex presentations.

---

### **Banner Widget**

The Banner Widget is a horizontally oriented container, similar to a card but optimized for wide layouts. Banners are often used for showcasing promotions, alerts, or summary information. They can fill the entire parent widget's space or include customizable margins for precise placement.

---

### **Core Features**
1. **Horizontal Layout**:
   - Designed to span horizontally, making it ideal for headers, alerts, or promotional content.

2. **Content Versatility**:
   - Can include text, images, buttons, and other widgets.

3. **Customizable Sizing**:
   - Banners can either fill the parent container or include margins for spacing.

4. **Interactive States**:
   - Supports events like `on_click`, `on_hover`, and `on_dismiss`.

5. **Styling Options**:
   - Fully customizable with borders, shadows, animations, and background styles.

6. **Dynamic Content Integration**:
   - Fetch content dynamically from co-chains or APIs.

7. **Dismissible Options**:
   - Includes a close button for temporary banners.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `content`           | Array of widgets displayed inside the banner.                        | `content = [ { type = "text", value = "New Sale!" }, { type = "button", label = "Shop Now" } ]` |
| `size`              | Defines the height of the banner.                                    | `size = "50px"`                        |
| `fill`              | Determines if the banner fills the parent container.                 | `fill = true`                            |
| `margin`            | Specifies margin around the banner if `fill` is false.               | `margin = "10px"`                      |
| `dismissible`       | Enables a close button for dismissing the banner.                   | `dismissible = true`                     |
| `animation`         | Animations for appearance or dismissal.                             | `animation = { enter = "slide-in", exit = "fade-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `banner.size`             | Height of the banner.                                             | `banner.size = "50px"`                 |
| `banner.background`       | Background styling for the banner.                               | `banner.background = "linear-gradient(to right, #007BFF, #0056b3)"` |
| `banner.margin`           | Margin around the banner.                                         | `banner.margin = "10px"`              |
| `banner.border`           | Border style for the banner.                                      | `banner.border = "1px solid #CCC"`    |
| `banner.shadow`           | Shadow effect for the banner.                                     | `banner.shadow = "2px 2px 5px rgba(0,0,0,0.5)"` |
| `banner.animation.enter`  | Animation for the banner's appearance.                           | `banner.animation.enter = "slide-in"` |
| `banner.animation.exit`   | Animation for dismissing the banner.                             | `banner.animation.exit = "fade-out"`  |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "banner"
size = "50px"
fill = true
dismissible = true
animation = { enter = "slide-in", exit = "fade-out" }
content = [
    { type = "text", value = "Limited Time Offer!" },
    { type = "button", label = "Shop Now" }
]
```

---

### **Example GSS Implementation**
```toml
[banner]
size = "50px"
background = "linear-gradient(to right, #007BFF, #0056b3)"
margin = "10px"
border = "1px solid #CCC"
shadow = "2px 2px 5px rgba(0,0,0,0.5)"

[banner.animation]
enter = "slide-in"
exit = "fade-out"
```

---

### **Advanced Considerations**
1. **Dynamic Content Integration**:
   - Fetch dynamic content for banners from co-chains or APIs.

2. **Interactive States**:
   - Include hover effects and interactive elements, like buttons.

3. **Responsive Design**:
   - Ensure banners adapt to different screen sizes and orientations.

4. **Accessibility Enhancements**:
   - Ensure close buttons and interactive elements are keyboard navigable and screen reader compatible.

---

### **Conclusion**
The Banner Widget is a horizontally oriented container ideal for alerts, promotions, and headers. With support for dynamic content, interactive elements, and extensive styling options, it enhances user engagement while maintaining a clean, flexible design.

---

### **Window Widget**

The Window Widget simulates a window within the GSS environment. It is primarily used for development and design purposes but also serves as the foundational container for all M3L forms. Windows include interactive title bars, standard controls (close, minimize, maximize), and a defined area for embedding other widgets.

---

### **Core Features**
1. **Title Bar**:
   - Includes a title, and standard controls: close, minimize, and maximize buttons.

2. **Container Area**:
   - Provides a defined area for embedding any widget type.
   - Supports advanced layout configurations (e.g., grid, flex).

3. **Draggable and Resizable**:
   - Windows can be moved and resized for enhanced interactivity.

4. **Styling Options**:
   - Fully customizable title bar and container appearance.

5. **Interactive States**:
   - Supports `on_close`, `on_minimize`, `on_maximize`, `on_drag`, and `on_resize` events.

6. **Accessibility Enhancements**:
   - Includes keyboard shortcuts and screen reader-friendly descriptions for controls.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `title`             | Text to display in the window title bar.                            | `title = "Settings"`                   |
| `controls`          | Enables or disables title bar controls (close, minimize, maximize). | `controls = { close = true, minimize = true, maximize = true }` |
| `draggable`         | Allows the window to be moved by dragging the title bar.            | `draggable = true`                      |
| `resizable`         | Allows the window to be resized.                                     | `resizable = true`                      |
| `layout`            | Layout for widgets inside the window (`grid`, `flex`, etc.).        | `layout = "grid"`                      |
| `content`           | Array of widgets embedded in the window.                            | `content = [ { type = "text", value = "App Settings" } ]` |
| `border`            | Border styling for the window.                                       | `border = "1px solid #CCC"`            |
| `shadow`            | Shadow effect for the window.                                        | `shadow = "5px 5px 10px rgba(0,0,0,0.3)"` |
| `background`        | Background styling for the window.                                  | `background = "#FFF"`                  |
| `animation`         | Animations for opening, closing, or resizing the window.            | `animation = { open = "fade-in", close = "fade-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `window.border`           | Border style for the window.                                      | `window.border = "1px solid #CCC"`    |
| `window.shadow`           | Shadow effect for the window.                                    | `window.shadow = "5px 5px 10px rgba(0,0,0,0.3)"` |
| `window.background`       | Background styling for the window.                               | `window.background = "#FFF"`          |
| `window.titlebar.height`  | Height of the title bar.                                          | `window.titlebar.height = "30px"`     |
| `window.titlebar.color`   | Background color of the title bar.                               | `window.titlebar.color = "#007BFF"`   |
| `window.title.font`       | Font style for the title text.                                   | `window.title.font = "bold 14px Arial"` |
| `window.controls.style`   | Styling for the close, minimize, and maximize buttons.           | `window.controls.style = "flat"`      |
| `window.animation.open`   | Animation for opening the window.                                | `window.animation.open = "fade-in"`   |
| `window.animation.close`  | Animation for closing the window.                                | `window.animation.close = "fade-out"` |
| `window.animation.resize` | Animation for resizing the window.                               | `window.animation.resize = "smooth"`  |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "window"
title = "Settings"
controls = { close = true, minimize = true, maximize = true }
draggable = true
resizable = true
layout = "grid"
border = "1px solid #CCC"
shadow = "5px 5px 10px rgba(0,0,0,0.3)"
background = "#FFF"
animation = { open = "fade-in", close = "fade-out" }
content = [
    { type = "text", value = "Application Settings" },
    { type = "button", label = "Save Changes" }
]
```

---

### **Example GSS Implementation**
```toml
[window]
border = "1px solid #CCC"
shadow = "5px 5px 10px rgba(0,0,0,0.3)"
background = "#FFF"

[window.titlebar]
height = "30px"
color = "#007BFF"

[window.title]
font = "bold 14px Arial"

[window.controls]
style = "flat"

[window.animation]
open = "fade-in"
close = "fade-out"
resize = "smooth"
```

---

### **Advanced Considerations**
1. **Device-Specific Behavior**:
   - Adapt draggable and resizable functionality based on the input device (e.g., touch vs. mouse).

2. **Custom Controls**:
   - Allow developers to define custom actions or styles for title bar buttons.

3. **Dynamic Content Loading**:
   - Support loading additional widgets or data dynamically into the window.

4. **Nested Windows**:
   - Enable windows within windows for advanced UI scenarios like modal dialogs.

5. **Accessibility Enhancements**:
   - Ensure windows are keyboard navigable and screen reader compatible.

---

### **Conclusion**
The Window Widget is a foundational element for M3L forms, providing a structured and interactive container for other widgets. With support for draggable, resizable, and customizable options, it offers a flexible and visually consistent experience for developers and users alike.

---

### **Screenshot Widget**

The Screenshot Widget provides a flexible area for capturing and annotating screen content. It is designed for highlighting, freeform drawing, and sharing visual feedback. While primarily used for capturing on-screen elements, it can also serve as a tool for collaborative workflows and visual problem-solving.

---

### **Core Features**
1. **Screen Capture**:
   - Captures the visible area or a specific region of the screen.
   - Provides options for capturing entire frames or focused widgets.

2. **Annotation Tools**:
   - Support for freeform drawing, highlighting, and shape-based annotations.
   - Tools include brushes, highlighters, and text insertion.

3. **Undo/Redo Functionality**:
   - Tracks user actions to enable seamless undo and redo.

4. **Save and Share Options**:
   - Export annotations to formats like PNG or SVG.
   - Includes sharing functionality for collaborative workflows.

5. **Interactive States**:
   - Events like `on_capture`, `on_draw`, and `on_highlight` for enhanced interactivity.

6. **Styling Options**:
   - Customize background, brush styles, and annotation colors.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `capture_area`      | Defines the area to capture (full screen, region, or widget).         | `capture_area = "full_screen"`         |
| `annotation_tools`  | Enables tools like brushes and highlighters.                        | `annotation_tools = [ "brush", "highlighter", "text" ]` |
| `default_tool`      | Sets the default tool for annotations.                              | `default_tool = "brush"`               |
| `undo_redo`         | Enables undo and redo functionality.                                | `undo_redo = true`                       |
| `save_options`      | Defines export formats and sharing options.                         | `save_options = [ "PNG", "SVG" ]`      |
| `dimensions`        | Width and height of the capture area.                               | `dimensions = { width = "800px", height = "600px" }` |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `screenshot.background`   | Background color or image for the capture area.                  | `screenshot.background = "#FFF"`      |
| `screenshot.border`       | Border styling for the screenshot area.                         | `screenshot.border = "1px solid #CCC"` |
| `annotation.brush.color`  | Default color for the brush tool.                               | `annotation.brush.color = "#000"`      |
| `annotation.brush.size`   | Default size for the brush tool.                                | `annotation.brush.size = "5px"`        |
| `annotation.highlight.color` | Default color for the highlighter tool.                      | `annotation.highlight.color = "#FF0"`  |
| `annotation.text.font`    | Font style for text annotations.                                | `annotation.text.font = "14px Arial"`  |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "screenshot"
capture_area = "region"
annotation_tools = [ "brush", "highlighter", "text" ]
default_tool = "brush"
undo_redo = true
save_options = [ "PNG", "SVG" ]
dimensions = { width = "800px", height = "600px" }
```

---

### **Example GSS Implementation**
```toml
[screenshot]
background = "#FFF"
border = "1px solid #CCC"

[annotation.brush]
color = "#000"
size = "5px"

[annotation.highlight]
color = "#FF0"

[annotation.text]
font = "14px Arial"
```

---

### **Advanced Considerations**
1. **Dynamic Capture Areas**:
   - Allow users to dynamically resize or select specific regions for capture.

2. **Integration with Mimic**:
   - Save screenshots and annotations to Mimic for contextual analysis or feedback.

3. **Collaborative Sharing**:
   - Include real-time sharing options for collaborative workflows.

4. **Custom Annotations**:
   - Enable users to create and save custom annotation styles or presets.

5. **Accessibility Enhancements**:
   - Ensure screen reader compatibility and keyboard navigation for annotation tools.

---

### **Conclusion**
The Screenshot Widget bridges functionality and usability by combining screen capture with advanced annotation tools. With options for saving, sharing, and Mimic integration, it supports collaborative workflows and enhances visual communication for developers and end-users alike.

---

### **Carousel Widget**

The Carousel Widget is designed to cycle through various types of content, such as images, cards, or other widgets. It supports automatic and manual navigation, with hybrid options available for enhanced interactivity.

**Note**: In this context, "carousel" refers to a linear or looping content viewer, cycling through items horizontally or vertically. It does not represent a literal circular arrangement.

---

### **Core Features**
1. **Content Cycling**:
   - Automatically cycles through items on a timer.
   - Supports manual navigation via controls (e.g., `on_click` or `on_swipe`).

2. **Hybrid Mode**:
   - Allows both automatic and manual navigation simultaneously.

3. **Customizable Layout**:
   - Configurable direction (`horizontal`, `vertical`) and alignment.

4. **Interactive States**:
   - Events like `on_hover`, `on_click`, `on_swipe`, and `on_end`.

5. **Styling Options**:
   - Fully customizable indicators, controls, and animations.

6. **Dynamic Content Integration**:
   - Fetch content dynamically from external sources or co-chains.

7. **Pagination**:
   - Numbered dots or indicators show available content and the current position.

8. **Loading Animations**:
   - Display a loading animation while waiting for content to load.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `content`           | Array of widgets to display in the carousel.                        | `content = [ { type = "image", src = "@assets/img1.jpg" }, { type = "card", content = [...] } ]` |
| `direction`         | Direction of the carousel (`horizontal`, `vertical`).               | `direction = "horizontal"`             |
| `autoplay`          | Enables automatic cycling of content.                               | `autoplay = true`                        |
| `autoplay_interval` | Time in seconds between automatic transitions.                      | `autoplay_interval = 5`                  |
| `controls`          | Enables manual navigation controls.                                 | `controls = { prev = true, next = true }`|
| `indicators`        | Displays navigation indicators for content.                         | `indicators = true`                      |
| `animation`         | Defines animation style for transitions.                           | `animation = "slide"`                   |
| `loop`              | Enables looping through content.                                    | `loop = true`                            |
| `intent`            | High-level intent for navigation (`cycle`, `pause`, `reset`).       | `intent = "cycle"`                      |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `carousel.direction`      | Direction of the carousel.                                       | `carousel.direction = "horizontal"`    |
| `carousel.autoplay`       | Enables or disables autoplay.                                   | `carousel.autoplay = true`              |
| `carousel.indicators.style` | Styling for navigation indicators.                            | `carousel.indicators.style = "dots"`   |
| `carousel.controls.style` | Styling for navigation controls (e.g., arrows, buttons).        | `carousel.controls.style = "arrows"`   |
| `carousel.animation.type` | Type of animation for transitions.                              | `carousel.animation.type = "fade"`     |
| `carousel.animation.speed`| Speed of the animation.                                          | `carousel.animation.speed = "0.5s"`    |
| `carousel.loading.type`   | Style of loading animation (e.g., spinner, shimmer).            | `carousel.loading.type = "spinner"`    |
| `carousel.loading.color`  | Color of the loading animation.                                 | `carousel.loading.color = "#007BFF"`  |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "carousel"
direction = "horizontal"
autoplay = true
autoplay_interval = 5
intent = "cycle"
loop = true
content = [
    { type = "image", src = "@assets/img1.jpg" },
    { type = "image", src = "@assets/img2.jpg" },
    { type = "card", content = [ { type = "text", value = "Product Name" }, { type = "button", label = "Buy Now" } ] }
]
```

---

### **Example GSS Implementation**
```toml
[carousel]
direction = "horizontal"
autoplay = true

[carousel.indicators]
style = "dots"

[carousel.controls]
style = "arrows"

[carousel.animation]
type = "slide"
speed = "0.5s"

[carousel.loading]
type = "spinner"
color = "#007BFF"
```

---

### **Advanced Considerations**
1. **Dynamic Content Loading**:
   - Support for fetching content dynamically from co-chains or APIs.

2. **Custom Transitions**:
   - Allow developers to define custom animations for transitions.

3. **Device-Specific Behavior**:
   - Optimize interactions for touch, mouse, and controller inputs.

4. **Accessibility Enhancements**:
   - Ensure indicators and controls are keyboard navigable and screen reader compatible.

5. **Loading States**:
   - Display loading animations when fetching content dynamically.

---

### **Conclusion**
The Carousel Widget is a powerful tool for cycling through diverse content, with support for automatic and manual navigation, advanced animations, and dynamic integrations. Its flexibility ensures seamless integration into various applications and use cases.

---

### **Break Widget**

The Break Widget is a simple visual divider used to separate pieces of content on a screen. Breaks can be vertical or horizontal and styled in various ways to suit the design, including lines, background colors, or custom visual elements.

---

### **Core Features**
1. **Orientation**:
   - Supports both horizontal and vertical orientations.

2. **Customizable Styling**:
   - Fully customizable appearance, including colors, thickness, and patterns.

3. **Dynamic Sizing**:
   - Automatically adjusts to fit within its parent container or specified dimensions.

4. **Interactive States**:
   - Optional hover effects or animations for enhanced visual appeal.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `orientation`       | Specifies the direction of the break (`horizontal`, `vertical`).      | `orientation = "horizontal"`           |
| `size`              | Defines the thickness or width of the break.                         | `size = "2px"`                          |
| `color`             | Color of the break line or background.                               | `color = "#CCC"`                        |
| `margin`            | Spacing around the break.                                            | `margin = "10px 0"`                     |
| `pattern`           | Defines a pattern for the break line (e.g., solid, dashed, dotted).  | `pattern = "dashed"`                    |
| `animation`         | Optional animations for appearance or hover effects.                | `animation = { enter = "fade-in" }`     |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `break.orientation`       | Orientation of the break.                                        | `break.orientation = "horizontal"`     |
| `break.size`              | Thickness or width of the break.                                 | `break.size = "2px"`                   |
| `break.color`             | Color of the break line or background.                           | `break.color = "#CCC"`                 |
| `break.margin`            | Margin around the break.                                          | `break.margin = "10px 0"`              |
| `break.pattern`           | Pattern of the break line.                                       | `break.pattern = "dashed"`             |
| `break.animation.enter`   | Animation for the break's appearance.                            | `break.animation.enter = "fade-in"`    |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "break"
orientation = "horizontal"
size = "2px"
color = "#CCC"
margin = "10px 0"
pattern = "dashed"
animation = { enter = "fade-in" }
```

---

### **Example GSS Implementation**
```toml
[break]
orientation = "horizontal"
size = "2px"
color = "#CCC"
margin = "10px 0"
pattern = "dashed"

[break.animation]
enter = "fade-in"
```

---

### **Advanced Considerations**
1. **Dynamic Sizing**:
   - Allow breaks to dynamically adjust their length or height based on the parent container.

2. **Interactive States**:
   - Optional hover effects or animations for breaks.

3. **Device-Specific Styling**:
   - Allow different styles or sizes based on device type.

---

### **Conclusion**
The Break Widget is a lightweight and flexible tool for visually organizing content. With customizable orientations, patterns, and animations, it enhances the clarity and visual appeal of user interfaces.

---

### **Toolbar Widget**

The Toolbar Widget provides a collection of buttons, icons, and menus for interacting with and manipulating content within an application. It is ideal for applications requiring a robust toolset for user actions in the workspace. The Toolbar is designed to integrate with functions on UndChain and supports customization for specific applications.

---

### **Core Features**
1. **Toolset Organization**:
   - Houses multiple buttons or tools grouped logically.
   - Supports separators and nested menus for better organization.

2. **Standard Items**:
   - Predefined actions for commonly used functionalities:
     - **File Menu**: `New`, `Open`, `Save`, `Save As`, `Export`, `Close`
     - **Edit Menu**: `Undo`, `Redo`, `Cut`, `Copy`, `Paste`, `Delete`
     - **View Menu**: `Zoom In`, `Zoom Out`, `Fit to Screen`, `Full Screen`
     - **Help Menu**: `About`, `Documentation`, `Report Issue`
     - **Controls**: `Start`, `Stop`, `Add`, `Delete`
   - Comes with default monochrome icons that can be styled by GSS designers.

3. **Custom Actions**:
   - Developers can define custom buttons and map them to specific application functions.

4. **Interactive States**:
   - Supports `on_click`, `on_hover`, and `on_press` events for each tool.

5. **Dynamic Updates**:
   - Tools and menus can dynamically update based on the state of the application.

6. **Positioning**:
   - Toolbars can be placed at the `top`, `left`, `right`, or `bottom` of the application.

7. **Separator and Grouping**:
   - Includes support for separators to visually divide tool groups.
   - Groups are defined in M3L, each with a name, and styled in GSS.

8. **Styling Options**:
   - Fully customizable icons, button layouts, and interaction effects.

---

### **Proposed Fields**
| **Field**           | **Description**                                                       | **Example**                              |
|---------------------|-----------------------------------------------------------------------|------------------------------------------|
| `tools`             | Array of tool groups in the toolbar. Each group includes tools and a name. | `tools = [ { group_name = "File", tools = [...] } ]` |
| `orientation`       | Direction of the toolbar (`horizontal`, `vertical`).                | `orientation = "horizontal"`           |
| `position`          | Placement of the toolbar within the application.                    | `position = "top"`                      |
| `standard_icons`    | Enables predefined icons for standard actions.                      | `standard_icons = true`                  |
| `custom_icons`      | Defines custom icons for application-specific tools.                | `custom_icons = [ { name = "Offset", icon = "@assets/offset.svg" } ]` |
| `animation`         | Optional animations for tool appearance or interaction.             | `animation = { hover = "highlight", click = "bounce" }` |
| `dynamic`           | Allows tools to update dynamically based on application state.      | `dynamic = true`                         |
| `separator`         | Adds visual separators between groups of tools.                     | `separator = true`                       |

---

### **GSS Styling Parameters**
| **Parameter**             | **Description**                                                   | **Example**                              |
|---------------------------|-------------------------------------------------------------------|------------------------------------------|
| `toolbar.orientation`     | Orientation of the toolbar.                                      | `toolbar.orientation = "horizontal"`   |
| `toolbar.position`        | Placement of the toolbar within the application.                | `toolbar.position = "top"`             |
| `toolbar.background`      | Background styling for the toolbar.                             | `toolbar.background = "#FFF"`         |
| `toolbar.border`          | Border style for the toolbar.                                    | `toolbar.border = "1px solid #CCC"`   |
| `toolbar.icon.color`      | Default color for monochrome icons.                              | `toolbar.icon.color = "#000"`         |
| `toolbar.icon.size`       | Size of the icons.                                               | `toolbar.icon.size = "24px"`          |
| `toolbar.animation.hover` | Animation for tool hover effects.                                | `toolbar.animation.hover = "highlight"`|
| `toolbar.animation.click` | Animation for tool click effects.                                | `toolbar.animation.click = "bounce"`  |
| `toolbar.separator.style` | Styling for separators between tool groups.                     | `toolbar.separator.style = "solid"`   |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "toolbar"
orientation = "horizontal"
position = "top"
standard_icons = true
custom_icons = [ { name = "Offset", icon = "@assets/offset.svg" } ]
dynamic = true
separator = true
tools = [
    {
        group_name = "File",
        tools = [
            { type = "button", label = "Open", intent = "@UndChain.SESSION_ID.file.open" },
            { type = "button", label = "Save", intent = "@UndChain.SESSION_ID.file.save" }
        ]
    },
    {
        group_name = "Edit",
        tools = [
            { type = "button", label = "Undo", intent = "@UndChain.SESSION_ID.edit.undo" },
            { type = "button", label = "Redo", intent = "@UndChain.SESSION_ID.edit.redo" }
        ]
    },
    {
        group_name = "Help",
        tools = [
            { type = "button", label = "About", intent = "@UndChain.SESSION_ID.help.about" }
        ]
    }
]
```

---

### **Example GSS Implementation**
```toml
[toolbar]
orientation = "horizontal"
position = "top"
background = "#FFF"
border = "1px solid #CCC"

[toolbar.icon]
color = "#000"
size = "24px"

[toolbar.animation]
hover = "highlight"
click = "bounce"

[toolbar.separator]
style = "solid"
```

---

### **Advanced Considerations**
1. **Dynamic Updates**:
   - Allow tools to enable or disable based on application state (e.g., disabling `undo` if no actions can be undone).

2. **Custom Tool Groups**:
   - Enable developers to create logical groups of tools for specific workflows.

3. **Device-Specific Behavior**:
   - Adapt toolbar layout and interactions for touch, mouse, and controller inputs.

4. **Accessibility Enhancements**:
   - Ensure all tools are keyboard navigable and screen reader compatible.

---

### **Conclusion**
The Toolbar Widget is a powerful interface element for applications requiring a rich toolset. With support for standard and custom tools, dynamic updates, separators, flexible positioning, and extensive styling options, it offers developers a versatile and user-friendly solution for creating complex applications.

---

### **Toolbar Widget**

The Toolbar Widget provides a collection of buttons, icons, and menus for interacting with and manipulating content within an application. It is ideal for applications requiring a robust toolset for user actions in the workspace. The Toolbar is designed to integrate with functions on UndChain and supports customization for specific applications.

---

### **Core Features**

1. **Toolset Organization**:

   - Houses multiple buttons or tools grouped logically.
   - Supports separators and nested menus for better organization.

2. **Standard Items**:

   - Predefined actions for commonly used functionalities:
     - **File Menu**: `New`, `Open`, `Save`, `Save As`, `Export`, `Close`
     - **Edit Menu**: `Undo`, `Redo`, `Cut`, `Copy`, `Paste`, `Delete`
     - **View Menu**: `Zoom In`, `Zoom Out`, `Fit to Screen`, `Full Screen`
     - **Help Menu**: `About`, `Documentation`, `Report Issue`
     - **Controls**: `Start`, `Stop`, `Add`, `Delete`
   - Comes with default monochrome icons that can be styled by GSS designers.

3. **Custom Actions**:

   - Developers can define custom buttons and map them to specific application functions.

4. **Interactive States**:

   - Supports `on_click`, `on_hover`, and `on_press` events for each tool.

5. **Dynamic Updates**:

   - Tools and menus can dynamically update based on the state of the application.

6. **Positioning**:

   - Toolbars can be placed at the `top`, `left`, `right`, or `bottom` of the application.

7. **Separator and Grouping**:

   - Separators are implicitly styled in GSS and applied when new groups are defined.
   - Menus are defined in M3L with `menu_name`, and tool groups are nested within the menus.

8. **Styling Options**:

   - Fully customizable icons, button layouts, and interaction effects.
   - GSS designers can define unique styles based on the toolbar's position.

---

### **M3L Fields**

| **Field**        | **Description**                                                           | **Example**                                                           |
| ---------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `tools`          | Array of menus in the toolbar. Each menu includes a name and tool groups. | `tools = [ { menu_name = "File", groups = [...] } ]`                  |
| `orientation`    | Direction of the toolbar (`horizontal`, `vertical`).                      | `orientation = "horizontal"`                                          |
| `position`       | Placement of the toolbar within the application.                          | `position = "top"`                                                    |
| `animation`      | Optional animations for tool appearance or interaction.                   | `animation = { hover = "highlight", click = "bounce" }`               |
| `dynamic`        | Allows tools to update dynamically based on application state.            | `dynamic = true`                                                      |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                                      | **Example**                                   |
| ------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| `toolbar.orientation`     | Orientation of the toolbar.                          | `toolbar.orientation = "horizontal"`          |
| `toolbar.position`        | Placement of the toolbar within the application.     | `toolbar.position = "top"`                    |
| `toolbar.background`      | Background styling for the toolbar.                  | `toolbar.background = "#FFF"`                 |
| `toolbar.border`          | Border style for the toolbar.                        | `toolbar.border = "1px solid #CCC"`           |
| `toolbar.icon.color`      | Default color for monochrome icons.                  | `toolbar.icon.color = "#000"`                 |
| `toolbar.icon.size`       | Size of the icons.                                   | `toolbar.icon.size = "24px"`                  |
| `toolbar.animation.hover` | Animation for tool hover effects.                    | `toolbar.animation.hover = "highlight"`       |
| `toolbar.animation.click` | Animation for tool click effects.                    | `toolbar.animation.click = "bounce"`          |
| `toolbar.position.top`    | Custom styles for toolbars positioned at the top.    | `toolbar.position.top.background = "#EEE"`    |
| `toolbar.position.left`   | Custom styles for toolbars positioned on the left.   | `toolbar.position.left.background = "#DDD"`   |
| `toolbar.position.right`  | Custom styles for toolbars positioned on the right.  | `toolbar.position.right.background = "#CCC"`  |
| `toolbar.position.bottom` | Custom styles for toolbars positioned at the bottom. | `toolbar.position.bottom.background = "#BBB"` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "toolbar"
orientation = "horizontal"
position = "top"
dynamic = true
tools = [
    {
        menu_name = "File",
        groups = [
            {
                group_name = "File Management",
                tools = [
                    { type = "button", label = "Open", intent = "@UndChain.SESSION_ID.file.open" },
                    { type = "button", label = "Save", intent = "@UndChain.SESSION_ID.file.save" }
                ]
            }
        ]
    },
    {
        menu_name = "Edit",
        groups = [
            {
                group_name = "Editing Tools",
                tools = [
                    { type = "button", label = "Undo", intent = "@UndChain.SESSION_ID.edit.undo" },
                    { type = "button", label = "Redo", intent = "@UndChain.SESSION_ID.edit.redo" },
                    { type = "button", label = "Offset", intent = "@UndChain.SESSION_ID.edit.offset" }
                ]
            }
        ]
    },
    {
        menu_name = "Help",
        groups = [
            {
                group_name = "Assistance",
                tools = [
                    { type = "button", label = "About", intent = "@UndChain.SESSION_ID.help.about" }
                ]
            }
        ]
    }
]
```

---

### **Example GSS Implementation**

```toml
[toolbar]
orientation = "horizontal"
position = "top"
background = "#FFF"
border = "1px solid #CCC"

[toolbar.icon]
color = "#000"
size = "24px"

[toolbar.animation]
hover = "highlight"
click = "bounce"

[toolbar.position.top]
background = "#EEE"

[toolbar.position.left]
background = "#DDD"

[toolbar.position.right]
background = "#CCC"

[toolbar.position.bottom]
background = "#BBB"
```

---

### **Advanced Considerations**

1. **Dynamic Updates**:

   - Allow tools to enable or disable based on application state (e.g., disabling `undo` if no actions can be undone).

2. **Custom Tool Groups**:

   - Enable developers to create logical groups of tools for specific workflows.

3. **Device-Specific Behavior**:

   - Adapt toolbar layout and interactions for touch, mouse, and controller inputs.

4. **Accessibility Enhancements**:

   - Ensure all tools are keyboard navigable and screen reader compatible.

---

### **Conclusion**

The Toolbar Widget is a powerful interface element for applications requiring a rich toolset. With support for standard and custom tools, dynamic updates, separators, flexible positioning, and extensive styling options, it offers developers a versatile and user-friendly solution for creating complex applications.

---

### **Floating Menu Widget**

The Floating Menu Widget provides a context-sensitive menu that activates based on user interactions, such as right-clicking or hovering over an element. This compact and focused menu is designed to offer quick access to the most relevant actions for the selected context.

---

### **Core Features**

1. **Context-Sensitive Activation**:

   - Activated by specific intents such as `add_context` (e.g., right-click, long press, hover).
   - Automatically adjusts its options based on the context of the interaction.

2. **Compact Design**:

   - Focuses on the most commonly used actions for the context.
   - Optimized for minimal screen real estate.

3. **Dynamic Content**:

   - Updates dynamically based on the state of the application or widget.
   - Fetches relevant actions from co-chains or pre-defined menus.

4. **Styling Options**:

   - Fully customizable size, background, icons, and animations.
   - Positioning is determined by the GSS file and can be relative to the event trigger or set as an absolute position.

5. **Interactive States**:

   - Supports `on_hover`, `on_click`, and `on_exit` events for each menu item.

6. **Accessibility Enhancements**:

   - Keyboard navigable and screen reader compatible.

---

### **M3L Fields**

| **Field**        | **Description**                                                           | **Example**                                                           |
| ---------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `menu_items`     | Array of items in the floating menu. Each item includes a label and intent. | `menu_items = [ { label = "Copy", intent = "@UndChain.SESSION_ID.edit.copy" }, { label = "Paste", intent = "@UndChain.SESSION_ID.edit.paste" } ]` |
| `dynamic`        | Allows menu items to update dynamically based on the context.             | `dynamic = true`                                                      |
| `animation`      | Optional animations for menu appearance or interaction.                   | `animation = { enter = "fade-in", exit = "fade-out" }`               |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                                      | **Example**                                   |
| ------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| `floating_menu.size`      | Dimensions of the floating menu.                     | `floating_menu.size = "150px x 200px"`        |
| `floating_menu.background`| Background styling for the menu.                     | `floating_menu.background = "#FFF"`          |
| `floating_menu.border`    | Border style for the menu.                           | `floating_menu.border = "1px solid #CCC"`    |
| `floating_menu.icon.color`| Default color for menu icons.                        | `floating_menu.icon.color = "#000"`          |
| `floating_menu.animation.enter` | Animation for menu appearance.                  | `floating_menu.animation.enter = "fade-in"`  |
| `floating_menu.animation.exit`  | Animation for menu dismissal.                   | `floating_menu.animation.exit = "fade-out"` |
| `floating_menu.position.relative_to_trigger` | Places the menu relative to the event trigger position. | `floating_menu.position.relative_to_trigger = true` |
| `floating_menu.position.absolute` | Sets an absolute position for the menu.        | `floating_menu.position.absolute = "100px, 200px"` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "floating_menu"
dynamic = true
animation = { enter = "fade-in", exit = "fade-out" }
menu_items = [
    { label = "Copy", intent = "@UndChain.SESSION_ID.edit.copy" },
    { label = "Paste", intent = "@UndChain.SESSION_ID.edit.paste" },
    { label = "Delete", intent = "@UndChain.SESSION_ID.edit.delete" }
]
```

---

### **Example GSS Implementation**

```toml
[floating_menu]
size = "150px x 200px"
background = "#FFF"
border = "1px solid #CCC"

[floating_menu.icon]
color = "#000"

[floating_menu.animation]
enter = "fade-in"
exit = "fade-out"

[floating_menu.position]
relative_to_trigger = true
absolute = "100px, 200px"
```

---

### **Advanced Considerations**

1. **Dynamic Updates**:

   - Automatically adjust menu options based on user context and co-chain responses.

2. **Custom Positioning**:

   - Support for positioning relative to the triggering element or as an absolute value defined by the GSS designer.

3. **Device-Specific Behavior**:

   - Adapt menu interactions for touch, mouse, and controller inputs.

4. **Accessibility Enhancements**:

   - Ensure all menu items are keyboard navigable and screen reader compatible.

---

### **Conclusion**

The Floating Menu Widget is a lightweight and flexible context-sensitive tool, offering quick access to relevant actions. Its compact design, dynamic content, and extensive customization options make it an essential feature for enhancing user interactions in applications.

---

### **Context Menu Widget**

The Context Menu Widget provides a traditional right-click menu with options tailored to the selected element or context. Unlike the Floating Menu, which is designed for compact, dynamic menus, the Context Menu focuses on delivering a more extensive list of options typically used for file management, text editing, and similar actions. Notably, the Context Menu can only contain text elements—icons are not supported.

Developers should note that the `---` label is reserved specifically for defining breaks within the `menu_items` array.

---

### **Core Features**

1. **Standard Context Options**:

   - Includes common options such as `Copy`, `Paste`, `Cut`, `Rename`, and `Delete`.

2. **Contextual Actions**:

   - Updates dynamically based on the selected element or context.

3. **Expandable Sub-Menus**:

   - Supports nested menus for additional actions.

4. **Styling Options**:

   - Fully customizable size, background, and animations.
   - Positioning is determined by the GSS file and can be relative to the event trigger or set as an absolute position.

5. **Breaks**:

   - Developers can define logical breaks directly within the `menu_items` array in the M3L file for better organization.
   - GSS defines how these breaks are styled.

6. **Interactive States**:

   - Supports `on_hover`, `on_click`, and `on_exit` events for each menu item.

7. **Accessibility Enhancements**:

   - Keyboard navigable and screen reader compatible.

---

### **M3L Fields**

| **Field**    | **Description**                                                                    | **Example**                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `menu_items` | Array of items in the context menu. Items can include labels, intents, and breaks. | `menu_items = [ { label = "Copy", intent = "@UndChain.SESSION_ID.edit.copy" }, { label = "---" }, { label = "Paste", intent = "@UndChain.SESSION_ID.edit.paste" } ]` |
| `animation`  | Optional animations for menu appearance or interaction.                            | `animation = { enter = "fade-in", exit = "fade-out" }`                                                                                                               |

---

### **GSS Styling Parameters**

| **Parameter**                               | **Description**                                         | **Example**                                        |
| ------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- |
| `context_menu.size`                         | Dimensions of the context menu.                         | `context_menu.size = "200px x 300px"`              |
| `context_menu.background`                   | Background styling for the menu.                        | `context_menu.background = "#FFF"`                 |
| `context_menu.border`                       | Border style for the menu.                              | `context_menu.border = "1px solid #CCC"`           |
| `context_menu.animation.enter`              | Animation for menu appearance.                          | `context_menu.animation.enter = "fade-in"`         |
| `context_menu.animation.exit`               | Animation for menu dismissal.                           | `context_menu.animation.exit = "fade-out"`         |
| `context_menu.position.relative_to_trigger` | Places the menu relative to the event trigger position. | `context_menu.position.relative_to_trigger = true` |
| `context_menu.position.absolute`            | Sets an absolute position for the menu.                 | `context_menu.position.absolute = "100px, 200px"`  |
| `context_menu.break.style`                  | Styling for breaks between menu items.                  | `context_menu.break.style = "dashed"`              |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "context_menu"
animation = { enter = "fade-in", exit = "fade-out" }
menu_items = [
    { label = "Copy", intent = "@UndChain.SESSION_ID.edit.copy" },
    { label = "---" },
    { label = "Paste", intent = "@UndChain.SESSION_ID.edit.paste" },
    { label = "Rename", intent = "@UndChain.SESSION_ID.file.rename" },
    { label = "Delete", intent = "@UndChain.SESSION_ID.file.delete" }
]
```

---

### **Example GSS Implementation**

```toml
[context_menu]
size = "200px x 300px"
background = "#FFF"
border = "1px solid #CCC"

[context_menu.animation]
enter = "fade-in"
exit = "fade-out"

[context_menu.position]
relative_to_trigger = true
position = "100px, 200px"

[context_menu.break]
style = "dashed"
color = "#CCC"
margin = "5px"
```

---

### **Advanced Considerations**

1. **Dynamic Updates**:

   - Automatically adjust menu options based on user context and co-chain responses.

2. **Expandable Sub-Menus**:

   - Include support for nested sub-menus for advanced actions.

3. **Breaks for Organization**:

   - Developers can define logical breaks in the menu directly within the `menu_items` array for better grouping of options.

4. **Device-Specific Behavior**:

   - Adapt menu interactions for touch, mouse, and controller inputs.

5. **Accessibility Enhancements**:

   - Ensure all menu items are keyboard navigable and screen reader compatible.

---

### **Conclusion**

The Context Menu Widget is a versatile tool for delivering traditional right-click menu functionality. Its support for nested menus, dynamic updates, logical breaks, and extensive customization options ensures it meets the needs of a wide range of applications.

---

### **Graph Widget**

The Graph Widget generates visual representations of data, offering a variety of chart types and interactive features. It supports dynamic data sources, customizable styling, and advanced interactions for developers and users alike.

---

### **Core Features**

1. **Data Input**:
   - Accepts multiple input formats, including static arrays, CSV files, or links to UndChain co-chains (e.g., SQeeL).
   - Handles structured (e.g., time-series) and unstructured data (e.g., scatter plots).

2. **Graph Types**:
   - Bar charts (vertical and horizontal).
   - Line graphs (smooth or stepped).
   - Scatter plots.
   - Pie charts.
   - Area charts.

3. **Interactive Features**:
   - Zoom and pan for larger datasets.
   - Highlight data points on hover.
   - Clickable data points with intents (e.g., `on_click` to display more info).
   - Editable data if connected to a writable source.

4. **Styling**:
   - Controlled through GSS for colors, line styles, marker shapes, animations, and legend customization.
   - Supports frosted or transparent backgrounds.

5. **Axes and Grid**:
   - Customizable labels, ticks, units, and gridline styles.
   - Adjustable granularity for X and Y axes, with dynamic options to automatically adjust based on data density.

6. **Tooltips**:
   - Provides contextual information for hovered data points.
   - Fully customizable appearance.

7. **Performance Optimization**:
   - Includes a `sample_rate` parameter to manage large datasets by rendering every nth data point.

8. **Advanced Interactions**:
   - Export graphs as images or data files (e.g., CSV, JSON).
   - Annotate specific points or ranges.
   - Support for dual axes for datasets with different scales.

9. **Accessibility**:
   - Data summaries for screen readers.
   - Keyboard navigation.

---

### **M3L Fields**

| **Field**        | **Description**                                  | **Example**                                              |
| ---------------- | ------------------------------------------------ | -------------------------------------------------------- |
| `data_source`    | Defines the source of the data.                  | `data_source = "@SQeeL://path/to/data.csv"`             |
| `graph_type`     | Type of graph to generate.                       | `graph_type = "line"`                                   |
| `editable`       | Allows users to modify data points.              | `editable = true`                                        |
| `intents`        | Array of interactions for data points.           | `intents = [ "on_click", "on_hover" ]`                 |
| `animation`      | Animations for graph rendering or transitions.   | `animation = { enter = "fade-in", update = "bounce" }`  |
| `axes`           | Axis customization options.                      | `axes = { x_label = "Time", y_label = "Value", x_granularity = 5, y_granularity = 10, dynamic_granularity = true }` |
| `tooltip`        | Enables tooltips for data points.                | `tooltip = true`                                         |
| `legend`         | Enables the graph legend.                        | `legend = true`                                          |
| `sample_rate`    | Determines the rate at which data points are rendered. | `sample_rate = 10`                                 |

---

### **GSS Styling Parameters**

| **Parameter**           | **Description**                          | **Example**                              |
| ----------------------- | ---------------------------------------- | ---------------------------------------- |
| `graph.background`      | Background color for the graph area.     | `graph.background = "rgba(255, 255, 255, 0.7)"` |
| `graph.legend`          | Customization for the legend.            | `graph.legend.position = "bottom-right"` |
| `graph.line.color`      | Line color for line graphs.              | `graph.line.color = "#00F"`             |
| `graph.marker.shape`    | Shape of data point markers.             | `graph.marker.shape = "circle"`         |
| `graph.grid.style`      | Gridline style and visibility.           | `graph.grid.style = "dotted"`           |
| `graph.grid.granularity`| Granularity of major and minor gridlines.| `graph.grid.granularity = { major = 5, minor = 1 }` |
| `graph.tooltip`         | Tooltip styling for hovered data points. | `graph.tooltip.background = "#333"`    |
| `graph.fill`            | Fill options for area and bar charts.    | `graph.fill.type = "gradient"`         |

---

### **Example M3L Implementation**

#### Line Chart Example

```toml
[[layout.container.content]]
type = "graph"
data_source = "@SQeeL://Auction_House/sales_data.csv"
graph_type = "line"
editable = true
animation = { enter = "fade-in", update = "bounce" }
axes = { 
    x_label = "Time", 
    y_label = "Sales", 
    x_granularity = 5, 
    y_granularity = 10, 
    dynamic_granularity = true 
}
tooltip = true
legend = true
sample_rate = 10
```

#### Pie Chart Example

```toml
[[layout.container.content]]
type = "graph"
data_source = "@SQeeL://Auction_House/category_sales.csv"
graph_type = "pie"
editable = false
animation = { enter = "fade-in", update = "spin" }
legend = true
tooltip = true
```

---

### **Example GSS Implementation**

```toml
[graph]
background = "rgba(255, 255, 255, 0.7)"
effect = "frosted"

[graph.legend]
position = "bottom-right"
icon = { shape = "custom", src = "@assets/icons/custom_icon.svg" }

[graph.line]
color = "#00F"
width = "2px"

[graph.marker]
shape = "circle"
size = "5px"

[graph.grid]
style = "dotted"
major.color = "#AAA"
minor.color = "#CCC"

[graph.tooltip]
background = "#333"
color = "#FFF"
font-size = "12px"
border-radius = "4px"
padding = "5px"

[graph.fill]
type = "gradient"
gradient = { start = "#FF0000", end = "#0000FF", direction = "vertical" }
```

---

### **Advanced Considerations**

1. **Dynamic Updates**:
   - Allow real-time updates from co-chains.
   - Support partial updates for efficiency.

2. **Data Validation**:
   - Validate input data structure to prevent errors.

3. **Annotations**:
   - Allow users or developers to mark specific points or ranges on the graph.

4. **Multiple Axes**:
   - Support dual axes for datasets with different scales.

5. **Performance Optimization**:
   - Implement `sample_rate` to handle large datasets gracefully.

6. **Dynamic Granularity**:
   - Automatically adjust axis granularity based on the density of the data.

---

### **Conclusion**

The Graph Widget combines rich customization, dynamic interactivity, and extensive styling options to deliver powerful data visualization. By incorporating features like tooltips, legends, grid granularity, and sample rate handling, it meets the needs of diverse applications while ensuring accessibility and performance.

---

### **Candle Chart Widget**

The Candle Chart Widget is a specialized visualization tool designed for financial and trading applications. It provides candlestick representations of market data along with support for additional technical indicators like MACD, RSI, stochastic RSI, SMA, and volume overlays, including VRVP (Visible Range Volume Profile). The widget also supports various candlestick types, such as Heikin-Ashi.

---

### **Core Features**

1. **Candlestick Representation**:
   - Visualizes open, high, low, and close (OHLC) values for each time period.
   - Supports multiple candlestick types (e.g., traditional, Heikin-Ashi).
   - Color-coding for bullish and bearish candles (e.g., green for up, red for down).

2. **Technical Indicators**:
   - Built-in support for:
     - **MACD**: Moving Average Convergence Divergence.
     - **RSI**: Relative Strength Index.
     - **Stochastic RSI**: Combines RSI and stochastic oscillators.
     - **SMA**: Smooth Moving Average.
     - **Volume**: Overlay or separate chart.
     - **VRVP**: Displays volume profile as horizontal bars for specific ranges, distinguishing buy and sell volumes with different colors.
   - Developers can define custom indicators as additional chart elements.

3. **Drawing Tools**:
   - Add trend lines, support/resistance levels, labels, dots, or area bars.
   - Fully interactive, allowing users to adjust or remove elements dynamically.

4. **Zoom and Pan**:
   - Enables detailed examination of specific periods.
   - Smooth transitions for zoom and pan actions.

5. **Data Input**:
   - Accepts data from CSV files, JSON, or links to UndChain co-chains.

6. **Interactivity**:
   - Hover over candlesticks or indicators to show detailed tooltips.
   - Click events for additional actions (e.g., marking trades).

7. **Custom Overlays**:
   - Add trend lines, support/resistance levels, or annotations.

8. **Accessibility**:
   - Data summaries for screen readers.
   - Keyboard navigation for scrolling through time periods.

---

### **Custom Charting with the Graph Widget**

Developers can create their own charting tools using the Graph Widget as a foundation. By defining custom visualizations and linking data sources, they can build highly specialized charts for unique applications.

#### Key Features:
- Use `graph_type = "custom"` for bespoke visualizations.
- Accept any data input format (e.g., CSV, JSON, co-chains).
- Define unique formulas and visualizations.
- Reuse Graph Widget styling and interactions for consistency.

#### Example M3L Implementation for a Custom Chart:

```toml
[[layout.container.content]]
type = "graph"
data_source = "@SQeeL://CustomApp/data_stream.json"
graph_type = "custom"
custom_definitions = [
    { name = "Custom Line", formula = "data.y * 2", color = "#FF5733" },
    { name = "Custom Area", formula = "data.y / 2", color = "#33FF57", fill = true }
]
x_axis = { label = "Time", dynamic_granularity = true }
y_axis = { label = "Custom Metric", min = 0, max = 100 }
tooltip = true
legend = true
animation = { enter = "fade-in", update = "grow" }
```

#### Example GSS for Custom Charts:

```toml
[graph]
background = "#FFF"

[graph.line]
color = "#FF5733"
width = "2px"

[graph.area]
color = "#33FF57"
fill = "rgba(51, 255, 87, 0.5)"

[graph.tooltip]
background = "#000"
color = "#FFF"
font-size = "12px"
border-radius = "4px"
padding = "5px"

[graph.legend]
position = "bottom-right"
```

---

### **M3L Fields**

| **Field**        | **Description**                                  | **Example**                                              |
| ---------------- | ------------------------------------------------ | -------------------------------------------------------- |
| `data_source`    | Defines the source of the data.                  | `data_source = "@SQeeL://path/to/ohlc_data.csv"`        |
| `indicators`     | Array of indicators to display with the chart.   | `indicators = [ "MACD", "RSI", "Stochastic RSI", "SMA", "VRVP", "Volume" ]` |
| `overlay_lines`  | Defines custom overlays like trend lines.        | `overlay_lines = [ { name = "Support", points = [...] } ]` |
| `drawing_tools`  | Enables user-defined drawings like lines or labels. | `drawing_tools = true`                                  |
| `candlestick_type` | Specifies the type of candlestick to display.   | `candlestick_type = "Heikin-Ashi"`                      |
| `intents`        | Array of interactions for candles or indicators. | `intents = [ "on_click", "on_hover" ]`                 |
| `animation`      | Animations for rendering or updates.             | `animation = { enter = "fade-in", update = "grow" }`   |
| `tooltip`        | Enables tooltips for candles and indicators.     | `tooltip = true`                                         |

---

### **GSS Styling Parameters**

| **Parameter**           | **Description**                          | **Example**                              |
| ----------------------- | ---------------------------------------- | ---------------------------------------- |
| `candle_chart.background` | Background color for the chart area.     | `candle_chart.background = "#000"`       |
| `candle_chart.candle.up_color` | Color for bullish candles.          | `candle_chart.candle.up_color = "#0F0"`  |
| `candle_chart.candle.down_color` | Color for bearish candles.        | `candle_chart.candle.down_color = "#F00"` |
| `candle_chart.grid.style` | Gridline style and visibility.           | `candle_chart.grid.style = "dotted"`     |
| `candle_chart.legend`   | Customization for the legend.            | `candle_chart.legend.position = "top-left"` |
| `candle_chart.indicator.line.color` | Line color for indicators.     | `candle_chart.indicator.line.color = "#00F"` |
| `candle_chart.tooltip`  | Tooltip styling for hovered data.        | `candle_chart.tooltip.background = "#333"` |
| `candle_chart.vrvp`     | Styling for VRVP bars, with buy/sell differentiation. | `candle_chart.vrvp.buy_color = "#0A0", vrvp.sell_color = "#A00"` |

---

### **Advanced Considerations**

1. **Dynamic Updates**:
   - Support real-time updates from co-chains.
   - Allow partial updates to avoid re-rendering the entire chart.

2. **Custom Indicators**:
   - Enable developers to define and add their own indicators beyond MACD, RSI, Stochastic RSI, SMA, VRVP, and Volume.

3. **Drawing Tools**:
   - Allow users to draw custom annotations like lines, dots, labels, or area bars.

4. **Export Options**:
   - Provide options to export the chart as an image or JSON file.

5. **Performance Optimization**:
   - Implement `sample_rate` for large datasets.
   - Use adaptive rendering for zoomed-in views.

6. **Accessibility**:
   - Ensure keyboard navigation and data summaries are optimized for screen readers.

---

### **Conclusion**

The Candle Chart Widget and Graph Widget together empower developers to create robust, customized visualizations. With support for multiple indicators, candlestick types, real-time updates, and dynamic graphing capabilities, these tools provide the flexibility needed to build powerful, interactive, and extensible interfaces for a wide range of applications.

---

### **Timeline Widget**

The Timeline Widget is a specialized graph-like structure focusing on the chronological arrangement of events. It expands only horizontally and offers advanced features for representing, interacting with, and managing time-based data. Additionally, tracks can be used to organize and manipulate content such as video, audio, or animations over time.

---

### **Core Features**

1. **Horizontal Layout**:
   - The timeline expands only along the horizontal axis, ideal for representing events over time.
   - Supports scrolling and zooming for exploring longer timelines.

2. **Event Markers**:
   - Markers represent key events on the timeline.
   - Customizable shapes, colors, and icons for markers.
   - Markers can include tooltips or labels for detailed event information.

3. **Tracks**:
   - Supports tracks for managing time-based content like video, audio, or animations.
   - Tracks allow users to drag, drop, and adjust content segments over time.
   - Tracks can have unique styling, labels, and categories.

4. **Event Categories**:
   - Events can be grouped into categories, distinguished by color or marker style.
   - Categories can be toggled on/off to filter the timeline view.

5. **Dynamic Updates**:
   - Events and tracks can be dynamically added, updated, or removed based on data changes from co-chains or other sources.

6. **Interactivity**:
   - Clickable markers to trigger intents (e.g., open detailed views, start animations).
   - Hover effects for displaying tooltips or additional data.
   - Tracks support dragging, resizing, and linking of content segments.

7. **Styling and Customization**:
   - GSS designers can style the timeline background, marker appearance, grid lines, labels, and tracks.
   - Support for animations on marker entrance, updates, or transitions.

8. **Data Sources**:
   - Events and tracks can be sourced from static arrays, co-chains, or APIs.
   - Accepts time-series data formats for seamless integration.

9. **Accessibility**:
   - Screen-reader-friendly descriptions for events and tracks.
   - Keyboard navigation for browsing through the timeline.

---

### **M3L Fields**

| **Field**          | **Description**                                    | **Example**                                              |
| ------------------- | -------------------------------------------------- | -------------------------------------------------------- |
| `data_source`      | Defines the source of the timeline data.           | `data_source = "@SQeeL://events.db"`                    |
| `categories`       | Groups events into categories with unique styles.  | `categories = [ "work", "personal" ]`               |
| `tracks`           | Defines tracks for time-based content.             | `tracks = [ { name = "Audio", type = "audio", items = [...] } ]` |
| `intents`          | Defines interactions for markers or tracks.        | `intents = [ "on_click", "on_hover", "on_drag" ]`   |
| `animation`        | Animations for marker and track transitions.       | `animation = { enter = "fade-in", update = "bounce" }` |
| `tooltip`          | Enables tooltips for events and tracks.            | `tooltip = true`                                        |
| `grid_lines`       | Configures grid lines for the timeline.            | `grid_lines = true`                                     |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                          | **Example**                              |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| `timeline.background`     | Background color for the timeline.       | `timeline.background = "#FFF"`         |
| `timeline.marker.shape`   | Shape of event markers.                  | `timeline.marker.shape = "circle"`     |
| `timeline.marker.color`   | Color of event markers.                  | `timeline.marker.color = "#00F"`       |
| `timeline.marker.size`    | Size of event markers.                   | `timeline.marker.size = "10px"`        |
| `timeline.track.style`    | Styling for tracks (e.g., color, height). | `timeline.track.style = { color = "#CCC", height = "20px" }` |
| `timeline.grid.style`     | Gridline style for the timeline.         | `timeline.grid.style = "dashed"`       |
| `timeline.label.font`     | Font settings for labels.                | `timeline.label.font = "Arial, sans-serif"` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "timeline"
data_source = "@SQeeL://events.db"
categories = [ "work", "personal" ]
tracks = [
    { name = "Audio", type = "audio", items = [ { start = 0, end = 10, label = "Intro" } ] },
    { name = "Video", type = "video", items = [ { start = 5, end = 15, label = "Main Clip" } ] },
    { name = "Animation", type = "animation", items = [ { start = 7, end = 12, label = "Fade Transition" } ] }
]
intents = [ "on_click", "on_hover", "on_drag" ]
animation = { enter = "fade-in", update = "slide" }
tooltip = true
grid_lines = true
```

---

### **Example GSS Implementation**

```toml
[timeline]
background = "#FFF"

[timeline.marker]
shape = "circle"
color = "#00F"
size = "10px"

[timeline.track]
style = { color = "#CCC", height = "20px" }

[timeline.grid]
style = "dashed"
major.color = "#AAA"
minor.color = "#CCC"

[timeline.label]
font = "Arial, sans-serif"
color = "#333"
```

---

### **Advanced Considerations**

1. **Dynamic Event and Track Management**:
   - Events and tracks can be added or removed in real time, with smooth animations.

2. **Granularity Options**:
   - Zoom levels to view daily, monthly, or yearly events.

3. **Custom Interactions**:
   - Developers can define actions triggered by specific markers or tracks (e.g., link to a detailed page or trigger co-chain actions).

4. **Performance Optimization**:
   - Lazy loading for events and tracks in extensive timelines.
   - Clustering for densely packed events to reduce visual clutter.

---

### **Use Cases**
- **Project Timelines**: Visualize deadlines, milestones, and task progress.
- **Media Editing**: Manage video, audio, and animation tracks with adjustable durations.
- **Historical Data**: Explore events over months, years, or centuries.
- **Personal Logs**: Track daily activities, workouts, or journaling.

---

### **Conclusion**

The Timeline Widget combines flexibility and interactivity to visualize time-based data effectively. With support for event markers, tracks, animations, dynamic updates, and extensive styling options, it is a powerful tool for a wide range of applications, from media editing to project management.

---

### **Waterfall Widget**

**Waterfall Widget**: Displays a continuous stream of data over time, often used for visualizing RF signals, sensor data, or other time-based intensity variations. Supports vertical and horizontal orientations with customizable color gradients to emphasize stronger signals. Additionally, icons and shapes can be dynamically overlaid to mark major events or pattern matches, enhancing data visualization.

---

### **Core Features**

1. **Data Visualization**:
   - Displays intensity over time, commonly used for radio signals, seismic activity, or financial trends.
   - Supports both real-time and historical data streaming.

2. **Orientation and Layout**:
   - Can be rendered in **vertical** or **horizontal** orientation.
   - Adaptable to screen size with dynamic resizing based on user preference.

3. **Customizable Color Gradients**:
   - Allows defining color schemes to represent different intensity levels.
   - Supports heatmap-like visualization for improved clarity.

4. **Data Sources**:
   - Can pull data dynamically from:
     - **UndChain Database**: Fetches time-series data securely.
     - **Live Data Streams**: Connects to real-time sources like RF scanners or network traffic monitors.
     - **Static Datasets**: Used for testing and pre-recorded analysis.

5. **Interactivity**:
   - Supports zooming and panning for closer inspection of data.
   - Users can hover over data points to display tooltip information.

6. **Threshold Alerts**:
   - Can define intensity thresholds that trigger visual or audio alerts.
   - Useful for monitoring critical signals like system failures or emergency alerts.

7. **Event Markers & Pattern Recognition**:
   - Allows icons or shapes to be drawn at specific points to highlight key events.
   - Enables pattern recognition to overlay alerts or contextual annotations.
   - Ideal for marking interference in RF analysis, seismic anomalies, or trend spikes.

8. **GSS Styling and Animations**:
   - Customizable animations for data flow (e.g., smooth scrolling or fading transitions).
   - Allows GSS designers to implement custom effects based on intensity shifts.
   - Icons and markers can have animations tied to their appearance.

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "waterfall"
data_source = "SQeeL://sensor_data/realtime"
orientation = "horizontal"
color_gradient = { low = "#0000FF", mid = "#00FF00", high = "#FF0000" }
threshholds = { warning = 70, critical = 90 }
zoom_enabled = true
pan_enabled = true

[[layout.container.content.markers]]
position = 1245
icon = "@UndChain/icons/signal_warning.svg"
label = "Signal Interference Detected"

[[layout.container.content.markers]]
position = 2670
shape = "circle"
color = "#FFA500"
label = "Detected Anomaly"
```

---

### **Example GSS Implementation**

```toml
[waterfall]
background = "#000"
border = "1px solid #444"

[waterfall.data_intensity]
low = "#0000FF"
mid = "#00FF00"
high = "#FF0000"

[waterfall.animation]
scroll_speed = "2s"
transition_effect = "fade-in"

[waterfall.tooltip]
font-size = "14px"
color = "#FFF"
background = "rgba(0,0,0,0.7)"

[waterfall.markers]
icon_size = "20px"
marker_animation = "pulse"
```

---

### **Use Cases**

- **Radio Frequency Monitoring**: Visualizes RF noise levels and spectrum analysis, marking interference sources.
- **Seismic Activity Tracking**: Displays earthquake wave propagation with annotations for key events.
- **Stock Market Trends**: Shows financial movement over time, overlaying major buy/sell indicators.
- **Network Traffic Analysis**: Monitors bandwidth usage and anomalies, highlighting unusual spikes.

---

### **Conclusion**

The Waterfall Widget provides a powerful means of displaying time-based data with customizable visualizations. With real-time data streaming, custom gradients, event markers, and interactivity, it is a valuable tool for applications requiring continuous signal monitoring, anomaly detection, or advanced trend analysis.

---

### **Gantt Chart Widget**

The Gantt Chart Widget is a logical extension of the Timeline Widget, designed specifically for project management and task tracking. It inherits the core functionality of the Timeline Widget, adding task dependencies, progress indicators, and enhanced interaction capabilities.

---

### **Core Features**

1. **Task Representation**:
   - Displays tasks as horizontal bars spanning their start and end times.
   - Supports grouping tasks into parent-child hierarchies.

2. **Dependencies**:
   - Visualizes task dependencies using arrows or lines connecting tasks.
   - Supports lag/lead time between dependent tasks.

3. **Progress Indicators**:
   - Displays the progress of each task as a percentage within the task bar.
   - Progress can be updated dynamically from data sources.

4. **Dynamic Updates**:
   - Tasks and dependencies can be dynamically added, updated, or removed based on real-time data.

5. **Tracks and Layers**:
   - Tasks are organized into tracks, similar to the Timeline Widget.
   - Layers can represent different teams, phases, or milestones.

6. **Interactivity**:
   - Clickable tasks to trigger intents (e.g., open task details, mark as complete).
   - Drag-and-drop functionality for adjusting task durations or dependencies.

7. **Styling and Customization**:
   - GSS designers can define task colors, dependency line styles, progress indicators, and gridlines.
   - Gridlines can be fully customized for style, color, and granularity.
   - Default color schemes can be overridden or customized per project.

8. **Data Sources**:
   - Tasks and dependencies can be sourced from static arrays, co-chains, or APIs.
   - Accepts project management data formats for seamless integration.

9. **Accessibility**:
   - Screen-reader-friendly descriptions for tasks and dependencies.
   - Keyboard navigation for moving between tasks and layers.

---

### **M3L Fields**

| **Field**         | **Description**                                   | **Example**                                              |
| ------------------ | ------------------------------------------------- | -------------------------------------------------------- |
| `data_source`     | Defines the source of the Gantt chart data.        | `data_source = "@SQeeL://project_tasks.db"`             |
| `tasks`           | Defines tasks, including start, end, and progress.| `tasks = [ { id = "1", name = "Task A", start = 0, end = 10, progress = 50 } ]` |
| `dependencies`    | Links tasks with dependencies.                    | `dependencies = [ { from = "1", to = "2", type = "FS" } ]` |
| `intents`         | Defines interactions for tasks or dependencies.   | `intents = [ "on_click", "on_drag" ]`               |
| `animation`       | Animations for transitions or updates.            | `animation = { enter = "fade-in", update = "grow" }`|
| `tooltip`         | Enables tooltips for tasks and dependencies.      | `tooltip = true`                                        |
| `grid_lines`      | Configures grid lines for the Gantt chart.         | `grid_lines = true`                                     |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                          | **Example**                              |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| `gantt.background`        | Background color for the Gantt chart.    | `gantt.background = "#FFF"`           |
| `gantt.task.color`        | Default color for task bars.             | `gantt.task.color = "#00F"`           |
| `gantt.task.progress.color`| Color for task progress indicators.     | `gantt.task.progress.color = "#0A0"`  |
| `gantt.dependency.line`   | Style for dependency lines.              | `gantt.dependency.line = "dashed"`    |
| `gantt.grid.style`        | Gridline style for the Gantt chart.      | `gantt.grid.style = { major = "solid", color = "#CCC" }`         |
| `gantt.label.font`        | Font settings for task labels.           | `gantt.label.font = "Arial, sans-serif"`|

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "gantt_chart"
data_source = "@SQeeL://project_tasks.db"
tasks = [
    { id = "1", name = "Task A", start = 0, end = 10, progress = 50 },
    { id = "2", name = "Task B", start = 5, end = 15, progress = 25 }
]
dependencies = [
    { from = "1", to = "2", type = "FS" }
]
intents = [ "on_click", "on_drag" ]
animation = { enter = "fade-in", update = "grow" }
tooltip = true
grid_lines = true
```

---

### **Example GSS Implementation**

```toml
[gantt]
background = "#FFF"

[gantt.task]
color = "#00F"
progress.color = "#0A0"

[gantt.dependency.line]
style = "dashed"
color = "#333"

[gantt.grid]
style = { major = "solid", color = "#CCC" }

[gantt.label]
font = "Arial, sans-serif"
color = "#333"
```

---

### **Advanced Considerations**

1. **Dynamic Task and Dependency Management**:
   - Tasks and dependencies can be added or removed in real time.

2. **Custom Interactions**:
   - Developers can define actions triggered by specific tasks or dependencies.

3. **Performance Optimization**:
   - Lazy loading for large projects.
   - Efficient rendering for densely populated charts.

4. **Color Schemes**:
   - Default multicolored schemes can be overridden or made user-selectable.

5. **Grid Styling**:
   - Fully customizable gridlines, allowing designers to define major and minor styles separately.

---

### **Use Cases**
- **Project Management**: Track tasks, deadlines, and dependencies.
- **Resource Allocation**: Visualize resource usage across time.
- **Milestone Tracking**: Highlight key milestones and their dependencies.
- **Organizational Collaboration**: Display project progress and task ownership within an UndChain-based organization.

---

### **Conclusion**

The Gantt Chart Widget is an essential tool for project management and task tracking. With features like task dependencies, progress indicators, and real-time updates, combined with extensive GSS styling options, it provides a powerful and customizable solution for organizations and developers alike.

---

### **Roadmap Widget**

**Roadmap** - Widget that depicts a roadmap for a project. Contains markers that are designed for additional information.

The Roadmap Widget is a dynamic visualization tool for tracking and communicating project progress. It allows flexible pathway designs, milestone markers, and integration with card widgets for detailed information. The widget supports advanced customization for diverse use cases, including organizational and personal planning. Additionally, it introduces the ability for GSS designers to create custom paths using SVG files, offering unparalleled flexibility.

---

### **Core Features**

1. **Pathway Representation**:
   - Display the roadmap as a line, curve, or custom path defined by the GSS designer.
   - Options for linear, circular, or branching pathways.
   - Custom paths can be created using SVG files, with markers positioned dynamically based on available space and proximity rules.

2. **Markers**:
   - Represents milestones along the pathway using cards as the base framework.
   - Each marker can use any card type, with images replaced by customizable icons (SVG).
   - Differentiates between completed and pending markers with distinct styles.

3. **Dynamic Updates**:
   - Allows for real-time addition, removal, or updates to markers based on data changes.
   - Supports dynamic marker visibility based on zoom level, priority, or space constraints on custom paths.

4. **Styling and Customization**:
   - GSS designers can style the pathway, markers, tooltips, animations, and icons.
   - Media queries can adjust roadmap layout and styling for different screen sizes, ensuring responsiveness.
   - Provides default and custom themes for pathways and markers.

5. **Interactivity**:
   - Markers are clickable, triggering intents such as opening details or navigating to related content.
   - Hover effects for displaying additional information (e.g., descriptions, percentages).

6. **Progress Indicators**:
   - Option to visualize progress as a percentage, dynamically moving along the pathway.
   - Support for gradients or animations to show progression visually.

7. **Animations and Drawing Effects**:
   - Introduces a "draw" animation for SVG-defined paths, creating a smooth visual effect where the path is drawn onscreen.
   - The drawing speed can dynamically adjust based on the sharpness of angles in the SVG path, slowing down for tighter turns and accelerating on straight segments.

8. **Data Sources**:
   - Can fetch roadmap data from co-chains, APIs, or static arrays.
   - Links each marker to relevant data points for detailed interaction.

9. **Accessibility**:
   - Screen-reader support for roadmap descriptions and marker details.
   - Keyboard navigation for traversing the pathway and markers.

---

### **M3L Fields**

| **Field**         | **Description**                                   | **Example**                                              |
| ------------------ | ------------------------------------------------- | -------------------------------------------------------- |
| `data_source`     | Defines the source of the roadmap data.            | `data_source = "@SQeeL://project_roadmap.db"`            |
| `path_type`       | Specifies the style of the pathway.                | `path_type = "custom"`                                   |
| `markers`         | Defines roadmap markers with details.              | `markers = [ { name = "Start", position = 0, status = "completed", card_type = "info" } ]` |
| `intents`         | Defines interactions for markers or the pathway.   | `intents = [ "on_click", "on_hover" ]`               |
| `animation`       | Animations for transitions or updates.             | `animation = { enter = "fade-in", update = "draw" }`|
| `tooltip`         | Enables tooltips for markers.                      | `tooltip = true`                                        |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                          | **Example**                              |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| `roadmap.background`      | Background color for the roadmap.         | `roadmap.background = "#FFF"`         |
| `roadmap.path.style`      | Style for the roadmap pathway.            | `roadmap.path.style = "custom"`       |
| `roadmap.path.svg`        | Path definition using an SVG file.        | `roadmap.path.svg = "@assets/roadmap_path.svg"` |
| `roadmap.path.draw_speed` | Adjusts the speed of the "draw" animation.| `roadmap.path.draw_speed = "dynamic"` |
| `roadmap.marker.completed`| Styling for completed markers.            | `roadmap.marker.completed = { color = "#0A0", icon = "checkmark" }` |
| `roadmap.marker.pending`  | Styling for pending markers.              | `roadmap.marker.pending = { color = "#AAA", icon = "circle" }` |
| `roadmap.tooltip`         | Styling for marker tooltips.              | `roadmap.tooltip = { background = "#000", color = "#FFF" }` |
| `roadmap.progress`        | Customization for progress indicators.    | `roadmap.progress = { gradient = "true", color = "#0F0" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "roadmap"
data_source = "@SQeeL://project_roadmap.db"
path_type = "custom"
markers = [
    { name = "Start", position = 0, status = "completed", tooltip = "Project Initiation", card_type = "info" },
    { name = "Midway", position = 50, status = "pending", tooltip = "Halfway Mark", card_type = "highlight" },
    { name = "Finish", position = 100, status = "pending", tooltip = "Completion", card_type = "action" }
]
intents = [ "on_click", "on_hover" ]
animation = { enter = "fade-in", update = "draw" }
tooltip = true
```

---

### **Example GSS Implementation**

```toml
[roadmap]
background = "#FFF"

[roadmap.path]
style = "custom"
svg = "@assets/roadmap_path.svg"
width = "5px"
color = "#333"
draw_speed = "dynamic"

[roadmap.marker.completed]
color = "#0A0"
icon = "checkmark"

[roadmap.marker.pending]
color = "#AAA"
icon = "circle"

[roadmap.tooltip]
background = "#000"
color = "#FFF"
font-size = "12px"

[roadmap.progress]
gradient = true
color = "#0F0"
```

---

### **Advanced Considerations**

1. **Custom Marker Shapes and Cards**:
   - Allow developers to define custom SVG shapes or use card widgets for detailed marker content.

2. **Animations**:
   - Entrance, progress, and exit animations for markers and pathways.
   - The "draw" animation dynamically adjusts speed based on the path's sharpness, creating a natural flow.

3. **Media Queries**:
   - Use media queries to adjust roadmap layout and styling for different screen sizes.

4. **Dynamic Progress**:
   - Real-time updates reflecting progress as tasks are completed.

5. **Custom Paths with SVG**:
   - GSS designers can define completely custom pathways using SVG files, ensuring flexibility and visual creativity.
   - Rules ensure markers dynamically position themselves without overlapping existing content or markers.

6. **Integration with Other Widgets**:
   - Link markers to Gantt charts, timelines, or detailed task views.

---

### **Use Cases**
- **Project Tracking**: Visualize progress across milestones and goals.
- **Product Roadmaps**: Show upcoming features, releases, and updates.
- **Organizational Planning**: Communicate long-term strategies to stakeholders.
- **Personal Goals**: Track personal achievements and future objectives.

---

### **Conclusion**

The Roadmap Widget is a versatile tool for visualizing progress and milestones in a project. With its integration of card widgets, customizable pathways, SVG-defined paths, and dynamic updates, it provides an engaging and adaptable way to communicate plans and progress effectively.

---

### **Skill Tree Widget**

**Skill Tree**: This widget creates a skill tree-like structure where nodes (badges) can be activated only when their parent nodes are also activated. Nodes represent milestones, skills, or objectives, and the tree visually showcases progression paths.

---

### **Core Features**

1. **Node Representation**:

   - Nodes are based on a custom `badge` design, featuring a description, an image, and optional status icons.
   - Each node includes a label, status (locked/unlocked), and optional tooltip or description.

2. **Parent-Child Relationships**:

   - Nodes are locked until their parent nodes are activated.
   - Support for multiple parents (e.g., AND/OR relationships).

3. **Progress Tracking**:

   - Dynamic updates show which nodes are completed, available, or locked.
   - Real-time updates if connected to a co-chain like Mimic or SQeeL.

4. **Path Styling**:

   - GSS designers can style the connections between nodes (e.g., lines, arrows, curves).
   - Customizable animations for unlocking nodes and connecting paths.

5. **Skill Points or Unlock Criteria**:

   - Nodes can be unlocked using skill points, defined in the M3L file.
   - Other criteria (e.g., completing a task or reaching a milestone) can be specified.

6. **Dynamic Layout**:

   - Automatic layout adjustment for varying screen sizes using media queries.
   - Horizontal, vertical, and radial layout options.

7. **Interactive Features**:

   - Clickable or hoverable nodes to display details or trigger intents.
   - Tooltips or detailed views can display extended descriptions or unlock requirements when a node is highlighted or clicked.
   - Toast notifications can provide feedback when a node is unlocked, enhancing user engagement.

8. **Pan and Zoom**:

   - Users can pan and zoom around the skill tree, with panning behavior defined by GSS (e.g., right analog stick for controllers or `Ctrl + drag` for mouse).
   - Smooth zoom transitions ensure a seamless experience.

9. **Custom Animations and Multi-Layered Trees**:

   - GSS designers can create custom node unlock animations.
   - Multi-layered trees allow users to dive into specific subjects or explore diverse branches.
   - Root nodes can expand into new trees, with clustering to reduce clutter.

10. **Background Customization**:

    - GSS designers can use colors, gradients, or images as backgrounds for the tree.

---

### **M3L Fields**

| **Field**     | **Description**                                    | **Example**                                                                                                      |
| ------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `data_source` | Defines the source of the skill tree data.         | `data_source = "@SQeeL://skill_tree.db"`                                                                         |
| `layout`      | Specifies the layout style (horizontal, vertical). | `layout = "radial"`                                                                                              |
| `tree`        | Defines the nodes and their relationships.         | `tree = [ { id = "1", label = "Skill A", status = "locked", points_required = 3, connections = [ "2", "3" ] } ]` |
| `intents`     | Specifies interactions for nodes.                  | `intents = [ "on_click", "on_hover" ]`                                                                           |
| `background`  | Specifies a background image or color.             | `background = "@UndChain/skill_background.jpg"`                                                                  |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                      | **Example**                                                        |
| ------------------------- | ------------------------------------ | ------------------------------------------------------------------ |
| `skilltree.background`    | Background color for the skill tree. | `skilltree.background = "#FFF"`                                    |
| `skilltree.node.locked`   | Styling for locked nodes.            | `skilltree.node.locked = { color = "#AAA", icon = "lock" }`        |
| `skilltree.node.unlocked` | Styling for unlocked nodes.          | `skilltree.node.unlocked = { color = "#0A0", icon = "checkmark" }` |
| `skilltree.path.style`    | Path styling between nodes.          | `skilltree.path.style = { type = "curve", color = "#333" }`        |
| `skilltree.tooltip`       | Styling for tooltips.                | `skilltree.tooltip = { background = "#000", color = "#FFF" }`      |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "skill_tree"
data_source = "@SQeeL://skill_tree.db"
layout = "radial"
background = "@assets/background.jpg"
tree = [
    {
        id = "1",
        label = "Skill A",
        status = "completed",
        points_required = 0,
        tooltip = "Learned basic skill A",
        connections = [ "2", "3" ]
    },
    {
        id = "2",
        label = "Skill B",
        status = "locked",
        points_required = 3,
        tooltip = "Unlock after earning 3 skill points",
        connections = []
    },
    {
        id = "3",
        label = "Skill C",
        status = "locked",
        points_required = 5,
        tooltip = "Unlock after earning 5 skill points",
        connections = []
    }
]
intents = [ "on_click", "on_hover" ]
```

---

### **Example GSS Implementation**

```toml
[skilltree]
background = "#FFF"

[skilltree.node.locked]
color = "#AAA"
icon = "lock"

[skilltree.node.unlocked]
color = "#0A0"
icon = "checkmark"

[skilltree.path]
style = { type = "curve", color = "#333" }

[skilltree.tooltip]
background = "#000"
color = "#FFF"
font-size = "12px"
```

---

### **Advanced Considerations**

1. **Dynamic Node Unlocking**:

   - Nodes can unlock dynamically based on user actions, skill points, or data changes.
   - Real-time updates from co-chains enable interactive experiences.

2. **Custom Animations**:

   - GSS designers can create animations for node unlocking and path transitions.

3. **Multi-Layer Trees and Clustering**:

   - Support for hierarchical layers or sub-trees to organize large skill trees.
   - Clustering reduces clutter and allows root nodes to expand into new trees.

4. **Pan and Zoom**:

   - Allow users to navigate large trees with smooth panning and zooming.
   - Define panning behavior per input type in GSS.

5. **Toast Notifications**:

   - Notify users of node unlocks or achievements with engaging feedback.

---

### **Use Cases**

- **E-learning Platforms**: Represent course progress and prerequisites visually.
- **Gamification**: Track achievements and progress in productivity or learning apps.
- **Feature Roadmaps**: Display unlocked and upcoming features for user engagement.
- **Decision Making**: Represent branching decisions or workflows in a structured, visual format.
- **Application Settings**: Highlight features and configurations available within the app.

---

### **Conclusion**

The Skill Tree Widget introduces a highly interactive and visually engaging way to represent progress, dependencies, and unlockable content. With its support for dynamic updates, skill point integration, customizable paths, panning and zooming, and toast notifications, it is a versatile tool for applications ranging from e-learning to gamified productivity systems.

---

### **Badge Widget**

**Badge**: This widget acts as a hybrid between an icon and a card. It provides more space to display an icon and a name, while also allowing for expanded functionality such as viewing detailed descriptions or unlocking new features.

---

### **Core Features**

1. **Compact Design with Expandable Details**:
   - Displays an icon and a name in its default state.
   - Expands to show a full description or additional details when triggered by specific intents.

2. **Unlockable Functionality**:
   - Can transition from a "locked" to "unlocked" state, with animations and styling defined in the GSS file.
   - Useful for gamification, skill trees, or feature progression.

3. **Interactive Features**:
   - Supports intents such as `descriptor`, `unlock`, and `highlight` to provide a highly interactive experience.
   - Examples of interactions:
     - **Descriptor**: Displays a popup or page with detailed information about the badge.
     - **Unlock**: Changes the badge’s state to "unlocked," triggering animations and updates.
     - **Highlight**: Temporarily emphasizes the badge with animations or effects.

4. **Dynamic Updates**:
   - Real-time updates to badge status, description, or associated data via co-chains (e.g., Mimic or SQeeL).

5. **Styling and Customization**:
   - GSS designers can define the appearance, hover effects, unlock animations, and how expanded descriptions are displayed.
   - Supports dynamic styling based on state (e.g., locked, unlocked, highlighted).

6. **Accessibility**:
   - Includes screen-reader support for badge names and descriptions.
   - Keyboard navigation for interacting with badges and triggering intents.

---

### **M3L Fields**

| **Field**       | **Description**                                  | **Example**                                              |
| --------------- | ------------------------------------------------ | -------------------------------------------------------- |
| `icon`          | Specifies the icon displayed on the badge.        | `icon = "@assets/icons/skill_icon.svg"`                |
| `name`          | The name of the badge.                           | `name = "Skill Mastery"`                                |
| `description`   | Full description displayed when expanded.         | `description = "Achieved mastery in advanced skills."` |
| `status`        | Indicates if the badge is locked or unlocked.     | `status = "locked"`                                     |
| `intents`       | Specifies the interactions supported by the badge.| `intents = [ "descriptor", "unlock", "highlight" ]`    |

---

### **GSS Styling Parameters**

| **Parameter**           | **Description**                          | **Example**                              |
| ----------------------- | ---------------------------------------- | ---------------------------------------- |
| `badge.background`      | Background color for the badge.           | `badge.background = "#FFF"`            |
| `badge.icon`            | Styling for the badge icon.               | `badge.icon = { size = "40px", color = "#333" }` |
| `badge.locked`          | Styling for locked badges.                | `badge.locked = { color = "#AAA", icon = "lock" }` |
| `badge.unlocked`        | Styling for unlocked badges.              | `badge.unlocked = { color = "#0A0", icon = "checkmark" }` |
| `badge.highlight`       | Highlight effect styling.                 | `badge.highlight = { animation = "pulse", duration = "2s" }` |
| `badge.tooltip`         | Styling for tooltips displayed on hover.  | `badge.tooltip = { background = "#000", color = "#FFF" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "badge"
icon = "@assets/icons/skill_icon.svg"
name = "Skill Mastery"
description = "Achieved mastery in advanced skills."
status = "locked"
intents = [ "descriptor", "unlock", "highlight" ]
```

---

### **Example GSS Implementation**

```toml
[badge]
background = "#FFF"

[badge.icon]
size = "40px"
color = "#333"

[badge.locked]
color = "#AAA"
icon = "lock"

[badge.unlocked]
color = "#0A0"
icon = "checkmark"

[badge.highlight]
animation = "pulse"
duration = "2s"

[badge.tooltip]
background = "#000"
color = "#FFF"
font-size = "12px"
```

---

### **Advanced Considerations**

1. **Dynamic Badge Updates**:
   - Real-time updates to badge status and description based on user progress or external triggers.
   - Integration with co-chains like Mimic or SQeeL for advanced functionality.

2. **Custom Unlock Animations**:
   - GSS designers can define unique animations for transitioning badges from locked to unlocked states.

3. **Batch Operations**:
   - Support for batch unlocking or highlighting of multiple badges simultaneously.

4. **Integration with Other Widgets**:
   - Use badges within skill trees, leaderboards, or gamified progress tracking systems.

---

### **Use Cases**
- **Skill Trees**: Serve as individual nodes within a skill tree, providing detailed descriptions and unlockable functionality.
- **Achievement Systems**: Represent user achievements or milestones in applications.
- **Gamified Interfaces**: Enhance user engagement by visually representing progress or rewards.
- **Onboarding Processes**: Highlight key steps or features during user onboarding.

---

### **Conclusion**

The Badge Widget is a versatile addition to M3L and GSS, bridging the gap between icons and cards. Its compact design, interactivity, and unlockable functionality make it ideal for skill trees, achievement systems, and gamified interfaces. By supporting dynamic updates, customizable animations, and flexible intents, the Badge Widget enhances user engagement and visual communication across applications.

---

### **Spellcheck Widget**

**Spellcheck**: Highlights misspelled words with corrections shown in a tooltip.

The Spellcheck Widget works by integrating a dictionary or grammar rule system into editable text-based widgets (like `text_area` or `text_box`). It provides a visual layer for identifying errors and offering suggestions while allowing GSS designers to customize how these elements are displayed and interacted with.

---

### **Core Features**

1. **Error Highlighting**:
   - Highlights misspelled words with customizable visual styles (e.g., red squiggly underline, background color).
   - Distinguishes between spelling and grammar errors using separate styles.

2. **Tooltip for Corrections**:
   - Displays correction suggestions in a tooltip when activated (e.g., via right-click, hover, or keyboard shortcut).
   - Supports multiple correction options with the ability to select and replace the word.

3. **Interactive Menu**:
   - Allows contextual actions like “Add to Dictionary,” “Ignore,” or “Replace.”
   - Supports integration with the `context_menu` widget for an extended set of actions.

4. **Customization Options**:
   - GSS designers can define how errors are displayed, tooltips are styled, and interactions are handled.
   - Allows for audio or haptic feedback when users interact with errors (optional).

5. **Dynamic Updates**:
   - Checks for errors dynamically as the user types or when triggered by a specific event.
   - Integrates with co-chains for advanced grammar and language processing (e.g., Mimic).

6. **Keyboard Shortcuts**:
   - Allows GSS designers to define shortcuts for enabling/disabling spellcheck or cycling through errors (e.g., pressing `Ctrl + ;` to activate spellcheck).

7. **Multi-Language Support**:
   - Supports multiple dictionaries and language rules, selectable by the user or developer.
   - Automatically switches based on content language (if defined in metadata).

8. **Standard and User-Defined Word Lists**:
   - Includes a standard word list for basic spellchecking.
   - Allows users to define custom word lists to accommodate specific terminologies or preferences.
   - User-defined words can be managed through the context menu with options to add or remove entries.

9. **Accessibility**:
   - Screen-reader support for reading out detected errors and correction suggestions.
   - Keyboard navigation for cycling through errors and interacting with tooltips.

---

### **M3L Fields**

| **Field**            | **Description**                                    | **Example**                                              |
| --------------------- | -------------------------------------------------- | -------------------------------------------------------- |
| `enabled`            | Toggles spellcheck for the associated text widget.  | `enabled = true`                                         |
| `dictionary_source`  | Specifies the source of the dictionary.             | `dictionary_source = "@SQeeL://language/dictionary.db"`  |
| `user_word_list`     | Specifies the location of the user-defined word list.| `user_word_list = "@UserStorage://custom_words.db"`     |
| `language`           | Defines the language for spellcheck.                | `language = "en-US"`                                     |
| `highlight_style`    | Defines the visual style for error highlighting.    | `highlight_style = "underline"`                         |
| `intents`            | Specifies interactions (e.g., tooltip activation).  | `intents = [ "on_hover", "on_right_click" ]`           |

---

### **GSS Styling Parameters**

| **Parameter**                | **Description**                              | **Example**                              |
| ---------------------------- | -------------------------------------------- | ---------------------------------------- |
| `spellcheck.error.spelling`  | Styling for spelling errors.                 | `spellcheck.error.spelling = { underline = "red squiggly", tooltip = "true" }` |
| `spellcheck.error.grammar`   | Styling for grammar errors.                  | `spellcheck.error.grammar = { color = "orange", tooltip = "true" }` |
| `spellcheck.tooltip`         | Styling for tooltips displaying suggestions. | `spellcheck.tooltip = { background = "#FFF", color = "#000" }` |
| `spellcheck.shortcut`        | Keyboard shortcut for toggling spellcheck.   | `spellcheck.shortcut = "Ctrl + ;"`      |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "text_area"
spellcheck = {
    enabled = true,
    dictionary_source = "@SQeeL://language/dictionary.db",
    user_word_list = "@UserStorage://custom_words.db",
    language = "en-US",
    highlight_style = "underline",
    intents = [ "on_hover", "on_right_click" ]
}
```

---

### **Example GSS Implementation**

```toml
[spellcheck.error.spelling]
underline = "red squiggly"
tooltip = true

[spellcheck.error.grammar]
color = "orange"
tooltip = true

[spellcheck.tooltip]
background = "#FFF"
color = "#000"
font-size = "12px"

[spellcheck.shortcut]
keyboard = "Ctrl + ;"
```

---

### **Advanced Considerations**

1. **Custom Error Handling**:
   - Allow developers to define custom rules for error detection (e.g., specific jargon or domain-specific terms).

2. **Co-Chain Integration**:
   - Use Mimic or similar co-chains for advanced grammar suggestions and contextual recommendations.

3. **Event Triggers**:
   - Define when spellcheck runs (e.g., on typing, on submit, or when explicitly triggered).

4. **Language Switching**:
   - Automatically detect language based on text input or metadata and switch dictionaries dynamically.

5. **Error Reporting and Analytics**:
   - Optionally log error types and frequencies for analytics or AI training.

6. **User-Defined Word Management**:
   - Provide an interface for users to manage their custom word lists, enabling easy additions or removals directly within the application.

---

### **Use Cases**
- **Text Editors**: Provide real-time spellcheck and grammar corrections for writers.
- **Form Validation**: Ensure accurate input in forms and text fields.
- **Language Learning Tools**: Highlight errors and provide explanations for educational purposes.
- **Content Creation**: Improve quality and readability in blog posts, articles, or emails.

---

### **Conclusion**

The Spellcheck Widget adds a powerful layer of functionality to text-based widgets, allowing users to easily identify and correct errors in real time. Its integration with GSS ensures that designers can create a seamless and intuitive experience while maintaining visual consistency across applications. By supporting dynamic updates, keyboard shortcuts, user-defined word lists, and co-chain integration, the Spellcheck Widget is a versatile tool for a wide range of use cases.

---

### **Autocomplete Widget**

**Autocomplete**: Assists in writing by providing options to autocomplete words, allowing for faster input and improved accuracy. Suggestions are made in real-time based on the user's context and behavior.

---

### **Core Features**

1. **Dynamic Suggestions**:
   - Provides real-time suggestions based on user input.
   - Leverages language models, co-chains (e.g., SQeeL), or predefined dictionaries for generating predictions.
   - Maintains context to refine suggestions for higher accuracy.
   - Highlights the top suggestion by confidence, with the ability for users to select alternative suggestions.

2. **Interactive Suggestion Menu**:
   - Displays a dropdown of suggestions dynamically filtered as the user types.
   - Supports interaction methods like `Ctrl + Space` after highlighting a word.
   - The most confident suggestion is pre-highlighted by default.

3. **Integration with Spellcheck**:
   - Complements the Spellcheck Widget by suggesting corrections or completing words based on user input.
   - Replaces misspelled words seamlessly with the user’s consent.

4. **Customization and Contextual Adaptation**:
   - GSS designers can customize dropdown styling and interaction behavior.
   - Context-aware suggestions (e.g., technical terms in IDEs or domain-specific language in professional settings).

5. **Multi-Language and Domain-Specific Support**:
   - Supports multiple languages and can switch dynamically based on input or metadata.
   - Domain-specific dictionaries (e.g., medical terms, programming languages) can be dynamically loaded via UndChain.
   - Custom user dictionaries can be stored locally or on UndChain (e.g., `@UserStorage/suggestions.db`).

6. **Local Execution for Performance**:
   - Runs locally for minimal lag and responsive performance.
   - Downloads custom dictionaries or context profiles from UndChain for offline use.

7. **Audio and Visual Feedback**:
   - GSS designers can define visual animations or audio cues for suggestion updates and selections.

---

### **M3L Fields**

| **Field**           | **Description**                                        | **Example**                                              |
| -------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| `dictionary_source` | Defines the source of the autocomplete dictionary.      | `dictionary_source = "@SQeeL://language/autocomplete.db"` |
| `user_dictionary`   | Custom user dictionary for personalized suggestions.    | `user_dictionary = "@UserStorage/suggestions.db"`       |
| `context`           | Provides context for the suggestions (e.g., "coding"). | `context = "IDE"`                                        |
| `language`          | Defines the language used for suggestions.             | `language = "en-US"`                                     |
| `intents`           | Specifies interactions (e.g., `on_select`).             | `intents = [ "on_type", "on_select", "on_hover" ]`     |
| `max_suggestions`   | Maximum number of suggestions to display.               | `max_suggestions = 5`                                    |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                                  | **Example**                                |
| ------------------------- | ------------------------------------------------ | ------------------------------------------ |
| `autocomplete.dropdown`   | Styling for the suggestion dropdown menu.         | `autocomplete.dropdown = { background = "#FFF", border = "1px solid #CCC" }` |
| `autocomplete.suggestion` | Styling for individual suggestions.               | `autocomplete.suggestion = { font-size = "14px", color = "#000" }` |
| `autocomplete.selected`   | Styling for the currently highlighted suggestion. | `autocomplete.selected = { background = "#EEE" }` |
| `autocomplete.tooltip`    | Styling for tooltips displaying extra context.    | `autocomplete.tooltip = { background = "#000", color = "#FFF" }` |
| `autocomplete.audio`      | Audio cues for suggestion updates or selection.   | `autocomplete.audio = { select = "click.mp3", update = "ding.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "text_area"
autocomplete = {
    dictionary_source = "@SQeeL://language/autocomplete.db",
    user_dictionary = "@UserStorage/suggestions.db",
    context = "IDE",
    language = "en-US",
    intents = [ "on_type", "on_select", "on_hover" ],
    max_suggestions = 5
}
```

---

### **Example GSS Implementation**

```toml
[autocomplete.dropdown]
background = "#FFF"
border = "1px solid #CCC"

[autocomplete.suggestion]
font-size = "14px"
color = "#000"

[autocomplete.selected]
background = "#EEE"

[autocomplete.tooltip]
background = "#000"
color = "#FFF"
font-size = "12px"

[autocomplete.audio]
select = "click.mp3"
update = "ding.mp3"
```

---

### **Advanced Considerations**

1. **Domain-Specific Suggestions**:
   - Integrate specialized dictionaries for technical domains (e.g., medical terms, legal phrases, programming languages).
   - Allow developers to define context-specific autocomplete behavior.

2. **Co-Chain Integration**:
   - Use UndChain for downloading domain-specific dictionaries or user profiles.
   - Incorporate real-time updates based on evolving user context or preferences.

3. **User Customization**:
   - Enable users to add their own frequently used words or phrases to the autocomplete dictionary.

4. **Local Execution**:
   - Ensure fast, responsive performance by running locally while syncing with cloud-based profiles.

5. **Predictive Phrasing**:
   - Suggest one word at a time while maintaining context.
   - Allow user selection of highlighted words with pre-defined keybindings (e.g., `Ctrl + Space`).

6. **Feedback Mechanisms**:
   - Allow GSS designers to implement both visual animations and audio cues for feedback.

---

### **Use Cases**
- **IDEs and Code Editors**: Suggest code snippets, function signatures, or parameters.
- **Search Engines**: Predict user queries dynamically as they type.
- **Email Clients**: Provide phrase suggestions for faster email composition.
- **Chat Applications**: Speed up messaging with contextual word or emoji suggestions.
- **Forms and Surveys**: Guide users through input fields with predictive suggestions.

---

### **Conclusion**

The Autocomplete Widget enhances input efficiency and accuracy by providing dynamic, context-aware suggestions. Its integration with M3L and GSS ensures flexibility, allowing developers to tailor its functionality and design to meet diverse application needs. Whether used in productivity tools, coding environments, or communication platforms, the Autocomplete Widget is a powerful addition to the M3L framework.

---

### **Text Prediction Widget**

**Text Prediction**: This widget extends the functionality of autocomplete by leveraging AI models via the Mimic co-chain to predict entire strings or phrases based on the context of the user’s input. It provides powerful, context-aware text generation capabilities for productivity and creative applications.

---

### **Core Features**

1. **AI-Powered Predictions**:
   - Dynamically predicts complete strings, sentences, or paragraphs.
   - Uses the Mimic co-chain for advanced context processing and language modeling.

2. **Context Awareness**:
   - Maintains context to generate relevant and cohesive predictions.
   - Adapts to the tone, structure, and intent of the user’s writing.

3. **Dynamic Interaction**:
   - Predictions can be displayed inline in faint text or externally adjacent to the text area.
   - Users can accept, reject, or edit predictions seamlessly with shortcuts (e.g., `Ctrl + Plus`).

4. **Customization and Adaptability**:
   - GSS designers can define how predictions are presented and interacted with.
   - Developers can customize prompts sent to the Mimic co-chain for domain-specific predictions.

5. **Multi-Language Support**:
   - Supports multiple languages and dynamically adjusts based on input.

6. **Local Caching for Performance**:
   - Caches recent predictions locally to improve responsiveness and reduce repeated requests.

7. **Accessibility**:
   - Fully navigable via keyboard and screen-readers.
   - Offers voice prompts for visually impaired users (optional).

---

### **M3L Fields**

| **Field**           | **Description**                                        | **Example**                                              |
| -------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| `ai_source`         | Specifies the source of the AI model.                   | `ai_source = "@Mimic://text_prediction"`               |
| `context`           | Provides context for the predictions (e.g., "email").  | `context = "business email"`                            |
| `language`          | Defines the language used for predictions.             | `language = "en-US"`                                     |
| `max_predictions`   | Maximum number of predictions to display.               | `max_predictions = 3`                                    |
| `intents`           | Specifies interactions (e.g., `on_predict`).            | `intents = [ "on_type", "on_hover", "on_predict" ]`   |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                                  | **Example**                                |
| ------------------------- | ------------------------------------------------ | ------------------------------------------ |
| `textprediction.inline`   | Styling for inline predictions.                   | `textprediction.inline = { color = "#CCC" }` |
| `textprediction.external` | Styling for external predictions outside the text field. | `textprediction.external = { color = "#AAA", font-style = "italic" }` |
| `textprediction.selected` | Styling for the currently highlighted prediction. | `textprediction.selected = { background = "#EEE" }` |
| `textprediction.tooltip`  | Styling for tooltips displaying extra context.    | `textprediction.tooltip = { background = "#000", color = "#FFF" }` |
| `textprediction.audio`    | Audio cues for prediction updates or selection.   | `textprediction.audio = { select = "confirm.mp3", update = "notify.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "text_area"
text_prediction = {
    ai_source = "@Mimic://text_prediction",
    context = "business email",
    language = "en-US",
    intents = [ "on_type", "on_hover", "on_predict" ],
    max_predictions = 3
}
```

---

### **Example GSS Implementation**

```toml
[textprediction.inline]
color = "#CCC"

[textprediction.external]
color = "#AAA"
font-style = "italic"

[textprediction.selected]
background = "#EEE"

[textprediction.tooltip]
background = "#000"
color = "#FFF"
font-size = "12px"

[textprediction.audio]
select = "confirm.mp3"
update = "notify.mp3"
```

---

### **Advanced Considerations**

1. **Domain-Specific Predictions**:
   - Use custom prompts for Mimic to generate domain-relevant text (e.g., medical documentation, legal contracts).
   - Incorporate predefined templates to speed up repetitive tasks.

2. **Real-Time Updates**:
   - Dynamically update predictions based on the user’s evolving input.
   - Leverage context to refine predictions for accuracy and tone.

3. **Feedback and Learning**:
   - Capture user feedback to improve the AI model’s predictions over time.
   - Optionally log user-approved predictions for analysis and refinement.

4. **Co-Chain Dependency**:
   - Requires Mimic for text prediction, but can fallback to a limited local model for basic functionality.

5. **Multi-Sentence Predictions**:
   - Optionally extend predictions to include multi-sentence or paragraph-level outputs.

6. **Shortcut Customization**:
   - GSS designers can define shortcuts for accepting predictions (e.g., `Ctrl + Plus`).

---

### **Use Cases**
- **Email Drafting**: Generate professional email responses with appropriate tone and context.
- **Content Creation**: Assist writers with completing sentences, paragraphs, or entire sections.
- **Code Assistance**: Provide boilerplate code snippets or function templates in IDEs.
- **Chatbots and Messaging**: Enable smart, context-aware replies in communication platforms.
- **Educational Tools**: Offer writing assistance and suggestions tailored to learning objectives.

---

### **Conclusion**

The Text Prediction Widget empowers users with AI-driven text generation capabilities, bridging the gap between manual input and fully automated content creation. With its integration into M3L and GSS, it offers flexibility and adaptability across diverse applications, enhancing productivity and user experience.

---

### **Video Widget**

**Video**: Plays videos with predefined controls and settings, serving as a foundational component for larger media workflows. The control UI is fully customizable through GSS, allowing advanced layouts such as overlays, separate control windows, or embedded controls. This widget also supports video streaming via the Live co-chain, enabling seamless content delivery within UndChain.

---

### **Core Features**

1. **Basic Playback Controls**:
   - **Play/Pause**: Toggle between playing and pausing the video.
   - **Fast Forward (FF)** and **Rewind (RR)**: Skip forward or backward by predefined intervals.
   - **Replay**: Restart the video from the beginning.

2. **Volume Control**:
   - GSS defines how volume is adjusted (e.g., slider, buttons, or dials).
   - Includes Mute/Unmute functionality.

3. **Progress Bar**:
   - Editable size, allowing developers to tailor its appearance.
   - Can display **highlights** based on popular playback sections.
   - Chapter markers for navigation.

4. **Chapters and Bookmarks**:
   - Allow users to jump to specific sections of interest.
   - Chapters can include titles and timestamps.
   - Mimic integration in the Media Player Widget can auto-define chapters/bookmarks based on content analysis.

5. **Subtitles and Closed Captions (CC)**:
   - Load subtitle files (e.g., SRT, VTT).
   - GSS designers can style fonts, colors, positioning, and background for subtitles and captions.

6. **Playback Speed Control**:
   - Adjustable playback speeds (e.g., 0.5x, 1x, 1.5x, 2x).

7. **Full-Screen, Fill-Screen, and Pop-Out Modes**:
   - **Full-Screen**: Seamless transition between windowed and full-screen modes.
   - **Fill-Screen**: Expands the video horizontally while maintaining aspect ratio, leaving unused areas available for other widgets.
   - **Pop-Out Mode**: Allows users to drag the video into a separate, floating window.

8. **Mini Mode**:
   - Activates when the user scrolls past the video content.
   - Displays a small floating player with basic controls (e.g., Play/Pause and Expand).

9. **Source Flexibility**:
   - Supports AVX encoding for efficient and royalty-free video playback.
   - Videos can be local (`@Undline/videos/video.mp4`), streamed via co-chains like SQeeL, or hosted on the Live co-chain for seamless streaming.

10. **Accessibility Features**:
   - Keyboard shortcuts for all controls (e.g., Space for play/pause, Arrow keys for seeking).
   - Screen-reader support for buttons and labels.

11. **Buffering Indicator**:
    - Loading animations for videos being streamed or buffered.

12. **Dynamic Updates**:
    - Dynamic content switching without reloading the widget (e.g., switching sources).

---

### **M3L Fields**

| **Field**           | **Description**                                  | **Example**                                              |
| -------------------- | ------------------------------------------------ | -------------------------------------------------------- |
| `source`            | Defines the video source.                        | `source = "@Live://channel/stream_id"`                  |
| `subtitles`         | Provides a subtitle file for the video.          | `subtitles = "@SQeeL://videos/subtitles.srt"`           |
| `autoplay`          | Automatically starts playback when loaded.       | `autoplay = true`                                        |
| `loop`              | Enables continuous playback.                     | `loop = false`                                           |
| `playback_speeds`   | Defines supported playback speeds.               | `playback_speeds = [ 0.5, 1.0, 1.5, 2.0 ]`              |
| `default_speed`     | Sets the default playback speed.                 | `default_speed = 1.0`                                    |
| `chapters`          | Defines video chapters with titles and timestamps.| `chapters = [ { title = "Introduction", time = "00:00:00" }, { title = "Conclusion", time = "00:10:00" } ]` |
| `intents`           | Specifies interactions for controls.             | `intents = [ "on_play", "on_pause", "on_seek" ]`       |

---

### **GSS Styling Parameters**

| **Parameter**             | **Description**                                  | **Example**                                |
| ------------------------- | ------------------------------------------------ | ------------------------------------------ |
| `video.background`        | Background color for the video widget.            | `video.background = "#000"`              |
| `video.controls`          | Styling for the playback controls.                | `video.controls = { button.color = "#FFF", progress_bar.color = "#007BFF" }` |
| `video.progress_bar`      | Styling for the progress bar.                     | `video.progress_bar = { height = "8px", background = "#333" }` |
| `video.volume_slider`     | Styling for the volume slider.                    | `video.volume_slider = { color = "#007BFF" }` |
| `video.subtitles`         | Styling for subtitles.                           | `video.subtitles = { font-size = "16px", color = "#FFF", background = "rgba(0, 0, 0, 0.5)" }` |
| `video.mini_mode`         | Styling for the mini mode player.                | `video.mini_mode = { size = "200px", position = "bottom-right" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "video"
source = "@Live://channel/tutorial_stream"
subtitles = "@SQeeL://videos/tutorial_subs.srt"
autoplay = true
loop = true
playback_speeds = [ 0.5, 1.0, 1.5, 2.0 ]
default_speed = 1.0
chapters = [
    { title = "Introduction", time = "00:00:00" },
    { title = "Main Content", time = "00:05:00" },
    { title = "Conclusion", time = "00:10:00" }
]
intents = [ "on_play", "on_pause", "on_seek", "on_volume_change" ]
```

---

### **Example GSS Implementation**

```toml
[video]
background = "#000"

[video.controls]
button.color = "#FFF"
button.hover.color = "#CCC"
progress_bar.color = "#007BFF"
progress_bar.background = "#333"
progress_bar.height = "8px"
volume_slider.color = "#007BFF"
volume_slider.background = "#333"

[video.subtitles]
font-size = "16px"
color = "#FFF"
background = "rgba(0, 0, 0, 0.5)"
position = "bottom"

[video.mini_mode]
size = "200px"
position = "bottom-right"
background = "#111"
controls = { button.color = "#FFF", button.hover.color = "#CCC" }
```

---

### **Advanced Considerations**

1. **Highlighting Sections**:
   - Progress bars can include highlights based on user interaction data.

2. **Chapter Navigation**:
   - Users can navigate to specific sections using chapter markers.

3. **Closed Captions (CC)**:
   - Support for multiple subtitle tracks and on-the-fly switching.

4. **Accessibility and Customization**:
   - Keyboard shortcuts and screen-reader support ensure inclusivity.
   - GSS customization for every control element allows tailored user experiences.

5. **Custom UI Layouts**:
   - GSS allows advanced control layouts, such as overlays on the video, separate control windows, or mobile-friendly media controls.

6. **Fill-Screen and Mini Mode Enhancements**:
   - Enable seamless transitions between different viewing modes.

---

### **Use Cases**
- **Tutorial Applications**: Embedding videos with chapters and progress tracking.
- **Learning Platforms**: Supporting subtitles, playback speed adjustments, and chapter navigation.
- **Media Applications**: Building foundational video players for larger media workflows.
- **Live Streaming**: Seamless integration with the Live co-chain for broadcasting and consuming streamed content.

---

### **Conclusion**

The Video Widget is a robust and adaptable component for video playback. With support for AVX encoding, subtitle styling, dynamic content updates, and Live co-chain integration, it sets the stage for a seamless user experience while maintaining flexibility for diverse applications.

---

### **Popup Widget**

**Popup**: Creates modals for warnings, errors, confirmations, or informational messages. These popups provide a flexible and customizable way to communicate with users through a focused interface.

---

### **Core Features**

1. **Structured Layout**:
   - **Header/Title**: A concise title summarizing the purpose of the popup.
   - **Description**: A detailed message or explanation.
   - **Buttons**: Actionable buttons such as "OK," "Cancel," or "Report."

2. **Customizable Design**:
   - GSS designers can define the size, position, and styling of the popup.
   - Includes options for fixed, draggable, or resizable popups.
   - Supports customization based on popup types (e.g., warning, error, confirmation, informational).

3. **Event Triggers**:
   - Supports events such as `on_open`, `on_close`, and `on_action`.
   - Popups can be triggered by user actions, co-chain events, or system events.

4. **Types of Popups**:
   - **Warning**: Alerts the user to a potential issue or risk.
   - **Error**: Notifies the user of a failure or problem.
   - **Confirmation**: Requests user approval for an action.
   - **Informational**: Provides additional details or guidance.

5. **Dynamic Content**:
   - Content can be dynamically updated via co-chains like Mimic or SQeeL.
   - Can display data fetched in real time (e.g., error logs, form validation feedback).

6. **Accessibility Features**:
   - Fully navigable via keyboard and screen readers.
   - Support for high contrast modes.

7. **Animations and Sounds**:
   - Entrance and exit animations (e.g., fade, slide, zoom).
   - Custom sound effects specific to each popup type can be defined in GSS.

---

### **M3L Fields**

| **Field**        | **Description**                                    | **Example**                                              |
| ---------------- | -------------------------------------------------- | -------------------------------------------------------- |
| `type`           | Specifies the type of popup.                       | `type = "warning"`                                      |
| `header`         | Title text for the popup.                          | `header = "System Warning"`                             |
| `description`    | Main content of the popup.                         | `description = "Your session is about to expire."`      |
| `buttons`        | Array of button definitions.                       | `buttons = [ { label = "OK", intent = "on_close" }, { label = "Report", intent = "on_report" } ]` |
| `intents`        | Specifies popup-level interactions.                | `intents = [ "on_open", "on_close", "on_action" ]`      |
| `dynamic_source` | Dynamically fetches content for the popup.          | `dynamic_source = "@SQeeL://popup_content.db"`          |

---

### **GSS Styling Parameters**

| **Parameter**              | **Description**                                      | **Example**                                |
| -------------------------- | ---------------------------------------------------- | ------------------------------------------ |
| `popup.background`         | Background color of the popup.                       | `popup.background = "#FFF"`              |
| `popup.border`             | Border styling for the popup.                        | `popup.border = "1px solid #CCC"`        |
| `popup.header`             | Styling for the popup header.                        | `popup.header = { font-size = "18px", color = "#000" }` |
| `popup.description`        | Styling for the description text.                    | `popup.description = { font-size = "14px", color = "#333" }` |
| `popup.buttons`            | Styling for buttons within the popup.                | `popup.buttons = { button.color = "#FFF", button.background = "#007BFF" }` |
| `popup.warning`            | Custom styling for warning popups.                   | `popup.warning = { background = "#FFF3CD", border = "1px solid #FFEEBA" }` |
| `popup.error`              | Custom styling for error popups.                     | `popup.error = { background = "#F8D7DA", border = "1px solid #F5C6CB" }` |
| `popup.confirmation`       | Custom styling for confirmation popups.              | `popup.confirmation = { background = "#D4EDDA", border = "1px solid #C3E6CB" }` |
| `popup.informational`      | Custom styling for informational popups.             | `popup.informational = { background = "#D1ECF1", border = "1px solid #BEE5EB" }` |
| `popup.animations`         | Entrance and exit animations for the popup.          | `popup.animations = { entrance = "fade-in", exit = "slide-out" }` |
| `popup.sounds.warning`     | Custom sound for warning popups.                     | `popup.sounds.warning = "warning_sound.mp3"`            |
| `popup.sounds.error`       | Custom sound for error popups.                       | `popup.sounds.error = "error_sound.mp3"`                |
| `popup.sounds.confirmation`| Custom sound for confirmation popups.                | `popup.sounds.confirmation = "confirmation_sound.mp3"`  |
| `popup.sounds.informational`| Custom sound for informational popups.              | `popup.sounds.informational = "info_sound.mp3"`         |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "popup"
header = "Session Timeout"
description = "Your session is about to expire. Please save your work or extend your session."
buttons = [
    { label = "OK", intent = "on_close" },
    { label = "Extend Session", intent = "on_extend" },
    { label = "Report", intent = "on_report" }
]
intents = [ "on_open", "on_close", "on_action" ]
dynamic_source = "@SQeeL://popup_content.db"
```

---

### **Example GSS Implementation**

```toml
[popup]
background = "#FFF"
border = "1px solid #CCC"

[popup.header]
font-size = "18px"
color = "#000"

[popup.description]
font-size = "14px"
color = "#333"

[popup.buttons]
button.color = "#FFF"
button.background = "#007BFF"
button.hover.color = "#0056B3"

[popup.warning]
background = "#FFF3CD"
border = "1px solid #FFEEBA"

[popup.error]
background = "#F8D7DA"
border = "1px solid #F5C6CB"

[popup.confirmation]
background = "#D4EDDA"
border = "1px solid #C3E6CB"

[popup.informational]
background = "#D1ECF1"
border = "1px solid #BEE5EB"

[popup.animations]
entrance = "fade-in"
exit = "slide-out"

[popup.sounds]
warning = "warning_sound.mp3"
error = "error_sound.mp3"
confirmation = "confirmation_sound.mp3"
informational = "info_sound.mp3"
```

---

### **Advanced Considerations**

1. **Dynamic Content Integration**:
   - Leverage co-chains like SQeeL to fetch real-time content or suggestions.

2. **Multi-Step Popups**:
   - Support for wizard-style or sequential popups to guide users through complex workflows.

3. **Error Handling**:
   - Automatically trigger popups in response to system errors or validation failures.

4. **Custom Interaction Logic**:
   - Allow developers to bind popups to specific intents (e.g., closing other widgets upon confirmation).

5. **GSS Flexibility**:
   - Define popups for various screen sizes and input methods, ensuring responsiveness and usability.

---

### **Use Cases**
- **Warnings**: Alert users about critical actions or system states.
- **Errors**: Provide detailed error messages with actionable buttons.
- **Confirmations**: Obtain user consent before performing an irreversible action.
- **Information**: Share updates or contextual guidance.

---

### **Conclusion**

The Popup Widget provides a flexible and visually customizable method for engaging users with critical information or interactions. With GSS and co-chain integration, it adapts seamlessly to a variety of use cases and device types.

---

### **Notification Panel Widget**

**Notification Panel**: This widget provides a comprehensive listing of notifications specific to the application being used. Notifications may include system messages, updates, errors, warnings, or other user-relevant information. It works as part of a two-part system in conjunction with transient widgets like the Toast widget. Users can revisit dismissed or timed-out messages and interact with the Notification Panel through shortcuts, settings menus, or dedicated notification buttons.

> **Note**: The Notification Panel is distinct from the UndChain primary notification system. Applications wishing to post in the master notification system must explicitly request user permission. This distinction ensures application-specific notifications remain separate from the user's primary notifications.

---

### **Core Features**

1. **Structured Layout**:

   - Displays notifications in a list format, with the newest notifications appearing at the top (or as defined by the GSS designer).
   - Each notification can include:
     - **Type**: Warning, Error, Information, Confirmation, etc.
     - **Timestamp**: When the notification was generated.
     - **Message**: A brief description or title.
     - **Details**: Optional additional information.
     - **Persistence**: Identifies whether a notification persists across sessions (default is temporary).

2. **Interaction Options**:

   - Users can dismiss individual notifications via a dedicated button or clear all notifications at once.
   - Expandable notifications for detailed views.
   - Users can open the Notification Panel via a button, shortcut, or settings menu.

3. **Customizable Design**:

   - GSS defines the layout, color schemes, and animations.
   - Supports icons for notification types (e.g., warning icon, confirmation checkmark).
   - Includes two icons for the notification button: one for standard use and another to indicate unread notifications.

4. **Event Integration**:

   - Notifications can be dynamically added via intents triggered by application events.
   - Persistent storage for notifications fetched from co-chains like Mimic or SQeeL can be used.

5. **Accessibility Features**:

   - Fully navigable via keyboard or screen readers.
   - Support for high contrast modes.

6. **Animation and Sounds**:

   - Entrance and exit animations for notifications (e.g., slide-in, fade-out).
   - Sounds are primarily used for dismiss actions, with other notification sounds handled before being added to the panel.

7. **Categories and Filtering**:

   - Group notifications by type or priority.
   - Search and filter options for large lists.

---

### **M3L Fields**

| **Field**           | **Description**                                | **Example**                                               |
| ------------------- | ---------------------------------------------- | --------------------------------------------------------- |
| `type`              | Specifies the type of notification panel.      | `type = "notification_panel"`                            |
| `intents`           | Specifies actions for notification management. | `intents = [ "on_dismiss", "on_expand", "on_clear_all" ]` |
| `dynamic_source`    | Fetches notifications from a co-chain.         | `dynamic_source = "@SQeeL://notifications.db"`           |
| `max_notifications` | Limits the number of visible notifications.    | Defined in the GSS file.                                  |

---

### **GSS Styling Parameters**

| **Parameter**                   | **Description**                                 | **Example**                                                                               |
| ------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `notification_panel.background` | Background color of the notification panel.     | `notification_panel.background = "#FFF"`                                                  |
| `notification_panel.border`     | Border styling for the panel.                   | `notification_panel.border = "1px solid #CCC"`                                            |
| `notification_panel.title`      | Styling for the title text of the panel.        | `notification_panel.title = { font-size = "18px", color = "#000" }`                       |
| `notification_item`             | Styling for individual notification entries.    | `notification_item = { background = "#F9F9F9", border = "1px solid #EEE" }`               |
| `notification_item.warning`     | Custom styling for warning notifications.       | `notification_item.warning = { color = "#856404", background = "#FFF3CD" }`               |
| `notification_item.error`       | Custom styling for error notifications.         | `notification_item.error = { color = "#721C24", background = "#F8D7DA" }`                 |
| `notification_item.success`     | Custom styling for success notifications.       | `notification_item.success = { color = "#155724", background = "#D4EDDA" }`               |
| `notification_item.info`        | Custom styling for informational notifications. | `notification_item.info = { color = "#0C5460", background = "#D1ECF1" }`                  |
| `notification_item.animations`  | Entrance and exit animations for notifications. | `notification_item.animations = { entrance = "slide-in", exit = "fade-out" }`             |
| `notification_item.sounds`      | Custom sounds for specific notification types.  | `notification_item.sounds = { warning = "warning_sound.mp3", error = "error_sound.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "notification_panel"
dynamic_source = "@SQeeL://notifications.db"
intents = [ "on_dismiss", "on_expand", "on_clear_all" ]
```

---

### **Example GSS Implementation**

```toml
[notification_panel]
background = "#FFF"
border = "1px solid #CCC"

[notification_panel.title]
font-size = "18px"
color = "#000"

[notification_item]
background = "#F9F9F9"
border = "1px solid #EEE"

[notification_item.warning]
color = "#856404"
background = "#FFF3CD"

[notification_item.error]
color = "#721C24"
background = "#F8D7DA"

[notification_item.success]
color = "#155724"
background = "#D4EDDA"

[notification_item.info]
color = "#0C5460"
background = "#D1ECF1"

[notification_item.animations]
entrance = "slide-in"
exit = "fade-out"

[notification_item.sounds]
warning = "warning_sound.mp3"
error = "error_sound.mp3"
success = "success_sound.mp3"
info = "info_sound.mp3"
```

---

### **Advanced Considerations**

1. **Toast Integration**:

   - Notifications generated by the Toast widget can persist in the Notification Panel.

2. **Custom Filtering**:

   - Allow users to filter notifications by type, priority, or time range.

3. **Mobile-Friendly Design**:

   - Ensure responsiveness for smaller screens, with collapsible or scrollable layouts.

4. **Search Functionality**:

   - Enable users to search for specific notifications.

5. **Dynamic Updates**:

   - Synchronize with co-chains like Mimic or SQeeL for real-time notification updates.

---

### **Use Cases**

- **Error Logs**: Track system errors and issues in one location.
- **User Activity**: Notify users about completed tasks, updates, or changes.
- **System Updates**: Inform users of critical application or system events.
- **Persistent Notifications**: Provide a history of important notifications for reference.

---

### **Conclusion**

The Notification Panel Widget serves as a centralized hub for managing and viewing application notifications. Its seamless integration with other widgets like Toast ensures users remain informed while maintaining flexibility and customization for developers.

---

### **Toast Widget**

**Toast**: A temporary, transient notification that briefly appears on the screen and automatically disappears after a set amount of time. Toast messages are typically used to convey short-term, non-critical information to users and are archived in the Notification Panel for later reference.

---

### **Core Features**

1. **Predefined Types**:
   - **Warning**: Alerts the user to a potential issue.
   - **Error**: Notifies the user of a failure or problem.
   - **Confirmation**: Confirms the successful completion of an action.
   - **Informational**: Provides additional details or updates.

2. **Customizable Design**:
   - GSS defines the placement, appearance, and animations of toast messages.
   - Supports icons and styling specific to each type.
   - Allows designers to define screen positions (e.g., top-right, bottom-center).

3. **Timing Options**:
   - Default duration for each toast type (e.g., 5 seconds).
   - Customizable duration via M3L field or GSS.
   - Option to make toast persistent until dismissed by the user.

4. **Event Integration**:
   - Supports intents such as `on_show` and `on_dismiss`.
   - Automatically logs to the Notification Panel after dismissal or expiration.

5. **Accessibility Features**:
   - Fully navigable via keyboard and screen readers.
   - Support for high contrast modes and assistive technologies.

6. **Animation and Sounds**:
   - Unified animation and sound control, allowing synchronized feedback.
   - Designers can define delays, offsets, and interaction-specific sound effects.

---

### **M3L Fields**

| **Field**          | **Description**                                   | **Example**                                               |
| ------------------ | ------------------------------------------------- | --------------------------------------------------------- |
| `type`             | Specifies the type of toast.                      | `type = "confirmation"`                                 |
| `message`          | Main content of the toast.                        | `message = "Your settings have been saved successfully."`|
| `duration`         | Duration before the toast disappears (in seconds).| `duration = 5`                                           |
| `intents`          | Specifies actions for toast events.               | `intents = [ "on_show", "on_dismiss" ]`                 |

---

### **GSS Styling Parameters**

| **Parameter**           | **Description**                                      | **Example**                                |
| ----------------------- | ---------------------------------------------------- | ------------------------------------------ |
| `toast.background`      | Background color for all toast messages.             | `toast.background = "#FFF"`              |
| `toast.border`          | Border styling for the toast.                        | `toast.border = "1px solid #CCC"`        |
| `toast.position`        | Placement on the screen (e.g., top-right).           | `toast.position = "bottom-right"`         |
| `toast.animations`      | Unified entrance and exit animations with sounds.    | `toast.animations = { entrance = { type = "fade-in", duration = "0.5s", sound = { file = "confirmation_sound.mp3", delay = "0.1s" } }, exit = { type = "slide-up", duration = "0.5s" } }` |
| `toast.warning`         | Custom styling for warning toasts.                   | `toast.warning = { background = "#FFF3CD", border = "1px solid #FFEEBA", sound = { file = "warning_sound.mp3", delay = "0s" } }` |
| `toast.error`           | Custom styling for error toasts.                     | `toast.error = { background = "#F8D7DA", border = "1px solid #F5C6CB", sound = { file = "error_sound.mp3", delay = "0s" } }` |
| `toast.confirmation`    | Custom styling for confirmation toasts.              | `toast.confirmation = { background = "#D4EDDA", border = "1px solid #C3E6CB", sound = { file = "confirmation_sound.mp3", delay = "0.1s" } }` |
| `toast.info`            | Custom styling for informational toasts.             | `toast.info = { background = "#D1ECF1", border = "1px solid #BEE5EB", sound = { file = "info_sound.mp3", delay = "0.2s" } }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "toast"
message = "Your settings have been saved successfully."
duration = 5
intents = [ "on_show", "on_dismiss" ]
```

---

### **Example GSS Implementation**

```toml
[toast]
background = "#FFF"
border = "1px solid #CCC"
position = "bottom-right"

[toast.animations]
entrance = { type = "fade-in", duration = "0.5s", sound = { file = "confirmation_sound.mp3", delay = "0.1s" } }
exit = { type = "slide-up", duration = "0.5s" }

[toast.warning]
background = "#FFF3CD"
border = "1px solid #FFEEBA"
sound = { file = "warning_sound.mp3", delay = "0s" }

[toast.error]
background = "#F8D7DA"
border = "1px solid #F5C6CB"
sound = { file = "error_sound.mp3", delay = "0s" }

[toast.confirmation]
background = "#D4EDDA"
border = "1px solid #C3E6CB"
sound = { file = "confirmation_sound.mp3", delay = "0.1s" }

[toast.info]
background = "#D1ECF1"
border = "1px solid #BEE5EB"
sound = { file = "info_sound.mp3", delay = "0.2s" }
```

---

### **Advanced Considerations**

1. **Notification Panel Integration**:
   - Toast messages are automatically logged into the Notification Panel after expiration or dismissal.

2. **Custom Timing**:
   - Allow users to override the default duration for specific toast types (e.g., error messages last longer).

3. **Dynamic Positioning**:
   - GSS can define responsive positions for toasts based on screen size or orientation.

4. **Sound and Animation Coordination**:
   - Synchronize sound effects with entrance animations to improve user feedback.

5. **Mobile Optimization**:
   - Ensure proper scaling and placement for smaller devices.

---

### **Use Cases**
- **Action Confirmation**: Display confirmation messages after user actions (e.g., saving settings).
- **Temporary Alerts**: Inform users of short-term updates (e.g., "Server will restart in 5 minutes").
- **Error Notifications**: Provide quick feedback on failures, like form validation errors.
- **Informational Messages**: Show helpful tips or non-urgent updates.

---

### **Conclusion**

The Toast Widget is a lightweight and visually engaging way to deliver temporary notifications. With robust GSS customization and seamless integration into the Notification Panel, it provides a user-friendly mechanism for transient messaging while ensuring users can review past messages if needed.

---

### **Date Picker Widget**

**Date Picker**: A widget designed to allow users to easily select and sanitize dates. It provides an intuitive interface for date selection and ensures consistent formatting and validation. Two modes, **macro** and **mini**, offer GSS designers flexibility in integrating the widget into various layouts.

---

### **Core Features**

1. **Modes**:
   - **Macro**: A larger, calendar-style interface for comprehensive date browsing and selection.
   - **Mini**: A compact, dropdown-style interface for quick date selection, ideal for limited screen space.

2. **Customizable Design**:
   - GSS defines the layout, colors, fonts, and animations for the widget.
   - Designers can toggle between macro and mini modes based on user input or screen size.

3. **Date Validation**:
   - Ensures selected dates fall within a specified range.
   - Prevents invalid dates (e.g., February 30).
   - Supports dynamic date constraints (e.g., disallow past dates).

4. **Event Integration**:
   - Intents such as `on_date_select`, `on_clear`, and `on_error` enable seamless integration with application workflows.
   - Supports interactions like hovering, clicking, or tapping.

5. **Accessibility Features**:
   - Fully navigable via keyboard or screen readers.
   - Support for high contrast modes and assistive technologies.

6. **Animation and Sounds**:
   - Entrance and exit animations for the date picker.
   - Optional sounds for date selection, validation errors, and clearing selections.

---

### **M3L Fields**

| **Field**        | **Description**                                   | **Example**                                              |
| ---------------- | ------------------------------------------------- | -------------------------------------------------------- |
| `type`           | Specifies the widget type.                        | `type = "date_picker"`                                  |
| `mode`           | Determines the mode of the date picker.           | `mode = "macro"` or `mode = "mini"`                   |
| `range`          | Defines the valid date range.                     | `range = { start = "2024-01-01", end = "2024-12-31" }`|
| `intents`        | Specifies actions for widget events.              | `intents = [ "on_date_select", "on_clear", "on_error" ]` |
| `dynamic_source` | Fetches date-related constraints dynamically.     | `dynamic_source = "@SQeeL://date_constraints.db"`      |

---

### **GSS Styling Parameters**

| **Parameter**           | **Description**                                    | **Example**                                 |
| ----------------------- | -------------------------------------------------- | ------------------------------------------- |
| `date_picker.background`| Background color of the date picker widget.         | `date_picker.background = "#FFF"`         |
| `date_picker.border`    | Border styling for the date picker.                 | `date_picker.border = "1px solid #CCC"`   |
| `date_picker.font`      | Font styling for dates in the widget.               | `date_picker.font = { size = "14px", color = "#000" }` |
| `date_picker.mode`      | Custom styling for macro or mini modes.             | `date_picker.mode.macro = { spacing = "10px" }` |
| `date_picker.animations`| Entrance and exit animations for the widget.        | `date_picker.animations = { entrance = "fade-in", exit = "slide-out" }` |
| `date_picker.sounds`    | Sounds for specific interactions (optional).        | `date_picker.sounds = { select = "click.mp3", error = "error.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "date_picker"
mode = "macro"
range = { start = "2024-01-01", end = "2024-12-31" }
dynamic_source = "@SQeeL://date_constraints.db"
intents = [ "on_date_select", "on_clear", "on_error" ]
```

---

### **Example GSS Implementation**

```toml
[date_picker]
background = "#FFF"
border = "1px solid #CCC"

[date_picker.font]
size = "14px"
color = "#000"

[date_picker.mode.macro]
spacing = "10px"

[date_picker.mode.mini]
spacing = "5px"

[date_picker.animations]
entrance = "fade-in"
exit = "slide-out"

[date_picker.sounds]
select = "click.mp3"
error = "error.mp3"
clear = "clear.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Constraints**
   - Use co-chains like SQeeL to fetch dynamic date constraints (e.g., blackout dates).

#### **Responsive Design**
   - GSS enables switching between macro and mini modes for mobile-friendly design.

#### **Localization Support**
   - Enable different date formats (e.g., MM/DD/YYYY, DD/MM/YYYY) based on locale settings.

---

### **Use Cases**
- **Event Scheduling**: Allow users to select dates for events, bookings, or deadlines.
- **Range Selection**: Let users choose start and end dates for reports or timelines.
- **Dynamic Calendars**: Integrate with co-chains for live updates, such as holidays or blackout dates.

---

### **Conclusion**

The Date Picker Widget provides a streamlined and visually customizable way to handle date selection in applications. Its flexible modes and robust features ensure it meets the needs of diverse applications while maintaining ease of use and accessibility.

---

### **Color Picker Widget**

**Color Picker**: A widget that allows users to select a color, typically from a palette. The widget supports customizable palettes and multiple modes for varying levels of detail and interaction.

---

### **Core Features**

1. **Modes**:
   - **Macro**: A larger interface providing a full-spectrum color palette, with options to adjust hue, saturation, and brightness.
   - **Mini**: A compact interface offering a simplified palette or a predefined set of colors.

2. **Customizable Palettes**:
   - GSS designers can define custom color palettes to match application themes or user requirements.
   - Default palette includes a full rainbow spectrum.

3. **Dynamic Color Ranges**:
   - Enables users to select colors within defined ranges (e.g., brand-specific colors).
   - Supports co-chain integration for dynamically updating palettes (e.g., pulling theme colors from a design system).

4. **Event Integration**:
   - Intents such as `on_color_select`, `on_clear`, and `on_error` allow seamless integration with application workflows.
   - Triggers for hover, click, or drag interactions.

5. **Accessibility Features**:
   - Keyboard navigation and screen reader support for color descriptions.
   - High contrast mode and visual indicators for selected colors.

6. **Animation and Sounds**:
   - Entrance and exit animations to make the picker feel engaging.
   - Optional sounds for selecting or clearing colors.

---

### **M3L Fields**

| **Field**        | **Description**                                   | **Example**                                              |
| ---------------- | ------------------------------------------------- | -------------------------------------------------------- |
| `type`           | Specifies the widget type.                        | `type = "color_picker"`                                 |
| `mode`           | Determines the mode of the color picker.          | `mode = "macro"` or `mode = "mini"`                   |
| `palette`        | Defines a custom palette of colors.               | `palette = [ "#FF0000", "#00FF00", "#0000FF" ]`       |
| `intents`        | Specifies actions for widget events.              | `intents = [ "on_color_select", "on_clear", "on_error" ]` |
| `dynamic_source` | Fetches palette data dynamically.                 | `dynamic_source = "@SQeeL://palette.db"`               |

---

### **GSS Styling Parameters**

| **Parameter**           | **Description**                                    | **Example**                                |
| ----------------------- | -------------------------------------------------- | ------------------------------------------ |
| `color_picker.background` | Background color of the color picker widget.       | `color_picker.background = "#FFF"`       |
| `color_picker.border`    | Border styling for the widget.                     | `color_picker.border = "1px solid #CCC"` |
| `color_picker.font`      | Font styling for labels or color descriptions.      | `color_picker.font = { size = "14px", color = "#000" }` |
| `color_picker.mode`      | Custom styling for macro or mini modes.             | `color_picker.mode.macro = { spacing = "10px" }` |
| `color_picker.animations`| Entrance and exit animations for the widget.        | `color_picker.animations = { entrance = "fade-in", exit = "slide-out" }` |
| `color_picker.sounds`    | Sounds for specific interactions (optional).        | `color_picker.sounds = { select = "click.mp3", clear = "clear.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "color_picker"
mode = "macro"
palette = [ "#FF0000", "#00FF00", "#0000FF" ]
dynamic_source = "@SQeeL://palette.db"
intents = [ "on_color_select", "on_clear", "on_error" ]
```

---

### **Example GSS Implementation**

```toml
[color_picker]
background = "#FFF"
border = "1px solid #CCC"

[color_picker.font]
size = "14px"
color = "#000"

[color_picker.mode.macro]
spacing = "10px"

[color_picker.mode.mini]
spacing = "5px"

[color_picker.animations]
entrance = "fade-in"
exit = "slide-out"

[color_picker.sounds]
select = "click.mp3"
clear = "clear.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Palettes**
   - Use co-chains like SQeeL to fetch and update palettes dynamically based on user or application needs.

#### **Responsive Design**
   - GSS enables switching between macro and mini modes for mobile-friendly design.

#### **Localization Support**
   - Support for localized color names or descriptions (e.g., "Scarlet Red" instead of "#FF0000").

---

### **Use Cases**
- **Brand Design**: Allow users to select brand-approved colors.
- **Theming**: Enable customization of UI themes or assets.
- **Art Tools**: Provide precise color selection for creative applications.

---

### **Conclusion**

The Color Picker Widget offers a versatile and visually customizable way to handle color selection. Its flexible modes and robust features ensure it meets the needs of diverse applications while maintaining ease of use and accessibility.

---

### **Tree View Widget**

**Tree View**: A widget designed to represent hierarchical data such as directories, categories, or nested structures. This widget allows users to navigate, expand, collapse, and interact with nodes in a clear and organized manner.

---

### **Core Features**

1. **Node Management**:
   - **Expandable and Collapsible Nodes**: Users can expand or collapse nodes to navigate the hierarchy.
   - **Dynamic Loading**: Nodes can fetch child elements dynamically from co-chains (e.g., loading directories or subcategories).

2. **Customizable Design**:
   - GSS allows customization of icons, colors, fonts, and animations for nodes.
   - Supports node-specific styling (e.g., highlight active nodes).

3. **Interaction Options**:
   - **Single-Select or Multi-Select**: Users can interact with one or multiple nodes.
   - **Drag-and-Drop**: Nodes can be reordered or moved within the tree structure.
   - **Context Menu Integration**: Supports floating menus for node-specific actions (e.g., rename, delete).

4. **Search and Filtering**:
   - Integrate a search bar for filtering visible nodes based on user input.
   - Highlight matching nodes during searches.

5. **Accessibility Features**:
   - Fully navigable via keyboard or screen readers.
   - Support for high contrast modes and visual indicators.

6. **Animation and Sounds**:
   - Entrance and exit animations for nodes (e.g., fade-in, slide-down).
   - Optional sounds for expanding or collapsing nodes.

---

### **M3L Fields**

| **Field**        | **Description**                                   | **Example**                                               |
| ---------------- | ------------------------------------------------- | --------------------------------------------------------- |
| `type`           | Specifies the widget type.                        | `type = "tree_view"`                                     |
| `dynamic_source` | Fetches hierarchical data dynamically.            | `dynamic_source = "@SQeeL://directory_structure.db"`     |
| `intents`        | Specifies actions for widget events.              | `intents = [ "on_select", "on_expand", "on_collapse" ]` |

---

### **GSS Styling Parameters**

| **Parameter**              | **Description**                                    | **Example**                                 |
| -------------------------- | -------------------------------------------------- | ------------------------------------------- |
| `tree_view.background`     | Background color of the tree view widget.          | `tree_view.background = "#FFF"`          |
| `tree_view.border`         | Border styling for the widget.                     | `tree_view.border = "1px solid #CCC"`    |
| `tree_view.font`           | Font styling for node labels.                      | `tree_view.font = { size = "14px", color = "#000" }` |
| `tree_view.node`           | Styling for individual nodes.                      | `tree_view.node = { padding = "5px" }`   |
| `tree_view.node.hover`     | Styling when a node is hovered.                    | `tree_view.node.hover = { background = "#EEE" }` |
| `tree_view.animations`     | Animations for expanding and collapsing nodes.     | `tree_view.animations = { expand = "slide-down", collapse = "slide-up" }` |
| `tree_view.sounds`         | Sounds for specific interactions (optional).       | `tree_view.sounds = { expand = "expand.mp3", collapse = "collapse.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "tree_view"
dynamic_source = "@SQeeL://directory_structure.db"
intents = [ "on_select", "on_expand", "on_collapse" ]
```

---

### **Example GSS Implementation**

```toml
[tree_view]
background = "#FFF"
border = "1px solid #CCC"

[tree_view.font]
size = "14px"
color = "#000"

[tree_view.node]
padding = "5px"

[tree_view.node.hover]
background = "#EEE"

[tree_view.animations]
expand = "slide-down"
collapse = "slide-up"

[tree_view.sounds]
expand = "expand.mp3"
collapse = "collapse.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Data Loading**
   - Use co-chains like SQeeL to dynamically fetch child nodes, enabling efficient navigation of large hierarchies.

#### **Responsive Design**
   - Ensure the widget adapts to various screen sizes and orientations.

#### **Localization Support**
   - Support for localized node labels and tooltips.

---

### **Use Cases**
- **File Browsers**: Navigate through directories and subdirectories.
- **Category Navigation**: Represent nested product categories in e-commerce.
- **Organizational Charts**: Visualize hierarchical relationships in teams or projects.

---

### **Conclusion**

The Tree View Widget is a versatile tool for navigating hierarchical data structures. Its customizable design, dynamic data loading, and robust interaction options make it suitable for a wide range of applications, from file browsers to organizational charts.

---

### **Object Tree Widget**

**Object Tree**: A widget designed for managing hierarchical objects with advanced interaction options. Unlike the Tree View Widget, the Object Tree supports property editing, visual connections, and customizable behaviors for each object in the hierarchy.

---

### **Core Features**

1. **Advanced Node Management**:
   - **Property Editing**: Inline editing for attributes and properties of objects.
   - **Expandable and Collapsible Nodes**: Users can expand or collapse nodes to navigate complex hierarchies.
   - **Multi-Select and Group Operations**: Enable bulk operations on selected objects.

2. **Visual Connections**:
   - **Node Relationships**: Show relationships between nodes using visual connectors (e.g., lines or arrows).
   - **Drag-and-Drop Connections**: Allow users to establish relationships between nodes dynamically.

3. **Customizable Node Behavior**:
   - GSS defines unique behaviors and styles for different object types.
   - Enable context-sensitive actions such as linking, duplicating, or deleting nodes.

4. **Dynamic Data Loading**:
   - Fetch object data dynamically from co-chains like SQeeL or Code Ledger.
   - Supports large datasets by loading child nodes on demand.

5. **Accessibility Features**:
   - Fully navigable via keyboard or screen readers.
   - High contrast mode for better visibility.

6. **Animation and Sounds**:
   - Entrance and exit animations for nodes and relationships.
   - Optional sounds for interactions such as linking or editing objects.

---

### **M3L Fields**

| **Field**        | **Description**                                   | **Example**                                               |
| ---------------- | ------------------------------------------------- | --------------------------------------------------------- |
| `type`           | Specifies the widget type.                        | `type = "object_tree"`                                   |
| `dynamic_source` | Fetches hierarchical object data dynamically.     | `dynamic_source = "@SQeeL://object_hierarchy.db"`       |
| `intents`        | Specifies actions for widget events.              | `intents = [ "on_select", "on_expand", "on_edit", "on_link" ]` |

---

### **GSS Styling Parameters**

| **Parameter**              | **Description**                                    | **Example**                                 |
| -------------------------- | -------------------------------------------------- | ------------------------------------------- |
| `object_tree.background`   | Background color of the object tree widget.        | `object_tree.background = "#FFF"`        |
| `object_tree.border`       | Border styling for the widget.                     | `object_tree.border = "1px solid #CCC"`   |
| `object_tree.font`         | Font styling for object labels.                    | `object_tree.font = { size = "14px", color = "#000" }` |
| `object_tree.node`         | Styling for individual nodes.                      | `object_tree.node = { padding = "5px" }`  |
| `object_tree.node.hover`   | Styling when a node is hovered.                    | `object_tree.node.hover = { background = "#EEE" }` |
| `object_tree.connection`   | Visual styling for node connectors.                | `object_tree.connection = { color = "#888", width = "2px" }` |
| `object_tree.animations`   | Animations for node interactions.                  | `object_tree.animations = { link = "fade-in", unlink = "fade-out" }` |
| `object_tree.sounds`       | Sounds for specific interactions (optional).       | `object_tree.sounds = { edit = "edit.mp3", link = "link.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "object_tree"
dynamic_source = "@SQeeL://object_hierarchy.db"
intents = [ "on_select", "on_expand", "on_edit", "on_link" ]
```

---

### **Example GSS Implementation**

```toml
[object_tree]
background = "#FFF"
border = "1px solid #CCC"

[object_tree.font]
size = "14px"
color = "#000"

[object_tree.node]
padding = "5px"

[object_tree.node.hover]
background = "#EEE"

[object_tree.connection]
color = "#888"
width = "2px"

[object_tree.animations]
link = "fade-in"
unlink = "fade-out"

[object_tree.sounds]
edit = "edit.mp3"
link = "link.mp3"
```

---

### **Advanced Considerations**

#### **Custom Node Types**
   - Allow developers to define custom node types with unique properties and interactions.

#### **Integration with Co-Chains**
   - Use co-chains like SQeeL or Code Ledger to fetch and update object data dynamically.

#### **Responsive Design**
   - Adapt node layouts and connectors for different screen sizes and orientations.

#### **Localization Support**
   - Support for localized object names and tooltips.

---

### **Use Cases**
- **3D Object Management**: Manage 3D assets in a game or simulation.
- **Application State Trees**: Visualize and manipulate the state hierarchy of an application.
- **Organizational Charts**: Represent complex team structures with properties for each team member.

---

### **Conclusion**

The Object Tree Widget is a powerful tool for managing hierarchical data with advanced interactions. Its property editing, visual connections, and dynamic loading capabilities make it ideal for use cases requiring detailed control over object relationships and attributes.

---

### **Poll Widget**

**Poll Widget**: A widget designed to present multiple-choice questions and display aggregated results. This widget is ideal for collecting user feedback, conducting surveys, or facilitating quick audience polls. The system defaults to two options, with the ability to scale to multiple options. Additionally, users can write in their own answers if this feature is enabled. All polls must have at least two options; otherwise, you are polling for engagement, which is a different widget type.

---

### **Core Features**

1. **Multiple Choice Options**:

   - Supports two or multiple-selection polls.
   - Customizable number of options.
   - Optional user-submitted answers, enabling greater flexibility and engagement.

2. **Aggregated Results**:

   - Displays results dynamically as users vote.
   - GSS designers can define result display types (e.g., percentages, absolute counts, or graphical bars).

3. **Dynamic Updates**:

   - Results update in real-time when connected to a co-chain like SQeeL.
   - Supports anonymous and authenticated voting.

4. **Customizable Design**:

   - GSS allows full control over the appearance of the poll, including option styling, fonts, and colors.
   - Supports progress animations for results.

5. **Accessibility Features**:

   - Fully navigable via keyboard or screen readers.
   - High contrast mode for better visibility.

6. **Animation and Sounds**:

   - Entrance and exit animations for poll options and results.
   - Optional sounds for voting and result updates.

---

### **M3L Fields**

| **Field**          | **Description**                            | **Example**                                      |
| ------------------ | ------------------------------------------ | ------------------------------------------------ |
| `type`             | Specifies the widget type.                 | `type = "poll_widget"`                           |
| `question`         | The poll question.                         | `question = "What is your favorite color?"`      |
| `options`          | List of available answers.                 | `options = [ "Red", "Blue", "Green", "Yellow" ]` |
| `allow_multiple`   | Specifies if multiple answers are allowed. | `allow_multiple = false`                         |
| `allow_user_input` | Enables users to submit their own answers. | `allow_user_input = true`                        |
| `dynamic_source`   | Fetches poll results dynamically.          | `dynamic_source = "@SQeeL://poll_results.db"`    |
| `intents`          | Specifies actions for widget events.       | `intents = [ "on_vote", "on_result_update" ]`    |

---

### **GSS Styling Parameters**

| **Parameter**              | **Description**                            | **Example**                                                          |
| -------------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| `poll_widget.background`   | Background color of the poll widget.       | `poll_widget.background = "#FFF"`                                    |
| `poll_widget.border`       | Border styling for the widget.             | `poll_widget.border = "1px solid #CCC"`                              |
| `poll_widget.font`         | Font styling for the question and options. | `poll_widget.font = { size = "16px", color = "#000" }`               |
| `poll_widget.option`       | Styling for individual poll options.       | `poll_widget.option = { padding = "10px" }`                          |
| `poll_widget.option.hover` | Styling when an option is hovered.         | `poll_widget.option.hover = { background = "#EEE" }`                 |
| `poll_widget.results`      | Styling for the results display.           | `poll_widget.results = { type = "bar", color = "#00FF00" }`          |
| `poll_widget.animations`   | Animations for voting and result updates.  | `poll_widget.animations = { vote = "fade-in", results = "expand" }`  |
| `poll_widget.sounds`       | Sounds for interactions (optional).        | `poll_widget.sounds = { vote = "click.mp3", update = "update.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "poll_widget"
question = "What is your favorite color?"
options = [ "Red", "Blue", "Green", "Yellow" ]
allow_multiple = false
allow_user_input = true
dynamic_source = "@SQeeL://poll_results.db"
intents = [ "on_vote", "on_result_update" ]
```

---

### **Example GSS Implementation**

```toml
[poll_widget]
background = "#FFF"
border = "1px solid #CCC"

[poll_widget.font]
size = "16px"
color = "#000"

[poll_widget.option]
padding = "10px"

[poll_widget.option.hover]
background = "#EEE"

[poll_widget.results]
type = "bar"
color = "#00FF00"

[poll_widget.animations]
vote = "fade-in"
results = "expand"

[poll_widget.sounds]
vote = "click.mp3"
update = "update.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Data Loading**

- Use co-chains like SQeeL to fetch and update poll results in real-time.

#### **Responsive Design**

- Ensure the widget adapts to various screen sizes and orientations.

#### **Localization Support**

- Support for localized questions and options.

---

### **Use Cases**

- **Audience Engagement**: Conduct live polls during presentations or streams.
- **Feedback Collection**: Gather opinions on features or services.
- **Education**: Use for quizzes or quick knowledge checks.

---

### **Conclusion**

The Poll Widget is a versatile and engaging tool for gathering user input and displaying results. Its dynamic design and robust customization options make it suitable for a variety of applications, from audience engagement to data collection.

---

### **Rating Widget**

**Rating Widget**: A widget designed to collect user ratings for content or experiences. This widget supports various rating types and scales, with a minimum of two rating levels and a customizable upper limit of 100, as defined in the M3L file. The most common implementation is a five-star system, but developers can configure other formats (e.g., numerical scales or emojis). Ratings must be tied to a specific widget, ensuring context and relevance for each use case.

---

### **Core Features**

1. **Customizable Rating Scales**:
   - Supports 2 to 100 rating levels.
   - Options include stars, numerical values, emojis, or custom icons.
   - GSS designers can implement control systems to adjust designs based on the number of rating levels (e.g., a slider for more than 10 levels).

2. **Dynamic Feedback**:
   - Shows real-time feedback as users hover or select ratings.
   - Supports optional text labels for each rating level (e.g., "Poor", "Excellent").

3. **Aggregated Results**:
   - Displays average ratings dynamically when connected to co-chains like Pages.
   - Allows GSS designers to define result display types (e.g., graphical bars, percentages).

4. **Interaction Options**:
   - Intents such as `on_rate` and `on_clear` allow seamless integration into applications.
   - Ratings are tied to a specific widget, ensuring clear context for feedback.
   - Supports resetting ratings if enabled by the developer.

5. **Accessibility Features**:
   - Fully navigable via keyboard or screen readers.
   - High contrast mode for better visibility.

6. **Animation and Sounds**:
   - Entrance and exit animations for the widget.
   - Optional sounds for hovering, selecting, or clearing ratings.

---

### **M3L Fields**

| **Field**        | **Description**                                   | **Example**                                                |
| ---------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `type`           | Specifies the widget type.                        | `type = "rating_widget"`                                  |
| `scale`          | Defines the number of rating levels (max 100).    | `scale = 5`                                               |
| `labels`         | Optional text labels for each level.              | `labels = [ "Poor", "Fair", "Good", "Very Good", "Excellent" ]` |
| `icons`          | Custom icons for each rating level.               | `icons = [ "star", "star", "star", "star", "star" ]`       |
| `dynamic_source` | Fetches aggregated ratings dynamically.           | `dynamic_source = "@SQeeL://content_ratings.db"`         |
| `target_widget`  | Specifies the widget being rated.                 | `target_widget = "asset_card_1"`                         |
| `intents`        | Specifies actions for widget events.              | `intents = [ "on_rate", "on_clear" ]`                     |

---

### **GSS Styling Parameters**

| **Parameter**              | **Description**                                    | **Example**                                 |
| -------------------------- | -------------------------------------------------- | ------------------------------------------- |
| `rating_widget.background` | Background color of the rating widget.             | `rating_widget.background = "#FFF"`      |
| `rating_widget.border`     | Border styling for the widget.                     | `rating_widget.border = "1px solid #CCC"` |
| `rating_widget.font`       | Font styling for labels (if applicable).           | `rating_widget.font = { size = "14px", color = "#000" }` |
| `rating_widget.icon`       | Styling for rating icons (e.g., color, size).       | `rating_widget.icon = { color = "#FFD700", size = "20px" }` |
| `rating_widget.icon.hover` | Styling when a rating icon is hovered.             | `rating_widget.icon.hover = { color = "#FFA500" }` |
| `rating_widget.results`    | Styling for displaying aggregated results.          | `rating_widget.results = { type = "bar", color = "#00FF00" }` |
| `rating_widget.animations` | Animations for rating interactions.                | `rating_widget.animations = { hover = "scale-up", select = "pulse" }` |
| `rating_widget.sounds`     | Sounds for specific interactions (optional).       | `rating_widget.sounds = { hover = "hover.mp3", select = "select.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "rating_widget"
scale = 5
labels = [ "Poor", "Fair", "Good", "Very Good", "Excellent" ]
icons = [ "star", "star", "star", "star", "star" ]
dynamic_source = "@SQeeL://content_ratings.db"
target_widget = "asset_card_1"
intents = [ "on_rate", "on_clear" ]
```

---

### **Example GSS Implementation**

```toml
[rating_widget]
background = "#FFF"
border = "1px solid #CCC"

[rating_widget.font]
size = "14px"
color = "#000"

[rating_widget.icon]
color = "#FFD700"
size = "20px"

[rating_widget.icon.hover]
color = "#FFA500"

[rating_widget.results]
type = "bar"
color = "#00FF00"

[rating_widget.animations]
hover = "scale-up"
select = "pulse"

[rating_widget.sounds]
hover = "hover.mp3"
select = "select.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Data Loading**
   - Use co-chains like SQeeL to fetch and update aggregated ratings in real-time.

#### **Responsive Design**
   - Ensure the widget adapts to various screen sizes and orientations.

#### **Localization Support**
   - Support for localized labels and tooltips.

#### **Custom Control Systems**
   - Enable GSS designers to create unique rating designs based on the scale (e.g., sliders for high scales, icons for low scales).

---

### **Use Cases**
- **Content Feedback**: Collect user ratings for videos, articles, or assets.
- **Product Reviews**: Enable customers to rate products in e-commerce platforms.
- **Service Quality**: Gather feedback on user experiences or customer support interactions.

---

### **Conclusion**

The Rating Widget is a flexible and visually engaging tool for collecting user sentiment. With robust customization options and seamless integration into co-chains like Pages, it provides valuable insights for content optimization and user engagement.

---

### **Classification Widget**

**Classification Widget**: A widget responsible for classifying content and recommending suitable audiences. This widget is crucial in social systems where user interactions influence content suggestions. It allows developers to indicate the intended audience and provides a field for users to describe why a specific classification was chosen. If a content widget does not have a classification, it will default to "Adult Only" as a security measure.

---

### **Core Features**

1. **Audience Classification**:

   - Developers can specify the intended audience (e.g., "Everyone", "Teen", "Mature").
   - Categories can follow predefined standards such as ESRB or custom classifications.
   - Default classification for untagged content widgets is "Adult Only".

2. **User Feedback**:

   - Users can add a description explaining their classification choice.
   - Provides transparency and accountability for content labeling.

3. **Dynamic Updates**:

   - Integrates with co-chains like Pages to dynamically adjust recommendations based on audience interactions and classifications.

4. **Customizable Design**:

   - GSS designers can define the appearance of classification categories, icons, and descriptions.

5. **Interaction Options**:

   - Intents such as `on_select` and `on_submit` allow seamless integration into applications.

6. **Accessibility Features**:

   - Fully navigable via keyboard or screen readers.
   - High contrast mode for better visibility.

7. **Animation and Sounds**:

   - Entrance and exit animations for the widget.
   - Optional sounds for selection and submission events.

---

### **M3L Fields**

| **Field**           | **Description**                                 | **Example**                                           |
| ------------------- | ----------------------------------------------- | ----------------------------------------------------- |
| `type`              | Specifies the widget type.                      | `type = "classification_widget"`                      |
| `categories`        | Defines available classification categories.    | `categories = [ "Everyone", "Teen", "Mature" ]`       |
| `default`           | Sets the default classification category.       | `default = "Everyone"`                                |
| `description_field` | Enables users to add a reason for their choice. | `description_field = true`                            |
| `dynamic_source`    | Fetches classification data dynamically.        | `dynamic_source = "@SQeeL://classification_rules.db"` |
| `intents`           | Specifies actions for widget events.            | `intents = [ "on_select", "on_submit" ]`              |

---

### **GSS Styling Parameters**

| **Parameter**                          | **Description**                                  | **Example**                                                                       |
| -------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------- |
| `classification_widget.background`     | Background color of the widget.                  | `classification_widget.background = "#FFF"`                                       |
| `classification_widget.border`         | Border styling for the widget.                   | `classification_widget.border = "1px solid #CCC"`                                 |
| `classification_widget.font`           | Font styling for categories and descriptions.    | `classification_widget.font = { size = "14px", color = "#000" }`                  |
| `classification_widget.category`       | Styling for individual categories.               | `classification_widget.category = { padding = "10px" }`                           |
| `classification_widget.category.hover` | Styling when a category is hovered.              | `classification_widget.category.hover = { background = "#EEE" }`                  |
| `classification_widget.description`    | Styling for the user feedback description field. | `classification_widget.description = { color = "#444" }`                          |
| `classification_widget.animations`     | Animations for widget interactions.              | `classification_widget.animations = { select = "fade-in", submit = "slide-out" }` |
| `classification_widget.sounds`         | Sounds for specific interactions (optional).     | `classification_widget.sounds = { select = "click.mp3", submit = "success.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "classification_widget"
categories = [ "Everyone", "Teen", "Mature" ]
default = "Everyone"
description_field = true
dynamic_source = "@SQeeL://classification_rules.db"
intents = [ "on_select", "on_submit" ]
```

---

### **Example GSS Implementation**

```toml
[classification_widget]
background = "#FFF"
border = "1px solid #CCC"

[classification_widget.font]
size = "14px"
color = "#000"

[classification_widget.category]
padding = "10px"

[classification_widget.category.hover]
background = "#EEE"

[classification_widget.description]
color = "#444"

[classification_widget.animations]
select = "fade-in"
submit = "slide-out"

[classification_widget.sounds]
select = "click.mp3"
submit = "success.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Data Loading**

- Use co-chains like SQeeL to dynamically fetch classification categories or adjust recommendations based on user interactions.

#### **Responsive Design**

- Ensure the widget adapts to various screen sizes and orientations.

#### **Localization Support**

- Support for localized category names and descriptions.

---

### **Use Cases**

- **Content Platforms**: Classify videos, articles, or posts to recommend appropriate audiences.
- **Social Applications**: Allow users to tag content with appropriate classifications for better visibility.
- **E-Learning**: Classify lessons or quizzes based on difficulty or age appropriateness.

---

### **Conclusion**

The Classification Widget is an essential tool for ensuring content is appropriately labeled and targeted to the right audience. With robust customization options and integration into social and content-driven systems, it promotes transparency and enhances the user experience.

---

### **Reaction Widget**

**Reaction Widget**: A widget that enables users to react to another widget using emojis, GIFs, or other visual elements. This widget is ideal for fostering engagement and interaction, commonly used in chats, videos, or content feeds.

---

### **Core Features**

1. **Reaction Options**:
   - Supports emojis, GIFs, or custom reaction icons.
   - Developers can define a set of pre-approved reactions.

2. **Dynamic Reaction Tracking**:
   - Tracks reaction counts in real-time when connected to co-chains like Pages.
   - Displays aggregated results (e.g., number of likes, favorite reactions).

3. **Customizable Design**:
   - GSS designers can style reaction icons, animations, and placement.
   - Allows for unique reaction designs per application or widget.

4. **Interaction Options**:
   - Intents such as `on_react`, `on_remove_reaction`, and `on_view_reactions` enable advanced interactions.
   - Multi-select support to allow users to choose multiple reactions, if enabled.

5. **Accessibility Features**:
   - Fully navigable via keyboard or screen readers.
   - High contrast mode for better visibility.

6. **Animation and Sounds**:
   - Entrance and exit animations for reaction icons.
   - Optional sounds for adding or removing reactions.

---

### **M3L Fields**

| **Field**          | **Description**                                   | **Example**                                                |
| ------------------ | ------------------------------------------------- | ---------------------------------------------------------- |
| `type`             | Specifies the widget type.                        | `type = "reaction_widget"`                                |
| `reaction_set`     | Defines the available reactions.                  | `reaction_set = [ "👍", "❤️", "😂", "😮", "😢", "👏" ]`    |
| `allow_gifs`       | Enables GIF reactions.                            | `allow_gifs = true`                                       |
| `dynamic_source`   | Fetches reaction data dynamically.                | `dynamic_source = "@SQeeL://reaction_data.db"`           |
| `intents`          | Specifies actions for widget events.              | `intents = [ "on_react", "on_remove_reaction" ]`         |
| `target_widget`    | Specifies the widget being reacted to.            | `target_widget = "chat_message_1"`                       |

---

### **GSS Styling Parameters**

| **Parameter**                | **Description**                                    | **Example**                                   |
| ---------------------------- | -------------------------------------------------- | --------------------------------------------- |
| `reaction_widget.background` | Background color of the reaction widget.           | `reaction_widget.background = "#FFF"`       |
| `reaction_widget.border`     | Border styling for the widget.                     | `reaction_widget.border = "none"`           |
| `reaction_widget.icon`       | Styling for reaction icons.                        | `reaction_widget.icon = { size = "24px" }` |
| `reaction_widget.icon.hover` | Styling when a reaction icon is hovered.           | `reaction_widget.icon.hover = { scale = "1.2" }` |
| `reaction_widget.results`    | Styling for aggregated reaction results.           | `reaction_widget.results = { color = "#FF00FF" }` |
| `reaction_widget.animations` | Animations for reactions (e.g., adding/removing).  | `reaction_widget.animations = { add = "bounce", remove = "fade-out" }` |
| `reaction_widget.sounds`     | Sounds for reaction interactions (optional).       | `reaction_widget.sounds = { add = "pop.mp3", remove = "delete.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "reaction_widget"
reaction_set = [ "👍", "❤️", "😂", "😮", "😢", "👏" ]
allow_gifs = true
dynamic_source = "@SQeeL://reaction_data.db"
target_widget = "chat_message_1"
intents = [ "on_react", "on_remove_reaction" ]
```

---

### **Example GSS Implementation**

```toml
[reaction_widget]
background = "#FFF"
border = "none"

[reaction_widget.icon]
size = "24px"

[reaction_widget.icon.hover]
scale = "1.2"

[reaction_widget.results]
color = "#FF00FF"

[reaction_widget.animations]
add = "bounce"
remove = "fade-out"

[reaction_widget.sounds]
add = "pop.mp3"
remove = "delete.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Data Loading**
   - Use co-chains like SQeeL to dynamically fetch and update reaction data.

#### **Responsive Design**
   - Ensure the widget adapts to various screen sizes and orientations.

#### **Localization Support**
   - Support for localized reaction sets (e.g., regional emoji preferences).

---

### **Use Cases**
- **Chats**: Allow users to react to individual messages with emojis or GIFs.
- **Videos**: Provide reaction tools for users to express sentiment during playback.
- **Content Feeds**: Enable reactions for posts, articles, or comments.

---

### **Conclusion**

The Reaction Widget fosters engagement and interactivity, providing users with an intuitive way to express sentiment. With dynamic customization options and seamless integration with other widgets, it’s a versatile tool for modern applications.

---

### **Status Bar Widget**

**Status Bar**: A widget designed to display relevant statistics or information at the bottom of the screen. This widget is ideal for creative or complex applications, providing feedback on processing times, system status, or the current mode within an application.

---

### **Core Features**

1. **Dynamic Status Updates**:
   - Displays real-time feedback for long-running processes (e.g., "Rendering: 75% complete").
   - Updates dynamically based on application state.

2. **Mode Display**:
   - Indicates the current mode of the application (e.g., "Edit Mode", "Preview Mode").
   - Allows seamless mode transitions with clear feedback to the user.

3. **Customizable Content**:
   - Supports text, icons, and progress bars for enhanced communication.
   - GSS designers can style the status bar to match the application’s theme.

4. **Interaction Options**:
   - Intents such as `on_click` or `on_hover` can trigger additional actions or tooltips.
   - Supports expandable sections for more detailed information.

5. **Accessibility Features**:
   - Fully navigable via keyboard or screen readers.
   - High contrast mode for better visibility.

6. **Animation and Sounds**:
   - Entrance and exit animations for smooth appearance or dismissal.
   - Optional sounds for status updates or warnings.

---

### **M3L Fields**

| **Field**        | **Description**                                   | **Example**                                                |
| ---------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `type`           | Specifies the widget type.                        | `type = "status_bar"`                                     |
| `default_mode`   | Sets the initial mode displayed.                  | `default_mode = "Edit Mode"`                              |
| `dynamic_source` | Fetches status updates dynamically.               | `dynamic_source = "@SQeeL://status_data.db"`             |
| `progress_bar`   | Enables or disables a progress bar.               | `progress_bar = true`                                     |
| `intents`        | Specifies actions for widget events.              | `intents = [ "on_click", "on_hover" ]`                   |

---

### **GSS Styling Parameters**

| **Parameter**                  | **Description**                                    | **Example**                                  |
| ------------------------------ | -------------------------------------------------- | -------------------------------------------- |
| `status_bar.background`        | Background color of the status bar.                | `status_bar.background = "#333"`           |
| `status_bar.border`            | Border styling for the widget.                     | `status_bar.border = "1px solid #FFF"`     |
| `status_bar.font`              | Font styling for status text.                      | `status_bar.font = { size = "12px", color = "#FFF" }` |
| `status_bar.progress`          | Styling for the progress bar (if enabled).         | `status_bar.progress = { color = "#0F0", height = "5px" }` |
| `status_bar.icon`              | Styling for icons displayed in the status bar.     | `status_bar.icon = { size = "16px", color = "#FFF" }` |
| `status_bar.animations`        | Animations for status updates or transitions.      | `status_bar.animations = { update = "fade-in", exit = "slide-out" }` |
| `status_bar.sounds`            | Sounds for status changes or updates.              | `status_bar.sounds = { update = "ping.mp3" }`          |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "status_bar"
default_mode = "Edit Mode"
dynamic_source = "@SQeeL://status_data.db"
progress_bar = true
intents = [ "on_click", "on_hover" ]
```

---

### **Example GSS Implementation**

```toml
[status_bar]
background = "#333"
border = "1px solid #FFF"

[status_bar.font]
size = "12px"
color = "#FFF"

[status_bar.progress]
color = "#0F0"
height = "5px"

[status_bar.icon]
size = "16px"
color = "#FFF"

[status_bar.animations]
update = "fade-in"
exit = "slide-out"

[status_bar.sounds]
update = "ping.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Data Loading**
   - Use co-chains like SQeeL to dynamically fetch and update status information in real-time.

#### **Responsive Design**
   - Ensure the widget adapts to various screen sizes and orientations.

#### **Localization Support**
   - Support for localized mode names and status descriptions.

---

### **Use Cases**
- **Creative Applications**: Display rendering progress or current tool mode.
- **System Monitoring**: Provide real-time system feedback, such as resource usage or network status.
- **Game Development**: Show game states or debug information during development.

---

### **Conclusion**

The Status Bar Widget is a vital tool for providing users with real-time feedback and context. Its flexible design and dynamic capabilities make it suitable for a wide range of applications, from creative tools to system monitoring.

---

### **Split View Widget**

**Split View**: A widget designed to divide the screen into two or more resizable panels, enabling flexible layouts and adjustable content areas. While initially intended for M3L and GSS editor applications, this widget has broad use cases for applications requiring multiple adjustable sections.

---

### **Core Features**

1. **Adjustable Panels**:
   - Allows users to resize panels dynamically.
   - GSS designers can define the minimum and maximum size for each panel.

2. **Dynamic Splits**:
   - Supports up to 2 splits on mobile devices and up to 4 splits on desktop.
   - Automatically adapts to screen size and orientation.

3. **Customizable Splitters**:
   - GSS designers can style the splitters, adding colors, gradients, or even images.
   - Splitter interaction (dragging) can trigger animations or sounds.

4. **Interaction Options**:
   - Intents such as `on_resize`, `on_drag_start`, and `on_drag_end` enable integration with application logic.
   - Supports snapping to predefined positions.

5. **Accessibility Features**:
   - Fully navigable via keyboard and screen readers.
   - High contrast mode for better visibility.

6. **Animation and Sounds**:
   - Animations for splitter resizing or snapping.
   - Optional sounds for drag interactions.

---

### **M3L Fields**

| **Field**         | **Description**                                   | **Example**                                                |
| ----------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `type`            | Specifies the widget type.                        | `type = "split_view"`                                     |
| `panels`          | Defines the number of panels.                     | `panels = 2`                                              |
| `min_panel_size`  | Sets the minimum size for each panel.             | `min_panel_size = "100px"`                                |
| `max_panel_size`  | Sets the maximum size for each panel.             | `max_panel_size = "auto"`                                 |
| `default_sizes`   | Specifies the initial sizes of the panels.         | `default_sizes = [ "50%", "50%" ]`                       |
| `intents`         | Specifies actions for widget events.              | `intents = [ "on_resize", "on_drag_start", "on_drag_end" ]` |

---

### **GSS Styling Parameters**

| **Parameter**               | **Description**                                    | **Example**                                   |
| --------------------------- | -------------------------------------------------- | --------------------------------------------- |
| `split_view.background`     | Background color for the entire widget.            | `split_view.background = "#F0F0F0"`         |
| `split_view.border`         | Border styling for the widget.                     | `split_view.border = "1px solid #CCC"`      |
| `split_view.splitter`       | Styling for the splitters (e.g., color, width).    | `split_view.splitter = { color = "#666", width = "5px" }` |
| `split_view.splitter.hover` | Styling for the splitter when hovered.             | `split_view.splitter.hover = { color = "#999" }` |
| `split_view.animations`     | Animations for resizing or snapping interactions.  | `split_view.animations = { resize = "ease-in-out", snap = "bounce" }` |
| `split_view.sounds`         | Sounds for dragging or snapping splitters.         | `split_view.sounds = { drag = "drag.mp3", snap = "snap.mp3" }` |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "split_view"
panels = 2
min_panel_size = "100px"
max_panel_size = "auto"
default_sizes = [ "50%", "50%" ]
intents = [ "on_resize", "on_drag_start", "on_drag_end" ]
```

---

### **Example GSS Implementation**

```toml
[split_view]
background = "#F0F0F0"
border = "1px solid #CCC"

[split_view.splitter]
color = "#666"
width = "5px"

[split_view.splitter.hover]
color = "#999"

[split_view.animations]
resize = "ease-in-out"
snap = "bounce"

[split_view.sounds]
drag = "drag.mp3"
snap = "snap.mp3"
```

---

### **Advanced Considerations**

#### **Dynamic Panel Adaptation**
   - Ensure panels resize dynamically when the screen size changes.

#### **Responsive Design**
   - Enforce screen size-based limits for splits (e.g., 2 for mobile, 4 for desktop).

#### **Customization and Theming**
   - GSS designers can create unique splitter styles and animations to match the application theme.

---

### **Use Cases**
- **M3L/GSS Editors**: Enable designers to preview how UIs respond to different layouts.
- **Development Tools**: Provide adjustable work areas for code, preview, and debugging.
- **Creative Applications**: Allow users to customize their workspace with adjustable panels.

---

### **Conclusion**

The Split View Widget is a versatile tool for creating resizable, multi-panel layouts. Its adaptability and customization options make it ideal for applications requiring dynamic and responsive designs, from creative tools to advanced editors.

---

### **Docking Widget**

**Docking Widget**: Allows UI elements to be draggable and dockable to predefined locations, spanning multiple screens, devices, and output types. This widget creates a **modular UI experience**, allowing users to customize their layout dynamically. With multi-output support, widgets can dock not only on screens but also on **haptic devices, audio systems, and smart environmental outputs**.

---

### **Core Features**

1. **Multi-Device Support**:
   - Dock widgets across **multiple displays**, including desktops, tablets, and mobile.
   - Allows seamless **cross-device** transitions (e.g., dock a chat window to a phone while keeping a dashboard on a monitor).

2. **Output-Responsive UI**:
   - Supports **audio-based docking** (e.g., notifications play through smart speakers or bone-conduction headsets).
   - Enables **haptic-based docking** (e.g., vibrations for alerts, controller trigger resistance for certain interactions).
   - Can link to **environmental devices** (e.g., smart lighting changes color based on notifications).

3. **Customizable Docking Zones**:
   - UI elements can be docked to **predefined areas** (top, left, right, bottom, floating, or user-defined positions).
   - Supports **auto-snap docking** for structured layouts or **freeform placement** for full user customization.

4. **GSS Styling and Behavior Customization**:
   - Define docking rules per **device type** and **screen resolution**.
   - Style docked UI elements with **border highlights, animations, and transparency effects**.

5. **Adaptive UI for Multiple Input Types**:
   - Seamless switching between **keyboard/mouse, controller, and touch**.
   - Allows GSS designers to **prioritize UI placement based on user preference and device interactions**.

6. **Drag-and-Drop Interaction**:
   - Widgets can be **freely moved, locked, or resized**, but only certain widget types support docking. For example, windows, toolbars, and media players can be docked, while elements like dropdown menus or context menus remain static.
   - Supports **gesture-based docking** for touch devices.

7. **AI-Assisted UI Adaptation (Optional Future Feature)**:
   - The system **learns user behavior** and suggests optimal widget docking positions.
   - Adaptive UI reorganization based on **frequent interactions**.

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "docking"
allowed_positions = ["top", "bottom", "left", "right", "floating"]
output_support = ["screen", "haptic", "audio", "environment"]

[[layout.container.content.default_widgets]]
id = "notifications"
dock_position = "top-right"
output_device = "screen"

[[layout.container.content.default_widgets]]
id = "alerts"
dock_position = "haptic"
output_device = "controller_trigger"
intensity = "medium"

[[layout.container.content.default_widgets]]
id = "music_player"
dock_position = "audio"
output_device = "bone_conduction"

[[layout.container.content.default_widgets]]
id = "workspace_lighting"
dock_position = "environment"
output_device = "smart_lighting"
color_theme = "cool blue"
```

---

### **Example GSS Implementation**

```toml
[docking]
background = "#1A1A1A"
border = "2px solid #444"

[docking.widget]
hover_effect = "glow"
active_border_color = "#00FFAA"
animation = "fade-in"

[docking.haptic_feedback]
trigger_resistance = "high"
intensity = "medium"

[docking.audio_feedback]
type = "subtle"
output = "3D_spatial_sound"

[docking.environmental_effects]
smart_lighting = "color_sync"
```

---

### **Use Cases**

- **Multi-Screen Workspaces**: Dock widgets between desktop monitors, tablets, and mobile for seamless productivity.
- **Immersive Gaming & Haptics**: Assign UI interactions to **controller vibrations or adaptive triggers**.
- **Audio & Sound Design**: Redirect notifications and alerts to **bone-conduction headsets or smart speakers**.
- **Smart Home Integration**: Sync notifications to **ambient lighting for passive alerts**.

---

### **Conclusion**

The Docking Widget redefines **UI flexibility**, allowing **dynamic, multi-device experiences**. Whether users **dock widgets across displays, haptic devices, or smart environments**, this widget provides a **seamless adaptive UI framework**. **With AI-assisted adaptation, future UI layouts will adjust to users' habits—automatically.**

---

### **Context Menu Widget**

**Context Menu**: A flexible menu system that appears upon interaction (right-click, long press, etc.) and offers quick access to relevant actions. Unlike static dropdowns, context menus in M3L can be **fully customized**, styled, and dynamically adapted based on user input and device type.

---

### **Core Features**

- **Dynamic Layout** – GSS designers can style it as a **dropdown, radial, cascading list, or linear menu**.  
- **Adaptive Visibility** – **GSS controls whether the menu disappears when the cursor moves away**.  
- **Base Functions** – Standard **UI functions** (e.g., **Cut, Copy, Paste, Pin to Desktop**) are always available.  
- **Custom Actions** – **M3L devs** can **inject their own custom functions** into the menu dynamically.  
- **Priority Items** – GSS **can set which items always appear first**, keeping layouts **clean and predictable**.  
- **Nested Menus** – Allows for **multi-tiered context menus** when needed.  
- **Positioning and Styling** – GSS **determines how and where the menu appears**.  
- **Item Limit** – Capped at **12 items per menu** to prevent UI overload.  
- **Shape Morphing** – GSS **can dynamically change the shape and structure of the menu**.  
- **SVG Icons Support** – Icons can replace text for **visual representation**, particularly useful for radial menus.  

---

### **Context Menu Behavior**

**How Do Default Items Work?**  
- **Each widget type has pre-defined default context options** (e.g., **Text Widgets** have Cut/Copy/Paste, **Asset View** has “Add to Cart” or “Compare”).  
- **M3L devs can override or extend this list**, but they cannot remove default OS-like functions.  

**Should Context Menus Persist?**  
- **Yes, if the GSS designer allows it.**  
- Some context menus may disappear on **mouse exit**, while others may remain until dismissed.  

**Can Menus Change Shape?**  
- **Yes.** The menu **can animate from a small dot into a full list, curve around an element, or dynamically reflow based on available space.**  

---

### **Example Context Menu in M3L**

```toml
[[layout.container.content]]
type = "context_menu"
allowed_layouts = ["dropdown", "radial", "list"]
auto_hide = false

[[layout.container.content.default_options]]
id = "copy"
label = "Copy"
intent = "copy"
icon = "@assets/icons/copy.svg"

[[layout.container.content.default_options]]
id = "paste"
label = "Paste"
intent = "paste"
icon = "@assets/icons/paste.svg"

[[layout.container.content.custom_options]]
id = "custom_action"
label = "Mark as Important"
intent = "custom"
icon = "@assets/icons/important.svg"
```

---

### **Example GSS Implementation**

```toml
[context_menu]
background = "#222"
border = "1px solid #555"
animation = "fade-in"

[context_menu.item]
hover_effect = "glow"
active_border_color = "#00FFAA"
icon_size = "20px"

[context_menu.layout.radial]
radius = "120px"
spread_angle = "180deg"

[context_menu.auto_hide]
enabled = true
timeout = "2s"
```

---

### **Use Cases**

- **Advanced UI Interactions**: Replace static menus with dynamic, interactive popups.  
- **Controller-Friendly UIs**: Perfect for **analog stick radial selections**.  
- **Fast Navigation in Productivity Apps**: Right-click or hold-press to quickly access relevant actions.  
- **Immersive Web3 Environments**: Context menus for **managing digital assets, interacting with on-chain tools, and performing quick operations**.  

---

### **Conclusion**

The **Context Menu Widget** transforms traditional menus into an **adaptive, fully customizable system**. Whether it's a **radial menu for controllers**, a **cascading list for file management**, or a **dynamic popup with AI-driven suggestions**, this widget brings **next-generation UI interactions** to UndChain.

---

### **Form Builder Widget**

**Form Builder**: A structured data entry system that supports dynamic validation, multi-step forms, and pre-filled inputs. This widget enables **structured data collection** while providing full flexibility for both M3L and GSS developers.

---

### **Core Features**

- **Dynamic Field Creation** – M3L developers define **text fields, checkboxes, dropdowns, radio buttons, and file uploads**.
- **Validation System** – Allows **real-time input validation** (e.g., required fields, regex validation, format checks).
- **Multi-Step Forms** – Supports **step-based navigation** for complex data entry.
- **Pre-Fill Support** – Users can opt-in to **auto-fill common fields** (e.g., name, email, phone) from their UndChain profile.
- **Custom Error Handling** – Errors are styled and handled by **GSS** (e.g., tooltips, popups, field highlights).
- **Auto-Saving & Drafts** – **Partially completed forms are saved on UndChain** but remain under the control of the **form writer**.
- **Submit Action** – Every form **must** have a submit button, which **triggers an intent for processing the data**.
- **Conditional Logic** – Fields can **show/hide based on previous answers** (e.g., If "Other" is selected, a new text field appears).
- **Controller & Keyboard Navigation** – Supports **tabbing between fields and controller-based inputs**.
- **Alternative Input Support** – Users can enter data **via voice input, handwriting, or standard text entry**, depending on GSS implementation.

---

### **File Submission Rules**

- **Files are uploaded to UndChain** and **linked in the form submission** (not physically attached).
- **File Size & Type Rules** – M3L developers can set acceptable file types and size limits.
- **Limits Per Form** – Form creators can set a **maximum number of attachments** per submission.
- **Off-Chain Attachments** – If a file is stored off-chain, the **user must explicitly approve the link before submission**.

---

### **CAPTCHA Alternative for Free Submissions**

- A **built-in challenge system** for spam prevention.
- **Only required when the user isn't paying for form submission.**
- Uses **UndChain perception scores and account activity** to determine if the user is a real person.
- Can be **enabled per form** by M3L developers.

---

### **Example Form Builder in M3L**

```toml
[[layout.container.content]]
type = "form_builder"
steps = 3  # Defines multi-step navigation

[[layout.container.content.fields]]
id = "full_name"
type = "text"
label = "Full Name"
required = true
pre_fill = true  # Pulls from user profile if permitted

[[layout.container.content.fields]]
id = "email"
type = "email"
label = "Email Address"
required = true
pre_fill = true

[[layout.container.content.fields]]
id = "file_upload"
type = "file"
label = "Upload Documents"
max_files = 3
file_types = ["pdf", "jpg", "png"]
max_size = "10MB"

[[layout.container.content.fields]]
id = "captcha"
type = "captcha"
label = "Verification"
required = true
```

---

### **Example GSS Implementation**

```toml
[form_builder]
background = "#FFF"
border = "1px solid #CCC"
padding = "15px"

[form_builder.field]
label_font_size = "14px"
error_color = "#FF0000"

[form_builder.button.submit]
background = "#007BFF"
color = "#FFF"
padding = "10px"
border-radius = "5px"
hover.background = "#0056b3"

[form_builder.captcha]
challenge_type = "image_recognition"
```

---

### **Use Cases**

- **E-commerce Checkout Forms** – Users can pre-fill shipping details for faster checkout.
- **Job Applications** – Supports multi-step entry and file uploads.
- **Event Registration** – Allows conditional fields based on user input.
- **On-Chain ID Verification** – Uses file upload validation for identity checks.

---

### **Conclusion**

The **Form Builder Widget** enables developers to **build complex, interactive forms** with full **validation, multi-step workflows, and adaptive pre-filling.** By integrating **alternative inputs, UndChain storage, and CAPTCHA-like security based on perception scores and activity tracking**, this widget **ensures smooth user experiences while preventing spam and abuse.**

---

### **Node Grid Widget**

**Node Grid**: A foundational widget for **flowcharts, visual scripting, neural network mapping, automation tools, and creative workflows**. This system allows **interactive, structured relationships** between various elements, creating a **flexible and powerful visualization environment**.

---

### **Core Features**

- **Grid-Based Layout** – Nodes snap to a defined grid system for cleaner layouts.
- **Widget-Agnostic Snapping** – Any widget can be snapped inside a node grid (e.g., shapes, text, images).
- **Connection System** – Nodes can be **linked via directional or bi-directional arrows** for structured relationships.
- **Multi-Input & Output Support** – A single node can have **multiple connection points** for complex structures.
- **Shape Integration** – Nodes can take the form of **rectangles, circles, diamonds**, or custom-defined SVG shapes.
- **Layering Support** – Supports **z-order management** so some nodes **can be layered on top of others**.
- **Dynamic Rearrangement** – Auto-layout options can **reposition nodes dynamically** based on relationships.
- **Dragging & Panning** – Users can freely **drag nodes** and **pan across the workspace**.
- **Custom Labels & Metadata** – Each node **can contain descriptions, icons, tags, and metadata**.
- **Animated Flow** – **Optional animations** when nodes **connect or disconnect** to improve visualization.
- **Group Nodes & Nesting** – Allows **collapsible groups** of nodes for **sub-flowcharting**.
- **Configurable Snapping** – The snapping grid is **controlled by the GSS designer** and adapts to **screen size and zoom level**.
- **Curved & Straight Connections** – **GSS designers** can configure connections to be **rigid or curved**.
- **Expandable Nodes** – **Nodes that contain additional data can expand/collapse**, with visual indicators for expansion.
- **Default Logic Nodes** – Includes **AND, OR, NOT** logic nodes for **decision trees and automation workflows**.
- **Configurable Arrows** – Connections can be **directional or bi-directional**, set by the M3L developer.

---

### **Example Node Grid in M3L**

```toml
[[layout.container.content]]
type = "node_grid"
snap_enabled = true

[[layout.container.content.nodes]]
id = "start_node"
type = "shape"
label = "Start"
shape = "circle"
color = "#007BFF"

[[layout.container.content.nodes]]
id = "decision_node"
type = "logic"
label = "Decision"
shape = "diamond"
logic_type = "AND"
expandable = true

[[layout.container.content.connections]]
from = "start_node"
to = "decision_node"
connection_style = "curved"
direction = "bi-directional"
```

---

### **Example GSS Implementation**

```toml
[node_grid]
grid_color = "#CCC"
snap_to_grid = true
zoom_enabled = true

[node_grid.node]
default_background = "#222"
default_border = "1px solid #555"
animation_on_connect = "fade-in"

[node_grid.connection]
default_style = "curved"
default_color = "#00FFAA"
arrow_type = "bi-directional"
```

---

### **Use Cases**

- **Flowchart Systems** – For business logic, automation workflows, and procedural mapping.
- **Visual Programming** – Enables block-based programming similar to Unreal Engine’s Blueprint system.
- **Neural Networks & AI Mapping** – Helps visualize decision trees and data flow models.
- **CAD-like Design Tools** – Can be expanded for **schematic representation and diagramming**.

---

### **Conclusion**

The **Node Grid Widget** enables **interactive, structured relationships** between various elements, providing a **powerful visualization framework** for automation, logic mapping, and interactive flowcharts. **By integrating SVG-based shapes, animated transitions, and customizable snapping, this widget offers a highly adaptable and dynamic experience.**

---

### **Shapes Widget**

**Shapes**: A versatile widget for **drawing, scaling, and manipulating geometric forms**. This system is designed for use in **flowcharts, CAD-like applications, whiteboards, and node-based interfaces.**

---

### **Core Features**

- **Predefined Shape Types** – Supports **rectangles, circles, triangles, diamonds, stars, hexagons**, and **custom SVG imports**.
- **Scalability** – Shapes can be **resized dynamically**, maintaining aspect ratios where needed.
- **Rotational Support** – Users can **rotate shapes** freely or snap to defined angles.
- **Text Annotations** – Shapes can contain **embedded text** with customizable font, size, and color.
- **Layering & Ordering** – Supports **z-order management** to control depth positioning.
- **Snap-to-Grid & Freeform Placement** – Shapes can be **manually placed** or **snapped to an alignment grid**.
- **Fill & Stroke Options** – Supports **solid, gradient, pattern fills, and custom stroke styles** (dashed, dotted, etc.).
- **Grouping & Ungrouping** – Multiple shapes **can be grouped together for batch manipulation**.
- **Opacity & Transparency Controls** – Allows **semi-transparent overlays** for layering effects.
- **Shape Animations** – Shapes can have **entrance, exit, and interaction animations** defined in GSS.
- **Dynamic Reshaping** – Some shapes (e.g., polygons) can **have adjustable points** to modify their structure.
- **Multi-Selection Support** – Users can select multiple shapes via **drag-select or object panel selection**.
- **Image Fill Support** – Shapes can contain **images as a fill**, with resolution options controlled by **M3L/GSS developers**.
- **Shape Merging & Boolean Operations** – Supports **union, subtraction, combination, and fragmentation** for complex shape manipulation.
- **Shape Sticking (Grouping)** – Users can **stick shapes together**, allowing movement as a single unit while maintaining separate shape definitions.

---

### **Example Shapes in M3L**

```toml
[[layout.container.content]]
type = "shape"
id = "custom_shape"
shape = "circle"
color = "#FF0000"
stroke = "2px solid #000"
rotation = 45
group = "main_group"

[[layout.container.content]]
type = "shape"
id = "image_shape"
shape = "rectangle"
fill_type = "image"
image_src = "@Undline/assets/texture.jpg"
max_resolution = "1080p"

[[layout.container.content]]
type = "shape"
id = "merged_shape"
merge_operation = "union"
merge_targets = ["custom_shape", "image_shape"]
```

---

### **Example GSS Implementation**

```toml
[shape]
default_background = "#EEE"
default_border = "1px solid #444"
animation_on_hover = "pulse"

[shape.fill]
default_style = "gradient"
default_gradient = ["#FF0000", "#FFA500"]

[shape.image]
max_resolution = "4K"
auto_disable = true

[shape.merge]
default_operation = "combine"
allow_fragmentation = true
```

---

### **Use Cases**

- **Flowchart Systems** – Creating structured diagrams with labeled nodes.
- **Whiteboard Applications** – Enabling freehand design with reusable elements.
- **CAD-Like Tools** – Allowing precise geometric shape manipulation.
- **UI Design & Prototyping** – Assisting in interface layout planning.

---

### **Conclusion**

The **Shapes Widget** enables **rich geometric manipulation** with **snapping, scaling, merging, and animation support**. By integrating **image fills, multi-selection, and custom Boolean operations**, this widget provides **a highly dynamic and versatile drawing experience.**

---

### **Chat Widget**

**Chat Widget**: A versatile messaging system supporting **real-time messaging, reactions, user status indicators, advanced moderation tools, and configurable file-sharing and link permissions**.

---

### **Core Features**

- **Live & Historical Messages** – Supports both **real-time chats and replayable past conversations** (e.g., VOD replays).
- **Message Formatting** – Allows for **bold, italics, underlines, links, emojis, and markdown support**.
- **Reactions & Reply System** – Users can react to messages (e.g., 👍, ❤️) and **reply in threads**.
- **User Status Indicators** – Shows **active, idle, offline, or custom status** (e.g., ‘Typing...’).
- **Typing Indicator Management** – **Typing indicators are automatically disabled when more than three users are actively chatting** to prevent overload.
- **Private & Group Chats** – Supports **one-on-one messaging and multi-user group chats**.
- **Message Pinning & Saving** – Allows users to **pin important messages** or **save them for later**.
- **Read Receipts & Delivery Status** – Displays **sent, delivered, and seen indicators**.
- **File Attachments** – Supports **sending images, videos, documents, and voice messages**, with host-configurable file-sharing permissions.
- **Moderation Controls** – Allows **admins/moderators to mute, ban, delete messages, and enforce chat modes**.
- **Chat Modes** – Hosts can **restrict chats to emoji-only, GIF-only, or slow mode** to manage high-volume conversations.
- **Link Sharing Permissions** – Hosts can **allow or block links** based on **user roles** (e.g., only moderators or VIP users can post links).
- **Theme & Layout Customization** – GSS can control **bubble shape, color schemes, and chat position**.
- **Timestamps & Message Ordering** – Messages are **timestamped** and sorted chronologically to **support VOD replays**.
- **AI-Powered Auto-Replies & Moderation** – Optionally integrates with **Mimic AI** to provide **suggested responses and automated moderation tools**.
- **Voice & Video Call Integration** – Supports linking to **external VoIP/video conferencing systems**.
- **Search & Filtering** – Users can **search for messages, filter by sender, or highlight keywords**.
- **Custom Emoji & Sticker Support** – Hosts can upload **custom emoji packs & stickers** (with optional subscription gating).
- **Self-Destructing Messages** – Users can opt to send **temporary messages** that disappear after a set duration.
- **Live Mode & Chat Replay** – **Live chat can be replayed** when watching recorded content (e.g., VOD playback).
- **Notification & Mute Settings** – Users can **mute chats, filter notifications, or adjust alert frequency** based on volume.
- **Bandwidth Optimization for Custom Emojis** – Limits emoji size & caching to prevent excessive data usage.

---

### **Example Chat Widget in M3L**

```toml
[[layout.container.content]]
type = "chat_widget"
mode = "live"
moderation_enabled = true
chat_mode = "emoji_only"
custom_emojis = true
allow_file_sharing = false
allow_link_sharing = "moderators_only"
typing_indicator_management = "auto_disable_on_high_volume"

[[layout.container.content.moderation]]
mimic_ai_assist = true
max_message_length = 500
allow_temp_messages = true
```

---

### **Example GSS Implementation**

```toml
[chat_widget]
bubble_background = "#222"
text_color = "#FFF"
typing_indicator = "pulse"
typing_indicator_auto_disable = 3

[chat_widget.emoji]
custom_emoji_support = true
emoji_cache_limit = "50MB"

[chat_widget.moderation]
default_mode = "slow"
mute_sound_on_high_volume = true

[chat_widget.permissions]
allow_file_sharing = false
allow_link_sharing = "moderators_only"
```

---

### **Use Cases**

- **Gaming & Live Streaming** – Supports real-time chat with **VOD replay functionality**.
- **Collaborative Workspaces** – Enables **private and group chats** for teams and communities.
- **Decentralized Social Platforms** – Offers a robust **messaging framework** for social engagement.
- **Educational Platforms** – Allows structured discussions with **emoji-based engagement and moderation tools**.

---

### **Conclusion**

The **Chat Widget** is a fully customizable, **real-time and replayable** chat system designed for **flexible integration in applications**. With support for **moderation tools, AI-assisted filtering, configurable file-sharing and link permissions, and multi-format messaging**, this widget enables both **casual and professional communication** while ensuring **efficient resource management and smooth user experience.**

---

### **Hero Section Widget**

**Hero Section**: Captures user attention with headers, sub-headers, and call-to-action buttons. Different types of hero sections allow for **dynamic content presentation, immersive storytelling, and action-driven user engagement**.

---

### **Hero Section Types**

- **Standard Hero** – The classic hero section with a **headline, subtext, and CTA button**.
- **Scrolling Banner Hero** – Functions as a **carousel or auto-scrolling banner**, featuring **multiple offers, images, or messages**.
- **Product Showcase Hero** – A **large display hero** featuring a **product or service**, possibly with **ratings, price, and add-to-cart functionality**.
- **CTA Hero** – Designed for **strong action-taking**, like signing up for a newsletter, **registering for an event**, or making a **purchase immediately**.
- **Interactive Hero** – Embeds **user input fields, search bars, countdown timers, or live updates** for a more dynamic experience.
- **Full-Screen Takeover Hero** – Expands the **entire viewport**, ideal for **immersive storytelling, launch pages, or cinematic experiences**.

---

### **Core Features**

- **Headline & Sub-Header** – The primary and supporting **text for user engagement**.
- **Call-to-Action (CTA) Buttons** – Supports **multiple action buttons** to guide users toward a goal.
- **Background Media** – Can use **static images, gradients, patterns, video, or animations** as a backdrop.
- **Overlay & Text Contrast Options** – Ensures readability with **darkened overlays or text shadowing**.
- **Alignment & Layout Control** – Supports **centered, left-aligned, or right-aligned text and buttons**.
- **Responsive Scaling** – Adapts to **mobile, tablet, and desktop layouts dynamically**.
- **Interactive Elements** – Allows **hover effects, animations, and scroll-triggered transformations**.
- **Customization for CTA Buttons** – Can be **rectangular, rounded, or floating** per GSS styling.
- **Auto-Scroll Prompts** – Can integrate **downward scroll indicators** to guide users further down the page.
- **Customizable Animations** – Can **fade in, slide in, zoom, or pulse upon page load**.
- **Parallax Support** – Background image/video can **scroll slower than foreground text for depth effects**.
- **Live Updates** – Can dynamically **update content without reloading the page**, useful for promotions or announcements.

---

### **Example: Full-Screen Hero for Product Launch**

```toml
[[layout.container.content]]
type = "hero_section"
hero_type = "full_screen"
background_type = "video"
background_src = "@UndChain/assets/console_promo.mp4"
animation_entry = "fade_in"
animation_exit = "fade_out"
dismiss_mode = "scroll, timer"
timer_duration = 5  # Auto-dismiss after 5 seconds

[[layout.container.content.text]]
type = "headline"
text = "The Future of Gaming is Here."
font_size = "4rem"
color = "#FFF"

[[layout.container.content.text]]
type = "subheader"
text = "Introducing the UndChain Console – Power. Speed. Innovation."
font_size = "2rem"
color = "#CCC"

[[layout.container.content.button]]
label = "Pre-Order Now"
action = "@UndChain.Store/preorder"
button_style = "primary"
```

---

### **Example GSS Styling**

```toml
[hero_section.full_screen]
background_color = "#000"
text_alignment = "center"
padding = "40px"
transition_speed = "1s"

[hero_section.full_screen.animation]
entry = "zoom_in"
exit = "fade_out"
```

---

### **Use Cases**

- **Gaming & Live Streaming** – Supports dramatic product launches with full-screen takeovers.
- **E-Commerce & Promotions** – Highlights key promotions with scrolling banner heroes.
- **Decentralized Social Platforms** – Creates engaging community entry points.
- **Educational Platforms** – Introduces new courses dynamically with interactive heroes.

---

### **Conclusion**

The **Hero Section Widget** provides **multiple configurations for eye-catching designs, engagement-driven CTAs, and immersive user experiences**. Its **versatile structure allows for seamless integration into any webpage**, whether for **advertising, content delivery, or user engagement.**

---

### **Settings Widget**

**Settings**: This widget contains settings for the current application that a user can control per the M3L developer and GSS designer. The settings menu includes default items but can also be expanded by both the M3L developer of the app where the settings widget is launched and the GSS designer currently in use.

---

### **Core Features**

- **Theme Customization** – Allows users to toggle dark/light mode, adjust color schemes, or switch between multiple UI themes if the GSS designer has provided them.
- **Text Scaling & Accessibility** – Adjusts default text size, font choices, contrast settings, and UI scaling for accessibility.
- **Device Management** – Enables users to add, remove, and assign content to connected devices in the multi-device ecosystem.
- **Notification & Sound Settings** – Allows users to mute specific notifications, enable sounds, or customize alert types (e.g., popups, toast messages, banners).
- **Permission Controls** – Grants users control over device access, storage permissions, media playback, and interaction preferences for individual applications.
- **Auto-Fill & Auto-Pay** – Supports custom rules for automatic form-filling and limits for auto-spending AdCoin or other digital assets on paywalled content.
- **Energy-Saving & Performance Modes** – Allows users to limit animations, reduce computational load, or optimize performance based on device capabilities.
- **Regional Settings** – Controls default language, currency, and time zone settings.
- **Security & Privacy Settings** – Includes options for biometric authentication, encryption settings, and data retention preferences.
- **Application-Specific Settings** – Developers can expose custom configuration options, like gameplay settings, workflow preferences, or toggling experimental features.

---

### **Advanced Features**

- **Animations Toggle** – Allows users to enable/disable animations entirely (useful for performance tuning or accessibility).
- **Per-Widget Animation Settings** – Users can choose which animations to disable or reduce intensity (e.g., subtle transitions vs. full animations).
- **Sound-Linked Animations** – Since sounds are triggered with animations, the animation toggle should also disable associated sounds unless the user specifies otherwise.
- **Intent Type for Accessing Settings** – Different devices may require different access methods:
  - Mouse & Keyboard → Click settings icon or press a shortcut (e.g., `Ctrl + ,`).
  - Controller → Press Pause/Menu Button or enter a Pause Menu.
  - Touchscreen → Tap a hamburger menu or swipe from the edge.
- **User Profile Management** –
  - View & manage public profile info.
  - Set custom avatars (stored in UndChain).
  - Switch between multiple user profiles.
  - View public key & account details.
- **Privacy & Visibility Controls** –
  - Toggle “Online” status visibility.
  - Decide whether read receipts are shared in chats.
  - Choose whether to display typing indicators.
  - Enable/disable activity tracking & logs (e.g., time online, spending behavior).
- **Connected Devices Panel** –
  - Lists all connected devices (PC, phone, controller, haptics, VR headset, etc.).
  - Displays device image, function, and current status (active, idle, disconnected).
  - Allows renaming devices for better management.
  - Configure input mappings (e.g., remap buttons for controllers).
  - Enable/disable specific device interactions (e.g., “disable motion controls”).
  - Allow/deny specific apps access to devices.
- **Security & Encryption Preferences** –
  - Encryption Type Display – Users can see what encryption method is currently in use.
  - Key Management – Shows the public key and allows users to generate a new key pair if needed.
  - Session Logs & Activity Tracking – Provides users visibility into login sessions & device access history.

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "settings"
theme_toggle = true
animation_toggle = true
font_scaling = true
device_management = true
auto_pay = { enabled = true, max_limit = 50 }
privacy_controls = { online_status = false, read_receipts = false, typing_indicator = true }

[[layout.container.content.profile]]
username = "@Undline"
avatar = "@Undline/avatar.png"
public_key = "0x123456789"
profile_switching = true

[[layout.container.content.devices]]
allow_remap = true
show_connected = true
device_list = [
    { name = "PS5 Controller", type = "gamepad", active = true },
    { name = "Meta VR Headset", type = "VR", active = false }
]

[[layout.container.content.security]]
encryption_type = "AES-256"
show_public_key = true
log_sessions = true
```

---

### **Example GSS Styling**

```toml
[settings]
background_color = "#222"
text_color = "#FFF"
toggle_style = "slider"
animation_entry = "fade_in"

[settings.privacy]
online_status_toggle = true
read_receipts_toggle = true
typing_indicator_toggle = true

[settings.devices]
list_display = "grid"
highlight_active = true
```

---

### **Use Cases**

- **Gaming & Streaming** – Users can fine-tune their experience based on performance and input preferences.
- **E-Commerce & Subscriptions** – Provides users control over automatic payments and purchase history.
- **Decentralized Workflows** – Manages connected devices, security, and custom workflows for dApps.

---

### **Conclusion**

The **Settings Widget** provides users with control over privacy, security, animations, input devices, notifications, and application preferences. Its extensive features make it a core part of any M3L-powered application, ensuring flexibility, security, and accessibility for all users.

---

### **Pause Menu Widget**

**Pause Menu**: Opens a pause menu widget that allows users to select from multiple options. Primarily designed for controller-based navigation but also accessible via keyboard (`Pause/Break` key) or touchscreen.

---

### **Core Features**

- **Resume Functionality** – Users can resume the session by pressing the `Pause` key again, selecting `Resume` from the menu, or pressing the designated controller button (e.g., `Start`).
- **Settings Menu** – Direct access to the **Settings Widget** for adjusting preferences mid-session.
- **Exit/Quit Option** – Allows the user to **exit the current app/session** (to desktop, main menu, or entirely out of the application). For controllers, this can be mapped to the `Exit` button, while the `Home` button returns users to the home screen, placing the application in a suspended state.
- **Save & Load (If Applicable)** – Provides options to **save progress and reload previous sessions** (useful for gaming or workflow-oriented applications).
- **Quick Select (Optional)** – A section where users can jump between **frequently accessed sections** (e.g., inventory, chat, user profiles).
- **Network Status Indicator** – Displays **connection status, ping, or blockchain sync state** for networked applications.
- **Controller Input Mapping** – Displays a **quick reference for control schemes**, especially useful when switching between different controllers.
- **Help & Support** – Access documentation, FAQs, or AI-powered assistance.
- **Return to Home Screen** – Option to suspend the current application and return to the UndChain desktop or main application hub.

---

### **Customization & Configuration**

- **Maximum of 8 Menu Items** – To prevent overwhelming users, the pause menu is limited to 8 selectable options.
- **Visual Transitions & Background Customization** –
  - Designers can **customize how the pause menu enters/exits** (e.g., fade-in, zoom, slide-in).
  - Instead of just blurring the background, designers can **swap in a completely different background** for more immersive effects.
  - The background can **change dynamically based on the currently selected option** (e.g., an animated guide highlighting different sections).
- **Live Pause vs. Freeze Mode** –
  - Applications can use **full freeze mode** (pauses updates, animations, and inputs) or **live pause mode** (keeps background data streams running).
  - Users can configure this in the **Settings Menu** based on their performance preferences.
- **Recent Messages Overlay** –
  - Users can view the last few messages received before pausing.
  - Useful in multiplayer applications or when using AI-assisted interactions.
- **Button Behavior Control** –
  - GSS designers can define how buttons behave (e.g., click-to-activate vs. hold-to-activate).
  - Users can also remap pause menu controls for their input device.

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "pause_menu"
pause_mode = "live"  # Options: "freeze", "live"
background = "custom_image"
options = [
    { label = "Settings", action = "open_settings" },
    { label = "Exit to Home", action = "return_home" },
    { label = "Exit Application", action = "exit_application" },
    { label = "Save Progress", action = "save_session" },
    { label = "Help", action = "open_help" }
]

[[layout.container.content.status]]
network_status = "show"
input_mapping = "show"
notifications = "hide"
```

---

### **Example GSS Styling**

```toml
[pause_menu]
background = "dark_overlay"
menu_style = "vertical_list"
animation_entry = "fade_in"
animation_exit = "fade_out"

[pause_menu.buttons]
hover_effect = "glow"
active_effect = "press_down"

[pause_menu.status]
network_display = "corner_top"
```

---

### **Use Cases**

- **Gaming & Streaming** – Allows users to manage sessions, settings, and network states while pausing.
- **Workflows & Productivity** – Enables quick saves, workflow switches, and connectivity checks in dApps.
- **Decentralized Applications** – Syncs across connected devices, providing multi-device pause handling.

---

### **Conclusion**

The **Pause Menu Widget** provides users with **seamless access to application settings, session management, and network details** without disrupting the experience. Its **customizable visual elements and flexible configurations** make it an essential tool for a wide variety of applications.

This includes:
- **Configurable freeze vs. live pause mode** (set by users in settings).
- **Dynamic UI customizations based on current selection.**
- **Customizable button behaviors, animations, and background swaps.**
- **Streamlined default menu with intuitive button mapping.**
- **Dedicated Exit and Home buttons for clear navigation.**

---

### **TOS Widget**

The **TOS Widget** is a standardized component designed for handling terms of service agreements, contracts, and user acknowledgments. It ensures users actively review agreements before proceeding with actions like using a co-chain, purchasing assets, or signing legally binding documents.

---

## **Core Features**

### **1. Structured Display**
- Presents **terms of service, contracts, or agreements** in an organized format.
- Supports **Markdown formatting** for the content sections, while section titles remain static.
- Displays structured sections with clear **titles** and **content blocks**.
- Can include **embedded media** (e.g., images, videos) for additional clarification.

### **2. Acceptance & Interaction**
- **Accept and Reject Buttons**: Users must actively confirm their decision.
- **Scroll Requirement**: Users must scroll through the entire document before acceptance.
- **Timer Enforcement**: Developers can set a mandatory review time before enabling the accept button.
- **Smart Scroll Detection**: Prevents rapid scrolling by limiting speed to ensure users read key sections.

### **3. Change Tracking & Summaries**
- **Version Control**: Users are notified when the TOS has been updated.
- **Change Highlights**: Marks and summarizes differences between the previous and current version.
- **Mandatory Re-Acceptance**: Users must accept the updated version before continuing (if required).

### **4. Customization & User Experience**
- **Multi-Language Support**: Users can switch to translated versions if available.
- **Theming**: Custom fonts, colors, and layouts defined by the GSS file.
- **Overlay or Fullscreen Mode**: Can be presented as a modal or full-page agreement.
- **Progress Indicator (GSS Implementation)**: Optional visual bar to track reading progress.
- **Dark Mode Compatibility**: Ensured via GSS customization.

### **5. Data Logging & Retrieval**
- **Timestamping**: Logs the time and date of acceptance.
- **Previous Agreements Access**: Users can review past accepted agreements.
- **Blockchain Validation (Optional)**: Co-chain validation records acceptance for transparency and non-repudiation.

---

## **M3L Implementation Example**
```toml
[[layout.container.content]]
type = "tos_widget"
id = "terms_of_service"
sections = [
    { title = "Introduction", content = "Welcome to our platform. By using our services, you agree to the following terms..." },
    { title = "Data Usage", content = "We collect minimal data necessary for platform functionality. See our privacy policy..." },
    { title = "User Responsibilities", content = "You are responsible for keeping your account secure and following the guidelines set forth..." }
]
accept_button = "I Agree"
reject_button = "Decline"
scroll_required = true
time_limit = 30  # Minimum 30 seconds before acceptance is enabled
```

---

## **GSS Implementation Example**
```toml
[tos_widget]
font-family = "Arial, sans-serif"
background-color = "#ffffff"
text-color = "#333333"
border-radius = "8px"

[tos_widget.buttons]
accept.background-color = "#007BFF"
accept.text-color = "#ffffff"
reject.background-color = "#FF3B30"
reject.text-color = "#ffffff"

[tos_widget.scroll_behavior]
disable_accept_until_read = true
scroll-speed-limit = "moderate"
progress-indicator = true

[tos_widget.animations]
on_open = "fade-in"
on_close = "fade-out"
```

---

## **Optional Enhancements**
- **AI Summary Assistance**: If enabled, AI (e.g., Mimic) generates a summarized version of the agreement.
- **Alternative Accept Methods**: Voice confirmation or biometric approval (if supported by the device).
- **Opt-In Features**: Users can check optional clauses within the same widget.
- **User-Specific Terms**: Custom agreements based on the user’s role or prior selections.

---

### **Final Thoughts**
The **TOS Widget** provides a standardized, transparent way to handle agreements, ensuring compliance while offering customization for developers and designers. With features like **change tracking, smart scrolling, markdown content support, and sectioned organization**, it balances legal clarity with user-friendly interactions.

---

### **Find/Replace Widget**

The **Find/Replace Widget** is an in-app **text search and replacement** system designed for applications that require **efficient, scoped, and interactive text navigation**. Unlike a full **application-wide search**, this widget operates within a defined **scope**, ensuring a streamlined and **context-aware** search experience.

---

## **Core Features**

### **1. Scoped Search & Matching (M3L)**

- **Scope Definition**:
  - **Widget-Specific**: Limited to selected widgets (`text_area`, `spreadsheet`, etc.).
  - **Document-Wide**: Searches across all text-based content within a specific M3L file.
- **Search Matching Options**:
  - **Case Sensitivity**: Optional (`true/false`).
  - **Whole Word Matching**: Ensures only full-word matches appear.
  - **Wildcard Support**:
    - `*` matches multiple characters (`doc*` → `document`, `docs`).
    - `?` matches a single character (`col?r` → `color`, `colour`).
  - **Fuzzy Search (Optional)**: AI-driven correction for misspelled search queries.

### **2. Replace Functionality**

- **Replace One**: Modifies only the currently selected match.
- **Replace All**: Applies replacements across all matched occurrences.
- **Undo & Redo Support**: Reverts or reapplies replacements.

### **3. Intuitive UI & Interaction (GSS Controlled)**

- **Search Panel**:
  - **Compact Mode**: Simple **search bar** with **hit count** and **navigation arrows**.
  - **Expanded Mode**: Includes **replace field**, **filters**, and **advanced options**.
- **Find Animation** (Contextual Highlighting):
  - **Scroll Views**: **Pans and highlights** found text using an **easing curve**.
  - **Multi-Page Documents**: **Slides to the correct page**, then highlights the match.
- **Voice Search Support**:
  - AI-assisted speech-to-text conversion.
  - **Optional microphone input trigger**.

---

## **M3L Implementation Example**

```toml
[[layout.container.content]]
type = "find_replace_widget"
id = "search_in_notes"
search_scope = ["text_area_1", "text_area_2"]
case_sensitive = false
whole_word = true
wildcard_enabled = true
ai_suggestions = true  # Users can disable this in settings
```

---

## **GSS Implementation Example**

```toml
[find_replace_widget]
font-family = "Arial, sans-serif"
background-color = "#f8f8f8"
text-color = "#333"
border-radius = "5px"
popup_position = "top"

[find_replace_widget.highlight]
background-color = "#ffeb3b"
border = "1px solid #ffcc00"

[find_replace_widget.buttons]
replace.background-color = "#007BFF"
replace.text-color = "#ffffff"
undo.background-color = "#FF3B30"
undo.text-color = "#ffffff"

[find_replace_widget.animations]
on_open = "slide-down"
on_close = "fade-out"
find_animation.scroll_view = "pan-and-highlight"
find_animation.multi_page = "slide-to-page-then-pan"

[find_replace_widget.voice_search]
enabled = true
trigger_button = "mic_icon"

[find_replace_widget.ai_suggestions]
enabled = true
highlight_suggestions = true
correction_prompt = "Did you mean: "
```

---

## **Advanced Features & Enhancements**

- **Multi-Device Search Panel**: Results can be displayed on **external screens or devices**.
- **Search Query History (Optional)**: Saves **recent search terms** for faster recall.
- **AI-Powered Corrections**: AI suggests **typo corrections** based on common patterns.
- **Find & Replace Logging**: Logs **past search-replace actions** for user reference.

---

### **Final Thoughts**

The **Find/Replace Widget** brings **precision, efficiency, and adaptability** to in-app search systems. With **AI-enhanced correction, dynamic navigation, and customizable animations**, it **simplifies** text searching while ensuring **developer flexibility**.

---

### **Calendar Widget Documentation**

The **Calendar Widget** provides a structured view of dates, events, and schedules, integrating seamlessly with **task management, scheduling, and event tracking**. It supports multiple display formats, customization options, and multi-device synchronization using UndChain.

---

## **Core Features**

### **1. Calendar Display Modes**

- **Yearly View**: Displays the entire year, highlighting important dates.
- **Monthly View**: Standard **grid-based** view with event markers.
- **Weekly View**: Shows a week’s schedule with hour-based breakdowns.
- **Daily View**: Provides a **detailed agenda** for the selected day.
- **Mini Mode**: A compact, **quick-glance version** of the calendar.
- **Macro Mode**: Full-screen, interactive calendar with deep scheduling features.

### **2. Scheduling & Event Management**

- **Event Creation**: Users can click on any date to **quick-add an event**.
- **Repeating Events**: Set weekly, monthly, or custom recurrence patterns.
- **Event Notifications**: Alerts for upcoming events, meetings, or deadlines.
- **Categories**: Work, Personal, Public, or Custom categories.
- **Privacy Settings**:
  - **Public** (viewable by anyone).
  - **Restricted** (shared with selected users).
  - **Private** (only the owner can view).
- **RSVP Integration**: Users can accept/decline invitations.

### **3. Time-Tracking & Digital Punch Cards**

- **Shift Logging**: Employees can clock in/out via a **punch card interface**.
- **Billable Hours Tracking**: Logs working hours for freelancers & consultants.
- **Work Session Tracking**: Measures time spent on specific tasks/projects.

### **4. Multi-Calendar Support**

- Users can **create multiple calendars** for different projects or teams.
- **Group Calendars**: Share and coordinate schedules with a team.
- **Cross-Application Syncing**:
  - Syncs with **Clock Widget** for task reminders.
  - Compatible with **Scheduler Widget** for integrated event tracking.

### **5. Multi-Device & Display Adaptation**

- **Seamless Syncing Across Devices** (if enabled by user).
- **Custom Themes & Views**:
  - Light & Dark mode support.
  - Adjust font sizes, background colors, and calendar markers.
- **Adaptive Layouts**: Different styling for **desktop, mobile, and multi-screen setups**.

### **6. Custom Event Metadata**

- **Event Type Icons** (meetings, deadlines, reminders, holidays, etc.).
- **Tags for Quick Filtering** (e.g., #work, #travel, #birthday).
- **Attachments**: Users can **attach files, notes, or links** to events.
- **Smart Suggestions**: Auto-suggests locations, invitees, and event names based on past usage.

---

## **M3L Implementation Example**

```toml
[[layout.container.content]]
type = "calendar_widget"
id = "primary_calendar"
title = "Work Calendar"  # Displayed title
data_source = "@Undline/calendar_data.db"  # Storage reference
calendar_type = "Work"  # Options: "Personal", "Work", "Shared", "Public"
display_mode = "macro"  # Options: "mini", "macro"
scheduler_enabled = true  # Enables scheduling features
privacy = "restricted"  # Options: "public", "restricted", "private"
```

---

## **GSS Styling Example**

```toml
[calendar_widget]
font = "Arial, sans-serif"
background_color = "#ffffff"
highlight_today = true
event_border_color = "#007BFF"
animation.on_hover = "scale"

[calendar_widget.mini_mode]
background_color = "#f0f0f0"
font_size = "12px"
padding = "5px"

[calendar_widget.macro_mode]
background_color = "#000000"
font_size = "16px"
padding = "15px"

[calendar_widget.yearly]
grid_line_color = "#dddddd"
marker_color = "#ff4500"

[calendar_widget.monthly]
background_color = "#e0e0e0"
marker_style = "circle"

[calendar_widget.weekly]
time_block_color = "#ffa500"
marker_style = "square"

[calendar_widget.daily]
highlight_appointments = true
event_background_color = "#00ff00"
```

---

## **Final Thoughts**

The **Calendar Widget** is a **powerful and adaptable scheduling tool** that integrates with **various time-tracking, planning, and event-based applications**. With **multi-calendar support, interactive scheduling, and multi-device syncing**, it serves as a **centralized hub** for all time-sensitive tasks and events.

---

### **Scheduler Widget**

The **Scheduler Widget** allows users to add events to their calendar seamlessly. It provides multiple UI display modes, supports **event linking** to the user's calendar, and offers **RSVP functionality** for shared events.

---

## **Core Features**

### **1. Event Creation & Linking**
- Directly links to a **user’s selected calendar**.
- Can be used standalone or embedded into other widgets (e.g., dMail, notifications, etc.).
- Supports **public, private, and group calendar events**.

### **2. Display Modes**
- **Button Mode**: Minimalist UI that adds an event on click.
- **Inline Mode**: Embedded text prompt allowing direct scheduling.
- **Popup Mode**: Expanded UI for selecting details before saving.
- **Compact Mode**: Small UI element that fits inside a larger widget.

### **3. Customizable Event Details**
- `title`: Name of the event.
- `description`: Short summary.
- `start_time`: Start date/time.
- `end_time`: End date/time.
- `location`: Physical or virtual.
- `reminders`: Notification settings.
- `event_type`: Meeting, Deadline, RSVP, etc.

### **4. RSVP & Public Events**
- Users can **RSVP** to an event when invited.
- Events can be marked **private, shared with specific users, or public**.
- **User roles** can be assigned (e.g., host, speaker, attendee).

### **5. Smart Scheduling & AI Assistance**
- Suggests best available time slots based on past scheduling patterns.
- Detects **conflicting events** and provides alternative slots.
- AI can **auto-generate event summaries** based on context.
- Offers an **estimated meeting cost** (if used with dMail for business meetings).

### **6. Time Zone Awareness**
- Detects and syncs with the user’s **time zone** automatically.
- Allows manual **time zone selection** for global scheduling.
- Adjusts for **daylight savings changes** dynamically.

### **7. Privacy & Security Controls**
- Users can **restrict event visibility** (public, friends, private).
- End-to-end encryption for **confidential meeting details**.
- Option to **disable automatic syncing** with other devices.

---

## **M3L Implementation Example**
```toml
[[layout.container.content]]
type = "scheduler_widget"
id = "meeting_scheduler"
display_mode = "popup"  # Options: "button", "inline", "popup", "compact"
calendar_link = "@Undline/work_calendar.m3l"
allow_rsvp = true
require_confirmation = false
reminder_time = "30min"
```

---

## **GSS Styling Example**
```toml
[scheduler_widget]
background_color = "#1E1E1E"
text_color = "#FFFFFF"
border_radius = "8px"
popup_style = "slide_in"
button_style = "rounded"
hover_effect = "pulse"
```

---

## **Final Thoughts**
The **Scheduler Widget** makes event planning seamless across M3L applications. With **event linking, RSVP support, and AI-powered scheduling**, it ensures that users never miss an important meeting or reminder.

---

### **Affiliate Widget**

#### **Overview**

The **Affiliate Widget** enables businesses to integrate **on-chain, verifiable affiliate marketing programs** into their **M3L applications and UndChain stores such as the auction house co-chain**. This **prevents affiliate sniping**, ensures **fair compensation**, and allows **customized commission structures**.

---

## **Core Features**

### **1. Business-Generated & Verified**

- **Affiliate links must be generated by the business selling the product/service.**
- **Each link is tied to a specific marketer/influencer**, ensuring no fraudulent code injection.
- **On-chain verification prevents third-party hijacking or unauthorized commissions.**

### **2. Time-Locked Affiliate Attribution**

- **Default Lock Duration:** **24 hours** *(can be modified by the business)*.
- **Re-clicking a link refreshes the time-lock.** *(If Joe clicks at 4PM, it locks in until 4PM the next day. If Joe clicks again at 8PM, it extends until 8PM the next day.)*
- **Businesses may choose to disable refresh, keeping the original attribution intact.**
- **Once a purchase is completed, affiliate tracking resets unless otherwise configured.**

### **3. Commission Models & Payouts**

- **Supported Commission Types**:
  - **Flat Fee** (fixed payout per sale)
  - **Percentage-Based** (e.g., 10% per sale)
  - **Tiered Rewards** (higher commissions for more sales)
- **Smart Contract Automation**:
  - **Payouts trigger after transaction verification**.
  - **Businesses can set a delay before payouts** *(to prevent abuse/refunds)*.
  - **Affiliate dashboards provide transparency on commissions earned**.

### **4. Expiration & Refreshing**

- **Businesses can set expiration limits** *(e.g., 7 days, 30 days, Infinite)*.
- **Re-clicking an affiliate link extends expiration** unless the business **disables** this feature.
- **Repeat customers remain under the affiliate for the specified duration**, unless they click a new affiliate link.

### **5. Fraud Prevention & Security**

- **No affiliate stacking or "last-click sniping" abuse.**
- **Once an affiliate link is assigned, it remains locked for the set period.**
- **Bots cannot auto-refresh affiliate links due to time-lock constraints.**
- **Affiliates can track performance but cannot modify their links post-generation.**

---

## **M3L Implementation Example**

```toml
[[layout.container.content]]
type = "affiliate_widget"
id = "affiliate_promo_001"
affiliate_link = "UndChain://store/affiliate/xyz123"
time_lock = "24h"  # Customizable: "24h", "7d", "30d", "infinite"
commission_type = "percentage"
commission_value = "10%"  
refreshable = true  # Allows time lock refresh upon re-click
expiration = "30d"  # After 30 days, link expires
tracking = true  # Enables business-side tracking & analytics
```

---

## **GSS Styling Example**

```toml
[affiliate_widget]
background_color = "#f4f4f4"
border_radius = "8px"
padding = "10px"
text_color = "#333"
hover_effect = "highlight"
animation.on_click = "bounce"
```

---

## **Final Thoughts**

The **Affiliate Widget** provides a **secure, transparent, and automated way** for businesses to **integrate affiliate marketing programs** into their **M3L applications and UndChain stores**. With **time-locked commissions, customizable payout structures, and built-in fraud prevention**, it ensures **fairness for both businesses and affiliates**.

---

### **Ad Widget Documentation**

#### **1. Overview**
The **Ad Widget** enables applications and services to integrate advertisements as part of the **Reward Task System (RTS)**. This system ensures that **users are compensated fairly** for their engagement with ads while maintaining **strict user controls** and **preventing exploitative ad practices**.

⚠️ **Important:** If a user **pays AdCoin** to access content, **ads cannot be displayed**. This protects user experience and prevents double monetization.

---

#### **2. The Reward Task System (RTS) & Ads**
The **Reward Task System (RTS)** is a decentralized framework that allows different co-chains to reward users for engagement-based tasks, including ad interaction, content classification, and AI training verification.

🔹 **How Ads Fit Into RTS:**
- Businesses register **ad tasks** within **RTS-compatible co-chains**.
- Users **engage with ads** (e.g., watching a video, answering interactive questions).
- The **system verifies genuine engagement** before triggering an **AdCoin payout**.
- Ads **cannot interfere with content paid for via AdCoin**.

🔹 **Other Use Cases for RTS (Beyond Ads):**
- **Content Classification** (Mimic / Pages Co-Chain).
- **Crowdsourced AI Training** (Mimic Co-Chain).
- **Bug Bounties & Security Reports** (Security Co-Chain).
- **Fitness & Activity Challenges** (Health / Fitness Co-Chains).

---

#### **3. Ad Widget Types**
The **Ad Widget** supports three core ad types:

1. **Banner Ads** – Small, non-intrusive ads displayed within UI components.
2. **Video Ads** – Short video advertisements (skippable or non-skippable based on RTS rules).
3. **Interactive Ads** – Users must complete an interaction (e.g., answering a question) to receive rewards.

💡 **Note:** M3L developers can select **which ad types** they wish to use, but they cannot override **global AdCoin rules**.

---

#### **4. User Control & Ad Restrictions**
To **ensure a positive user experience**, the **Ad Widget follows strict rules**:

- **No Ads on Paid Content:** If a user has spent AdCoin to access content, **ads are disabled automatically**.
- **User Controls:** Users can set ad **preferences** in **Settings**.
- **Cooldown Periods:** Prevents users from **farming AdCoin** by watching ads repeatedly.
- **Verified Engagement:** AI detects **fraudulent interactions** (e.g., muting ads, switching tabs).
- **Transparency:** Users **always know how much AdCoin they earn** before engaging.

---

#### **5. Verification & Anti-Exploit Measures**
To **prevent abuse**, the RTS and Ad Widget use the following protections:

- **Ad Engagement Tracking:** AI detects **genuine engagement** (e.g., no auto-skipping, no muting, active tab focus).
- **Rate Limits & Cooldowns:** Users **can’t farm ads** for infinite AdCoin.
- **Fraud Detection:** Detects **spam behaviors** and bans **exploitive activity**.
- **Penalty System:** Users caught **cheating the system** will lose rewards and perception score.

---

#### **6. M3L Implementation Example**
```toml
[[layout.container.content]]
type = "ad_widget"
id = "homepage_banner_ad"
ad_type = "banner"  # Options: "banner", "video", "interactive"
reward_payout = 10  # AdCoin reward amount (subject to RTS rules)
cooldown = 1800  # Time (in seconds) before another ad task is available
```

---

#### **7. GSS Styling Example**
```toml
[ad_widget]
background_color = "#222222"
border_radius = "10px"
animation.on_hover = "glow"
audio.on_start = "chime.wav"
size = "responsive"  # Auto-adjusts based on screen size
```

---

#### **8. Final Considerations**
- **The Ad Widget must comply with RTS rules.**
- **Users are always informed** about the reward amount before engaging.
- **Ads cannot be displayed** where AdCoin has been used for access.
- **Businesses and developers must register their ad tasks** with an RTS-compatible co-chain.

**The Ad Widget, combined with the Reward Task System, allows UndChain to create the first decentralized, fair, and user-controlled ad economy.**

---

## High-Level Widgets

High-level widgets are the cornerstone of M3L's simplicity and power. By combining multiple low-level widgets into cohesive, reusable components, they allow developers to implement complex functionality with minimal effort. These widgets encapsulate common design patterns, enabling a consistent look and feel across applications while simplifying development workflows.

---

### **Clock Widget Documentation**

The **Clock Widget** provides real-time timekeeping functionality and serves as a versatile tool for users. It supports multiple display modes, world clock features, and additional time-based utilities like a stopwatch and countdown timer. The Clock Widget is standalone but can integrate with the **Scheduler inside the Calendar Widget** if enabled.

---

## **Core Features**

### **1. Time Display Modes**
- **Digital Mode**: Displays time in a numerical format (12-hour or 24-hour toggleable).
- **Analog Mode**: A graphical clock face with moving hands.
- **World Clock**: Displays multiple time zones at once (if enabled by the user).
- **Custom Time Zones**: Users can manually select and pin different time zones.

### **2. Additional Timekeeping Tools**
- **Stopwatch**: Tracks elapsed time with start, stop, and reset buttons.
- **Countdown Timer**: Allows users to set a time duration that counts down to zero.
- **Multi-Timer Support**: Users can set multiple countdowns at once for different tasks.

### **3. Task & Event Integration (Optional)**
- If **Scheduler is enabled in the Calendar Widget**, the **Clock Widget can pull the next three scheduled events**.
- If **Scheduler is disabled**, the Clock remains a standalone time display.
- Users can enable/disable this functionality in the **Settings Menu**.

### **4. Display & Customization**
- **Full-Screen Mode**: Expands the clock to take up an entire display.
- **Mini Mode**: A compact, always-visible clock (can be docked or floating).
- **Custom Skins & Styles**: GSS designers can create different clock themes (e.g., futuristic, retro, minimalist).
- **Multi-Device Support**: The clock can sync across multiple screens if allowed in settings.

### **5. Animation & Interaction Options**
- **Smooth Animations**: Clock hands move fluidly in **analog mode**.
- **On-Hover Effects**: GSS designers can add hover effects to change the appearance of the clock.
- **User Input Triggers**:
    - **Double-click** toggles between digital and analog.
    - **Right-click** (or equivalent) opens quick settings.
    - **Middle-click** resets the stopwatch (if active).

### **6. Time Syncing & Precision**
- **Network Time Sync**: Option to pull accurate time from a global time server.
- **Offline Mode**: Uses the system clock when no network is available.
- **Time Drift Correction**: Adjusts automatically if network sync detects drift.

### **7. Notifications & Alerts**
- Users can **set alarms within the Scheduler** (if enabled).
- Optional **reminders for upcoming tasks** (pulled from the Calendar Widget).
- **Chimes & Sounds**: Custom sound profiles for different alerts (configurable in settings).

---

## **M3L Implementation Example**
```toml
[[layout.container.content]]
type = "clock_widget"
id = "desktop_clock"
mode = "digital"  # Options: "digital", "analog", "world_clock"
time_zone = "UTC-5"
display_mode = "mini"  # Options: "full", "mini", "docked"

# Optional: Enable Scheduler Integration
show_scheduled_tasks = true
calendar_sync = true  # Allows event previews
```

---

## **GSS Styling Example**
```toml
[clock_widget]
font = "Orbitron, sans-serif"
background_color = "#000000"
text_color = "#ffffff"
border_radius = "10px"
hover_effect = "glow"
animation.on_hover = "pulse"

# Analog Mode Styling
[clock_widget.analog]
clock_face = "modern"
hand_color = "#ffffff"
second_hand_color = "#ff0000"

# World Clock Styling
[clock_widget.world_clock]
background_color = "#222222"
text_color = "#00ffcc"
```

---

## **Final Thoughts**
The **Clock Widget** provides a **fully customizable, multi-functional timekeeping system** that fits into **any user interface**. With support for **multiple display modes, synchronization options, and extended scheduling integration**, it’s a **powerful yet lightweight** addition to any M3L-designed application.

Would you like to proceed to the **Calendar & Scheduler Widget next**, or refine anything here first?

---

### Key Advantages

1. **Ease of Use**:
   High-level widgets reduce development time by abstracting repetitive layouts and behaviors into ready-to-use components. Developers can focus on functionality without worrying about reinventing standard UI patterns.

2. **User Familiarity**:
   Standardized high-level widgets provide end-users with intuitive experiences, as they align with commonly recognized design schemes. Users can interact confidently with your application, even on first use.

3. **Dynamic Adaptability**:
   These widgets seamlessly inherit GSS styling, allowing designers to create unique, theme-driven experiences while maintaining a unified system-wide aesthetic.

4. **Backwards Compatibility**:
   As the M3L standard evolves, new high-level widgets may be introduced. If a GSS file does not include styling for these widgets, the system gracefully defaults to their low-level widget composition, adhering to the documented formula for fallback behavior.

5. **Page-Centric Design**:
   Most high-level widgets are intended to dominate a page or serve as the primary interface for an application. While some, like the Hero Section, can be "stacked" alongside other content, many high-level widgets, such as Asset View, are designed for standalone use. The distinction allows developers to balance flexibility with simplicity.

   - **Standalone Widget Example**: The Asset View widget provides a comprehensive shopping interface where nearly the entire page functionality revolves around its predefined components.
   - **Stackable Widget Example**: The Hero Section can sit at the top of a page and work seamlessly with other content, creating a visually engaging introduction while allowing flexibility below.

6. **Custom M3L Integration**:
   While high-level widgets provide standardized functionality, developers can still link to custom M3L pages from within them. For example, a link in an Asset View widget might redirect to a custom product details page designed with low-level widgets for tailored experiences.

---

### Maintenance Considerations

To keep applications visually consistent and cutting-edge, GSS designers should periodically review and update their stylesheets to include definitions for new high-level widgets. This ensures all elements take full advantage of the latest features and visual standards.

---

### Examples of High-Level Widgets

- **Asset View**: A comprehensive shopping interface for listing, filtering, and purchasing items.
- **Hero Section**: A visually engaging introduction to a page or product.
- **Dashboard**: An interactive hub for data visualization and user actions.
- **Node Editor**: A graphical interface for managing interconnected components, useful in workflows or visual programming.

---

### Future Expansion

As M3L evolves, the library of high-level widgets will grow to accommodate emerging trends and user needs. Developers and designers alike are encouraged to provide feedback and suggestions, ensuring the system remains flexible and future-proof.

---

High-level widgets showcase the power and versatility of M3L, making it easier than ever to build applications that are both intuitive and functional. With these robust tools at their disposal, developers can focus on creating impactful user experiences with minimal overhead.

---

### **Asset View Widget**

**Asset View**: Provides a comprehensive shopping experience with product grids, sorting tools, a shopping cart, detailed asset sections, and return management systems. This widget is designed for both digital and physical marketplaces, offering flexibility and customization to meet diverse needs.

---

### **Core Features**

1. **Dynamic Data Sources**:

   - Pull asset data dynamically from:
     - **UndChain Database**: Ensures secure, decentralized transactions using co-chains such as SQeeL.
     - **Static Datasets**: Useful for testing, debugging, or fixed inventories.

2. **Featured Items**:

   - A carousel highlights up to 10 featured items, cycling dynamically based on user behavior or developer-defined priorities.

3. **Shopping Cart Integration**:

   - Allows users to add items to a cart, with real-time updates and subtotal calculations.
   - Supports item holds for limited-stock assets and restrictions for high-demand items.
   - Includes the ability to add multiples of the same item, unless restricted by stock levels.

4. **Sorting and Filtering**:

   - Built-in sorting tools for price, popularity, and ratings.
   - Advanced filters for categories, contract types, availability, and user-defined preferences.

5. **Subscription Support**:

   - Users can opt for recurring subscriptions or one-time purchases for applicable assets.

6. **Dynamic Comparison**:

   - Compare similar items side-by-side, dynamically updating if stock levels or details change.

7. **Return Management System**:

   - Supports an integrated RMA (Return Merchandise Authorization) system.
   - Allows customers to initiate return requests and receive return shipping labels.
   - Tracks return data for analytics and customer service improvement.

8. **User Roles**:

   - Includes role-based access controls to limit analytics, sales data, or return visibility to appropriate users.

9. **Analytics Integration**:

   - Tracks user interactions like clicks, favorites, time spent on items, and return rates.
   - Generates data for marketing insights, inventory management, and user engagement analysis.

10. **Settings and Personalization**:

   - Captures browse history, purchase history, and user preferences for better personalization.
   - Supports favorites and wishlists for easy access to frequently viewed or desired items.

11. **Customizability**:

    - Developers can override details pages, checkout processes, or return systems as needed.
    - Sections can be overloaded by M3L designers to include additional text or functions.

12. **Accessibility**:

    - Fully navigable via keyboard and screen readers.
    - High-contrast modes and dynamic layout adjustments for touch and controller inputs.

13. **Animations**:

    - GSS designers can define animations for every widget within the asset view, allowing custom transitions, hover effects, and interaction feedback.

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "asset_view"
data_source = "SQeeL://marketplace/assets.db"
featured_items = [ "item1", "item2", "item3" ]
sorting_options = [ "price", "popularity", "ratings" ]
filters = [ "category", "contract_type", "availability" ]
cart_enabled = true
subscriptions = true
comparison_enabled = true
returns_enabled = true
user_roles = [ "admin", "manager", "viewer" ]
```

---

### **Example GSS Implementation**

```toml
[asset_view]
background = "#FFF"

[asset_grid.item]
padding = "10px"
background = "#F9F9F9"
hover.background = "#EEE"

[asset_grid.item.contract]
color = "#00FF00"

[featured_items.carousel]
duration = "5s"
transition = "ease-in-out"

[cart.icon]
size = "24px"
color = "#007BFF"

[filters.dropdown]
background = "#EEE"
border = "1px solid #CCC"

[animations.add_to_cart]
type = "bounce"
duration = "0.3s"

[animations.featured_cycle]
type = "slide-in"
duration = "0.5s"
```

---

### **Advanced Considerations**

#### **Dynamic Comparison**
   - Items in the comparison list dynamically update if stock levels or details change.

#### **Promotions and Campaigns**
   - Developers can integrate banners or dedicated widgets to highlight promotions.

#### **Return Management System**
   - Users can request returns directly from the asset view.
   - RMA tracking for store owners to process return requests.
   - Notifications for users on return status updates.

#### **User Roles and Permissions**
   - Analytics, sales data, and return data can be restricted to specific roles.

#### **Localization**
   - Support localized currencies and languages for a global audience.

---

### **Use Cases**

- **E-Commerce**: Digital marketplaces for assets like NFTs or physical goods.
- **Subscription Services**: Platforms offering monthly or yearly subscriptions.
- **Specialized Applications**: Niche tools like component selection systems for engineering or manufacturing.

---

### ***Default M3L Implementation for Asset View**

In the event that an M3L designer does not implement a custom layout for the Asset View widget, a default structure will be used to ensure usability and consistency. Below is the standardized implementation:



---

### **Conclusion**

The Asset View Widget is a powerful, versatile tool for creating robust shopping and browsing experiences. With its rich feature set and dynamic customization options, it empowers developers to build applications that cater to diverse audiences and business needs.

---

## Summary

This appendix showcases the flexibility and modularity of M3L and GSS through a comprehensive widget catalog. Developers can use these examples to create visually consistent and functional applications while ensuring compatibility with future enhancements.