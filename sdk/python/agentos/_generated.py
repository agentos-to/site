"""Auto-generated TypedDict classes from shape YAML — do not edit.

Generated from 73 shapes.
Regenerate with: python generate.py --lang python
"""

from __future__ import annotations

from typing import Any, TypedDict

class Account(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountType: str
    bio: str
    color: str
    displayName: str
    email: str
    handle: str
    identifier: str
    isActive: bool
    issuer: str
    joinedDate: str
    lastActive: str
    phone: str
    followers: list[Account]
    follows: list[Account]
    owner: Person
    platform: Product


class Activity(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    action: str
    changedKeys: list[str]
    duration: float
    published: str
    success: bool
    toolName: str
    folder: Folder
    session: Session


class Actor(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str


class Agent(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    model: str
    provider: str
    sessionId: str


class Aircraft(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    currency: str
    department: str
    iataCode: str
    icaoCode: str
    images: Any
    model: str
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    rangeKm: int
    seatCapacity: int
    servingSize: str
    sku: str
    soldByWeight: bool
    variant: str
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    manufacturer: Organization
    tagged: list[Tag]


class Album(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contains: list[Image]


class App(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    app_id: str
    description: str
    entity_types: Any
    standalone: bool


class Book(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    awardsWon: list[str]
    barcode: str
    calories: float
    categories: list[str]
    characters: list[str]
    currency: str
    department: str
    format: str
    genres: list[str]
    images: Any
    isbn: str
    isbn13: str
    language: str
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    originalTitle: str
    pages: int
    places: list[str]
    price: str
    priceAmount: float
    quantity: int
    series: str
    servingSize: str
    sku: str
    soldByWeight: bool
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    contributors: list[Person]
    manufacturer: Organization
    publisher: Organization
    tagged: list[Tag]
    writtenBy: Person


class Branch(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    ahead: int
    behind: int
    commit: str
    isCurrent: bool
    isRemote: bool
    upstream: str
    repository: Repository


class Brand(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    country: str
    founded: str
    tagline: str
    ownedBy: Organization
    website: Website


class Calendar(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accessRole: str
    backgroundColor: str
    calendarId: str
    color: str
    foregroundColor: str
    isPrimary: bool
    isReadonly: bool
    source: str
    timezone: str
    events: list[Event]
    owner: Person


class Channel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    banner: str
    platform: Product


class Class(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    activityType: str
    allDay: bool
    capacity: int
    dateUpdated: str
    endDate: str
    eventType: str
    icalUid: str
    isFull: bool
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    spotsRemaining: int
    startDate: str
    status: str
    timezone: str
    visibility: str
    attachments: list[File]
    creator: Person
    instructor: Person
    involves: list[Person]
    location: Place
    organizer: Person
    platform: Product
    venue: Place


class Community(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    privacy: str
    platform: Product


class Conversation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountEmail: str
    cwd: str
    gitBranch: str
    isArchived: bool
    isGroup: bool
    messageCount: int
    unreadCount: int
    in_: Folder  # in
    message: list[Message]
    participant: list[Actor]
    platform: Product


class DnsRecord(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    domain: str
    recordName: str
    recordType: str
    ttl: int
    values: list[str]


class Document(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    abstract: str
    contentType: str
    encoding: str
    filename: str
    format: str
    kind: str
    language: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    tableOfContents: str
    wordCount: int
    attachedTo: Message
    author: Actor
    citedBy: list[Document]
    references: list[Document]
    repository: Repository


class Domain(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    autoRenew: bool
    expiresAt: str
    nameservers: list[str]
    registrar: str
    status: str


class Email(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountEmail: str
    attachments: Any
    authResults: str
    bccRaw: str
    bodyHtml: str
    ccRaw: str
    deliveredTo: str
    hasAttachments: bool
    inReplyTo: str
    isAutomated: bool
    isDraft: bool
    isOutgoing: bool
    isSent: bool
    isSpam: bool
    isStarred: bool
    isTrash: bool
    isUnread: bool
    listId: str
    mailer: str
    manageSubscription: str
    messageId: str
    precedence: str
    references: str
    replyTo: str
    returnPath: str
    sizeEstimate: int
    subject: str
    toRaw: str
    unsubscribe: str
    unsubscribeOneClick: bool
    bcc: list[Account]
    cc: list[Account]
    ccDomain: list[Domain]
    domain: Domain
    from_: Account  # from
    inConversation: Conversation
    platform: Product
    repliesTo: Message
    tag: list[Tag]
    to: list[Account]
    toDomain: list[Domain]
    toolCalls: list[ToolCall]


class Episode(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    durationMs: int
    episodeNumber: int
    seasonNumber: int
    guest: list[Person]
    series: Podcast
    transcribe: Transcript


class Event(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    dateUpdated: str
    endDate: str
    eventType: str
    icalUid: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    platform: Product


class File(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    encoding: str
    filename: str
    format: str
    kind: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    attachedTo: Message
    repository: Repository


class Folder(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    hasReadme: bool
    path: str
    workspaceType: str
    contains: list[File]
    repository: Repository


class GitCommit(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    additions: int
    committedAt: str
    deletions: int
    filesChanged: int
    message: str
    sha: str
    shortHash: str
    author: Account
    committer: Account
    parent: GitCommit
    repository: Repository


class Group(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    category: str
    memberCount: int


class Hardware(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    currency: str
    department: str
    images: Any
    modelNumber: str
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    serialNumber: str
    servingSize: str
    sku: str
    soldByWeight: bool
    specs: Any
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    manufacturer: Organization
    tagged: list[Tag]


class Image(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    altText: str
    appName: str
    displayId: int
    displayIndex: int
    encoding: str
    filename: str
    format: str
    height: int
    kind: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    width: int
    windowId: int
    attachedTo: Message
    repository: Repository


class Invitation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    acceptedAt: str
    email: str
    expiresAt: str
    invitationType: str
    message: str
    revokedAt: str
    role: str
    status: str
    token: str
    invitee: Account
    inviter: Account
    organization: Organization
    platform: Product


class Job(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    boot_epoch: int
    config: Any
    kind: str
    status: str
    produced: Conversation
    requested_by: Account


class Leg(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrivalTime: str
    cabinClass: str
    carbonEmissions: Any
    departureTime: str
    duration: str
    durationMinutes: int
    flightNumber: str
    layoverMinutes: int
    polyline: str
    sequence: int
    trace: Any
    tracePointCount: int
    vehicleType: str
    aircraft: Aircraft
    carrier: Organization
    destination: Place
    origin: Place
    trip: Trip


class List(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isDefault: bool
    isPublic: bool
    listId: str
    listType: str
    privacy: str
    belongsTo: Account
    contains: list[Product]
    platform: Product


class LoadedModel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    digest: str
    expiresAt: str
    quantization: str
    size: str
    sizeVram: int
    vramUsage: str


class Meeting(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    calendarLink: str
    conferenceProvider: str
    dateUpdated: str
    endDate: str
    eventType: str
    icalUid: str
    isVirtual: bool
    meetingUrl: str
    phoneDialIn: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    platform: Product
    transcribe: Transcript


class Memex(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    description: str
    edgeCount: int
    filePath: str
    fileSize: str
    nodeCount: int
    origin: str
    published: bool
    snapshotOf: str
    forkedFrom: Memex
    owner: Person
    snapshots: list[Memex]


class Message(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isOutgoing: bool
    isStarred: bool
    from_: Actor  # from
    inConversation: Conversation
    platform: Product
    repliesTo: Message
    toolCalls: list[ToolCall]


class Model(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contextLength: int
    contextWindow: int
    digest: str
    family: str
    format: str
    maxOutput: int
    modality: list[str]
    modelType: str
    parameterSize: str
    pricingInput: str
    pricingOutput: str
    provider: str
    quantization: str
    quantizationLevel: str
    size: str


class Note(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isPinned: bool
    noteType: str
    createdBy: Person
    extractedFrom: Webpage
    references: list[Note]


class Offer(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    availability: str
    bookingToken: str
    currency: str
    offerType: str
    price: float
    validFrom: str
    validUntil: str
    for_: Product  # for
    offeredBy: Organization
    trips: list[Trip]


class Order(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    currency: str
    deliveryDate: str
    deliveryFee: float
    eta: str
    fareBreakdown: Any
    orderDate: str
    orderId: str
    originalTotal: str
    originalTotalAmount: float
    savings: float
    status: str
    subtotal: float
    summary: str
    taxes: float
    tipAmount: float
    total: str
    totalAmount: float
    contains: list[Product]
    delivery: Trip
    platform: Platform
    shippingAddress: Place
    store: Place
    tracking: Webpage


class Organization(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    founded: str
    industry: str
    domain: Domain
    headquarters: Place
    member: list[Person]
    website: Website


class Person(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    about: str
    actorType: str
    birthday: str
    firstName: str
    gender: str
    joinedDate: str
    lastActive: str
    lastName: str
    middleName: str
    nickname: str
    notes: str
    accounts: list[Account]
    location: Place
    roles: list[Role]
    website: Website


class Place(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accuracy: str
    businessStatus: str
    categories: list[str]
    city: str
    country: str
    countryCode: str
    district: str
    featureType: str
    fullAddress: str
    googlePlaceId: str
    hours: Any
    latitude: float
    locality: str
    longitude: float
    mapboxId: str
    neighborhood: str
    phone: str
    placeFormatted: str
    postalCode: str
    priceLevel: str
    rating: float
    region: str
    reviewCount: int
    street: str
    streetNumber: str
    timezone: str
    website: str
    wikidataId: str
    brand: Organization
    offers: list[Product]


class Platform(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    currency: str
    department: str
    images: Any
    license: str
    novaGroup: int
    nutritionScore: str
    openSource: bool
    originalPrice: str
    originalPriceAmount: float
    platform: list[str]
    platformType: str
    price: str
    priceAmount: float
    quantity: int
    repositoryUrl: str
    servingSize: str
    sku: str
    soldByWeight: bool
    version: str
    website: str
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    developer: Organization
    manufacturer: Organization
    repository: Repository
    tagged: list[Tag]


class Playlist(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isDefault: bool
    isPublic: bool
    listId: str
    listType: str
    privacy: str
    belongsTo: Account
    contains: list[Video]
    platform: Product


class Podcast(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    feedUrl: str
    episode: list[Episode]
    host: list[Person]
    platform: Product


class Post(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    externalUrl: str
    postType: str
    attachment: list[File]
    contains: list[Video]
    media: list[Image]
    postedBy: Account
    publish: Community
    replies: list[Post]
    repliesTo: Post


class Product(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    currency: str
    department: str
    images: Any
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    servingSize: str
    sku: str
    soldByWeight: bool
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    manufacturer: Organization
    tagged: list[Tag]


class Project(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    color: str
    state: str


class Quote(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    context: str
    year: int


class Repository(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    defaultBranch: str
    forks: int
    isArchived: bool
    isPrivate: bool
    language: str
    license: str
    openIssues: int
    size: int
    stars: int
    topics: list[str]
    forkedFrom: Repository
    owner: Account


class Result(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    indexedAt: str
    resultType: str


class Review(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    externalUrl: str
    isVerified: bool
    postType: str
    rating: float
    ratingMax: float
    tags: list[str]
    attachment: list[File]
    contains: list[Video]
    media: list[Image]
    postedBy: Account
    publish: Community
    replies: list[Post]
    repliesTo: Post
    reviews: Product


class Role(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    department: str
    endDate: str
    roleType: str
    startDate: str
    title: str
    organization: Organization
    person: Person


class Search(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    query: str
    resultCount: int
    searchCount: int
    searchedAt: str


class Session(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    client: str
    endedAt: str
    gitBranch: str
    messageCount: int
    projectId: str
    sessionType: str
    startedAt: str
    tokenCount: int
    folder: Folder
    participant: Actor


class Shelf(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isDefault: bool
    isExclusive: bool
    isPublic: bool
    listId: str
    listType: str
    privacy: str
    belongsTo: Account
    contains: list[Book]
    platform: Product


class Shortcut(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    builtin: bool
    filter: str
    target: str
    skill: Skill


class Simulation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actionCount: int
    endedAt: str
    graphMode: str
    profile: str
    startedAt: str
    status: str
    task: str
    writeCount: int
    agent: Agent
    forkedFrom: Simulation
    mountedMemex: list[Memex]
    primaryMemex: Memex
    startedBy: Person
    tether: Hardware


class Skill(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    color: str
    description: str
    error: str
    skillId: str
    status: str
    privacyPolicy: Webpage
    termsOfService: Webpage
    website: Website


class Software(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    currency: str
    department: str
    images: Any
    license: str
    novaGroup: int
    nutritionScore: str
    openSource: bool
    originalPrice: str
    originalPriceAmount: float
    platform: list[str]
    price: str
    priceAmount: float
    quantity: int
    repositoryUrl: str
    servingSize: str
    sku: str
    soldByWeight: bool
    version: str
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    developer: Organization
    manufacturer: Organization
    repository: Repository
    tagged: list[Tag]


class Source(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    address: str
    description: str
    enabled: bool
    lastSynced: str
    platform: str
    sourceId: str
    folder: Folder


class Spec(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    encoding: str
    filename: str
    format: str
    kind: str
    labels: list[str]
    lineCount: int
    mimeType: str
    path: str
    priority: int
    problem: str
    remoteId: str
    sha: str
    size: int
    startedAt: str
    state: str
    successCriteria: str
    targetDate: str
    assignedTo: Person
    attachedTo: Message
    blockedBy: list[Task]
    blocks: list[Task]
    children: list[Task]
    dependsOn: list[Spec]
    parent: Task
    project: Project
    repository: Repository
    supersedes: list[Spec]


class Tag(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    color: str
    tagType: str


class Task(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    labels: list[str]
    priority: int
    remoteId: str
    startedAt: str
    state: str
    targetDate: str
    assignedTo: Person
    blockedBy: list[Task]
    blocks: list[Task]
    children: list[Task]
    parent: Task
    project: Project
    repository: Repository


class Theme(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    colorScheme: str
    description: str
    family: str
    themeId: str
    wallpaper: Image


class ToolCall(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    durationMs: int
    input: str
    isError: bool
    output: str
    from_: Actor  # from
    inMessage: Message
    platform: Product
    repliesTo: ToolCall


class Transaction(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    amount: float
    balance: float
    category: str
    currency: str
    details: Any
    notes: str
    pending: bool
    postingDate: str
    recurring: bool
    type: str
    account: Account


class Transcript(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contentRole: str
    durationMs: int
    language: str
    segmentCount: int
    segments: Any
    sourceType: str


class Trip(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrivalTime: str
    bookingToken: str
    cabinClass: str
    carbonEmissions: Any
    currency: str
    departureTime: str
    distance: str
    duration: str
    durationMinutes: int
    fare: str
    fareAmount: float
    isScheduled: bool
    isSurge: bool
    rating: str
    status: str
    stops: int
    trackingUrl: str
    tripType: str
    vehicleType: str
    carrier: Organization
    destination: Place
    driver: Person
    legs: list[Leg]
    order: Order
    origin: Place


class Video(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    codec: str
    durationMs: int
    encoding: str
    filename: str
    format: str
    frameRate: float
    kind: str
    lineCount: int
    mimeType: str
    path: str
    resolution: str
    sha: str
    size: int
    addTo: Playlist
    attachedTo: Message
    channel: Channel
    repository: Repository
    transcribe: Transcript


class Volume(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    filesystem: str
    freeBytes: int
    path: str
    readOnly: bool
    removable: bool
    totalBytes: int
    usedBytes: int
    volumeType: str
    contains: list[Folder]


class Webpage(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contentType: str
    error: str
    lastVisitUnix: int
    visitCount: int


class Website(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    anonymous: bool
    claimToken: str
    claimUrl: str
    expiresAt: str
    status: str
    versionId: str
    domain: Domain
    ownedBy: Organization

