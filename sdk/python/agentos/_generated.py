"""Auto-generated TypedDict classes from shape YAML — do not edit.

Generated from 104 shapes.
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
    display: str
    displayName: str
    email: str
    handle: str
    identifier: str
    isActive: bool
    issuer: str
    joinedDate: str
    lastActive: str
    lastProfileFetch: str
    metadata: Any
    phone: str
    userId: str
    at: Actor
    authenticatedVia: Account
    followers: list[Account]
    follows: list[Account]
    operator: Actor
    owner: Person
    previousIdentity: list[Account]
    protocol: Protocol
    via: Product


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
    allDay: bool
    changedKeys: list[str]
    currentUrl: str
    dateUpdated: str
    distinctId: str
    duration: float
    endDate: str
    icalUid: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    success: bool
    timezone: str
    toolName: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    folder: List
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person
    session: McpSession


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
    category: str
    currency: str
    customizationGroups: Any
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
    creator: list[Actor]
    inspiredBy: list[Product]
    manufacturer: Organization
    tagged: list[Tag]


class Airline(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    alliance: str
    callsign: str
    country: str
    iataCode: str
    icaoCode: str
    industry: str
    domain: Domain
    headquarters: Place
    member: list[Person]
    parentOrganization: Organization
    website: Website


class Airport(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    city: str
    country: str
    countryCode: str
    elevationFt: int
    iataCode: str
    icaoCode: str
    terminalCount: int
    timezone: str
    location: Place
    operator: Organization


class App(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    defaultView: str
    handles: list[str]
    iconRole: str
    isSystem: bool
    route: str


class Birth(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    additionalName: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    familyName: str
    gender: str
    givenName: str
    honorificPrefix: str
    honorificSuffix: str
    icalUid: str
    legalName: str
    maidenName: str
    nameOrder: str
    nickname: str
    phoneticFamilyName: str
    phoneticGivenName: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sortAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person


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
    category: str
    characters: list[str]
    copyrightYear: int
    coverage: str
    currency: str
    customizationGroups: Any
    dateCreated: Any
    department: str
    description: str
    format: str
    genres: list[str]
    images: Any
    isbn: str
    isbn13: str
    language: str
    license: str
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
    tags: list[str]
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    contributors: list[Person]
    copyrightHolder: Person
    creator: list[Actor]
    inspiredBy: list[Product]
    manufacturer: Organization
    published_by: Actor
    tagged: list[Tag]
    written_by: Person


class BookingOffer(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    approvedAt: str
    baseAmount: float
    blob: str
    cartId: str
    checkoutUrl: str
    conditions: Any
    confirmEndpoint: str
    contactEmail: str
    contactPhone: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    expiresAt: str
    feesAmount: float
    hasVoidWindow: bool
    icalUid: str
    isChangeable: bool
    isRefundable: bool
    itineraryHash: str
    preparedAt: str
    presentedAt: str
    properties: Any
    recurrence: list[str]
    referenceNumber: str
    review: str
    showAs: str
    signature: str
    signatureAlg: str
    signedBy: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    taxAmount: float
    timezone: str
    totalAmount: float
    visibility: str
    voidWindowEndsAt: str
    account: Account
    at: Actor
    attachments: list[File]
    becameReservation: Reservation
    becameTransaction: Transaction
    billingAddress: Place
    broker: Actor
    buyers: list[Person]
    creator: Person
    derivedFrom: Offer
    fares: list[Fare]
    guests: list[Person]
    involves: list[Person]
    location: Place
    membership: Membership
    organizer: Person
    paymentMethod: PaymentMethod
    person: Person
    reservedItems: list[Pass]
    taxLines: list[TaxLine]
    trips: list[Trip]
    underName: Person


class Bookmark(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    target: Any


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
    primaryColor: str
    tagline: str
    textColor: str
    logo: Image
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
    at: Actor
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
    subscriberCount: int
    at: Actor


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
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    isFull: bool
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    spotsRemaining: int
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    instructor: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person
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
    allowCrypto: bool
    memberCount: int
    privacy: str
    subscriberCount: int
    at: Actor


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
    historyId: str
    isArchived: bool
    isGroup: bool
    messageCount: int
    source: str
    unreadCount: int
    at: Actor
    in_: List  # in
    message: list[Message]
    participant: list[Actor]


class Conversion(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    factor: float
    icalUid: str
    kind: str
    properties: Any
    rate: float
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    from_: Unit  # from
    involves: list[Person]
    location: Place
    organizer: Person
    parameter: Any
    person: Person
    to: Unit


class CreativeWork(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    language: str
    license: str
    tags: list[str]
    contributors: list[Person]
    copyrightHolder: Person
    published_by: Actor
    written_by: Person


class Credential(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    domain: str
    identifier: str
    itemType: str
    lastVerified: str
    obtainedAt: str
    refreshable: bool
    source: str
    storeRowId: int
    account: Account
    at: Organization
    writtenBy: Skill


class Dimension(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    amount: int
    current: int
    dimensionless: bool
    key: str
    label: str
    length: int
    luminous: int
    mass: int
    temperature: int
    time: int
    baseUnit: Unit


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
    priority: int
    recordId: str
    recordName: str
    recordType: str
    ttl: int
    type: str
    values: list[str]


class Document(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
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
    conversationId: str
    deliveredTo: str
    draftId: str
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
    at: Actor
    bcc: list[Account]
    cc: list[Account]
    ccDomain: list[Domain]
    domain: Domain
    from_: Account  # from
    inConversation: Conversation
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
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person


class Fare(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    basePrice: float
    bookingCode: str
    changeable: bool
    class_: str  # class
    components: int
    conditions: Any
    currency: str
    fareFamily: str
    identifier: str
    milesEarned: int
    passengerType: str
    pointsEarned: int
    productType: str
    refundable: bool
    restrictions: list[str]
    at: Actor
    earnsInto: Membership
    for_: Trip  # for
    legs: list[Leg]
    offer: Offer
    reservation: Reservation
    taxLines: list[TaxLine]


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


class FinancialAccount(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountId: str
    accountNumber: str
    accountType: str
    available: float
    balance: float
    cardType: str
    creditLimit: float
    currency: str
    identifier: str
    interestRate: float
    last4: str
    minimumPayment: float
    routingNumber: str
    accessedVia: Account
    at: Actor
    owner: Person


class Flight(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrivalTime: str
    cabinClass: str
    carbonEmissions: Any
    currentUrl: str
    dateUpdated: str
    departureTime: str
    distinctId: str
    duration: str
    durationMinutes: int
    endDate: str
    flightNumber: str
    icalUid: str
    layoverMinutes: int
    polyline: str
    properties: Any
    recurrence: list[str]
    sequence: int
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    stops: int
    timezone: str
    trace: Any
    tracePointCount: int
    vehicleType: str
    visibility: str
    aircraft: Aircraft
    airline: Airline
    arrivesAt: Airport
    at: Actor
    attachments: list[File]
    carrier: Organization
    creator: Person
    departsFrom: Airport
    destination: Place
    involves: list[Person]
    location: Place
    organizer: Person
    origin: Place
    person: Person
    trip: Trip


class Font(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    designerUrl: str
    family: str
    formats: list[str]
    genericFamily: str
    glyphCount: int
    language: str
    license: str
    licenseInfoUrl: str
    postscriptName: str
    scripts: list[str]
    styles: list[str]
    tags: list[str]
    vendorUrl: str
    weights: list[int]
    contributors: list[Person]
    copyrightHolder: Person
    published_by: Actor
    written_by: Person


class GitCommit(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    datePublished: str
    content: str
    additions: int
    allDay: bool
    committedAt: str
    currentUrl: str
    dateUpdated: str
    deletions: int
    distinctId: str
    endDate: str
    filesChanged: int
    icalUid: str
    message: str
    properties: Any
    recurrence: list[str]
    sha: str
    shortHash: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    author: Account
    committer: Account
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    parent: GitCommit
    person: Person
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
    category: str
    currency: str
    customizationGroups: Any
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
    creator: list[Actor]
    inspiredBy: list[Product]
    manufacturer: Organization
    tagged: list[Tag]


class HealthBiomarker(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    analyteType: str
    category: str
    description: str
    loincCode: str
    measure: str
    panels: list[HealthPanel]


class HealthCondition(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    bodySite: str
    clinicalArea: str
    clinicalStatus: str
    icd10Code: str
    mitigation: str
    proximity: str
    severity: str
    snomedCode: str
    verificationStatus: str
    evidence: list[File]
    subject: Person


class HealthImmunization(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    cvxCode: str
    dateAdministered: str
    dateUpdated: str
    diseaseTarget: str
    distinctId: str
    doseNumber: int
    endDate: str
    icalUid: str
    lotNumber: str
    manufacturer: str
    notes: str
    properties: Any
    recurrence: list[str]
    route: str
    seriesDoses: int
    showAs: str
    site: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    administeredAt: HealthLab
    at: Actor
    attachments: list[File]
    creator: Person
    evidence: list[File]
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person
    subject: Person


class HealthLab(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accreditation: str
    actorType: str
    ccn: str
    cliaNumber: str
    industry: str
    labType: str
    npi: str
    domain: Domain
    headquarters: Place
    member: list[Person]
    parentOrganization: Organization
    website: Website


class HealthObservation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    community: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    externalUrl: str
    flag: str
    icalUid: str
    indexedAt: str
    notes: str
    postId: str
    properties: Any
    recurrence: list[str]
    refHigh: float
    refLow: float
    refText: str
    resultType: str
    score: int
    showAs: str
    similarity: float
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    value: float
    valueText: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    document: File
    fromPanel: HealthPanel
    involves: list[Person]
    location: Place
    measures: HealthBiomarker
    organizer: Person
    person: Person
    reportedRange: HealthReferenceRange
    subject: Person


class HealthPanel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    default_view: str
    description: str
    distinctId: str
    endDate: str
    fasting: bool
    icalUid: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    ordering_mode: str
    panelCode: str
    path: str
    privacy: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sort_by: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    background_image: Image
    belongsTo: Account
    contains: list[Any]
    creator: Person
    document: File
    involves: list[Person]
    location: Place
    organizer: Person
    performedAt: HealthLab
    person: Person
    subject: Person


class HealthProcedure(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    bodySite: str
    cptCode: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    findings: str
    followUp: str
    icalUid: str
    outcome: str
    performedDate: str
    procedureType: str
    properties: Any
    recurrence: list[str]
    showAs: str
    snomedCode: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    evidence: list[File]
    involves: list[Person]
    location: Place
    orderedBy: Person
    organizer: Person
    performedAt: HealthLab
    performer: Person
    person: Person
    subject: Person
    treats: HealthCondition


class HealthReferenceRange(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    ageHigh: float
    ageLow: float
    allDay: bool
    category: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    fasting: bool
    gestationalAge: str
    high: float
    icalUid: str
    low: float
    method: str
    pregnancy: str
    properties: Any
    provenance: str
    recurrence: list[str]
    refText: str
    sex: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timeOfDay: str
    timezone: str
    unit: str
    visibility: str
    analyte: HealthBiomarker
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    issuingLab: HealthLab
    location: Place
    organizer: Person
    person: Person


class Icon(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    component: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    dimension: int
    format: str
    language: str
    license: str
    purpose: str
    style: str
    tags: list[str]
    contributors: list[Person]
    copyrightHolder: Person
    published_by: Actor
    written_by: Person


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
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    displayId: int
    displayIndex: int
    encoding: str
    filename: str
    format: str
    height: int
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    tags: list[str]
    width: int
    windowId: int
    attachedTo: Message
    contributors: list[Person]
    copyrightHolder: Person
    published_by: Actor
    repository: Repository
    written_by: Person


class IntellectualProperty(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    category: str
    filingBasis: str
    identifier: str
    mark: str
    niceClass: list[int]
    register: str
    renewalPeriod: str
    status: str
    validIn: str
    verificationUrl: str
    covers: CreativeWork
    granted_by: Organization
    held_by: Actor


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
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    email: str
    endDate: str
    icalUid: str
    invitationType: str
    message: str
    properties: Any
    recurrence: list[str]
    revokedAt: str
    role: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    token: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    invitee: Account
    inviter: Account
    involves: list[Person]
    location: Place
    organization: Organization
    organizer: Person
    person: Person


class Launch(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    articleUrl: str
    crewIds: list[str]
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    flightNumber: int
    icalUid: str
    landingOutcomes: Any
    launchpadId: str
    patchImage: str
    properties: Any
    recurrence: list[str]
    reusedBoosters: list[str]
    rocketId: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    webcastUrl: str
    wikipediaUrl: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person


class Leg(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrivalTime: str
    cabinClass: str
    carbonEmissions: Any
    currentUrl: str
    dateUpdated: str
    departureTime: str
    distinctId: str
    duration: str
    durationMinutes: int
    endDate: str
    flightNumber: str
    icalUid: str
    layoverMinutes: int
    polyline: str
    properties: Any
    recurrence: list[str]
    sequence: int
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    trace: Any
    tracePointCount: int
    vehicleType: str
    visibility: str
    aircraft: Aircraft
    at: Actor
    attachments: list[File]
    carrier: Organization
    creator: Person
    destination: Place
    involves: list[Person]
    location: Place
    organizer: Person
    origin: Place
    person: Person
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
    default_view: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str
    at: Actor
    background_image: Image
    belongsTo: Account
    contains: list[Any]


class LoadedModel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    digest: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    quantization: str
    recurrence: list[str]
    showAs: str
    size: str
    sizeVram: int
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    vramUsage: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person


class McpSession(TypedDict, total=False):
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
    folder: List
    participant: Actor


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
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    isVirtual: bool
    meetingType: str
    meetingUrl: str
    phoneDialIn: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person
    transcribe: Transcript


class Membership(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    autoRenew: bool
    billingType: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    guestPassQuantity: int
    icalUid: str
    price: float
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    tier: str
    timezone: str
    useCount: int
    visibility: str
    account: Account
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    member: Person
    organizer: Person
    person: Person
    plan: Product


class Memex(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    description: str
    distinctId: str
    edgeCount: int
    endDate: str
    filePath: str
    fileSize: str
    icalUid: str
    nodeCount: int
    origin: str
    properties: Any
    published: bool
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    forkedFrom: Memex
    involves: list[Person]
    location: Place
    organizer: Person
    owner: Person
    person: Person
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
    conversationId: str
    isOutgoing: bool
    isStarred: bool
    at: Actor
    from_: Actor  # from
    inConversation: Conversation
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
    quantization: str
    quantizationLevel: str
    size: str
    at: Actor


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
    allDay: bool
    availability: str
    bookingToken: str
    currency: str
    currentUrl: str
    dateUpdated: str
    departureToken: str
    distinctId: str
    endDate: str
    icalUid: str
    offerType: str
    price: float
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    for_: Product  # for
    involves: list[Person]
    location: Place
    offeredBy: Organization
    organizer: Person
    person: Person
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
    allDay: bool
    body: str
    currency: str
    currentUrl: str
    dateUpdated: str
    deliveryDate: str
    deliveryFee: float
    deliveryInstructions: str
    distinctId: str
    endDate: str
    eta: str
    fareBreakdown: Any
    head: str
    icalUid: str
    interactionType: str
    itemStates: Any
    latestArrival: str
    messages: Any
    orderDate: str
    orderId: str
    orderUuid: str
    originalTotal: str
    originalTotalAmount: float
    progress: float
    progressTotal: float
    properties: Any
    recurrence: list[str]
    savings: float
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    subtotal: float
    summary: str
    taxes: float
    timeline: Any
    timezone: str
    tipAmount: float
    total: str
    totalAmount: float
    visibility: str
    at: Actor
    attachments: list[File]
    contains: list[Product]
    creator: Person
    delivery: Trip
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person
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
    industry: str
    domain: Domain
    headquarters: Place
    member: list[Person]
    parentOrganization: Organization
    website: Website


class Pass(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    boardingGroup: str
    checkinStatus: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    gate: str
    icalUid: str
    isAllDayPass: bool
    nameOnTicket: str
    price: float
    properties: Any
    purchasedQuantity: int
    quantity: int
    recurrence: list[str]
    seatAssignment: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    terminal: str
    ticketClass: str
    ticketNumber: str
    timezone: str
    useCount: int
    visibility: str
    account: Account
    at: Actor
    attachments: list[File]
    creator: Person
    for_: Leg  # for
    grantedBy: Membership
    holder: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person
    reservation: Reservation
    type: Product


class PaymentMethod(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    balance: float
    binRange: str
    brand: str
    currency: str
    customDescription: str
    displayName: str
    expMonth: int
    expYear: int
    expirationDate: str
    fingerprint: str
    holderName: str
    identifier: str
    isDefault: bool
    isExpired: bool
    isPrimary: bool
    isSelected: bool
    last4: str
    metadata: Any
    providerTokens: Any
    status: str
    subtype: str
    type: str
    account: Account
    at: Actor
    billingAddress: Place
    fundingAccount: FinancialAccount
    holder: Person
    issuer: Actor
    membership: Membership


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
    additionalName: str
    familyName: str
    gender: str
    givenName: str
    honorificPrefix: str
    honorificSuffix: str
    legalName: str
    maidenName: str
    nameOrder: str
    nickname: str
    notes: str
    phoneticFamilyName: str
    phoneticGivenName: str
    preferredName: str
    sortAs: str
    accounts: list[Account]
    memberships: list[Membership]
    passes: list[Pass]
    practices: list[Practice]
    qualifications: list[Qualification]
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
    closedMessage: str
    country: str
    countryCode: str
    district: str
    eta: str
    featureType: str
    fullAddress: str
    googlePlaceId: str
    hours: Any
    isOrderable: bool
    latitude: float
    locality: str
    longitude: float
    mapboxId: str
    neighborhood: str
    phone: str
    placeFormatted: str
    postalCode: str
    priceLevel: str
    productCount: int
    rating: float
    region: str
    reviewCount: int
    street: str
    streetNumber: str
    timezone: str
    website: str
    wikidataId: str
    at: Actor
    brand: Organization
    offers: list[Product]


class Playlist(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    default_view: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str
    at: Actor
    background_image: Image
    belongsTo: Account
    contains: list[Video]


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
    at: Actor
    episode: list[Episode]
    host: list[Person]


class Post(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    commentCount: int
    community: str
    externalUrl: str
    postType: str
    score: int
    at: Actor
    attachment: list[File]
    contains: list[Video]
    media: list[Image]
    postedBy: Account
    publish: Community
    replies: list[Post]
    repliesTo: Post


class Practice(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aliases: list[str]
    code: str
    codeSystem: str
    description: str
    parent: Practice


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
    category: str
    currency: str
    customizationGroups: Any
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
    creator: list[Actor]
    inspiredBy: list[Product]
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
    parentId: str
    state: str
    at: Actor


class Protocol(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    homepage: str
    rfc: str
    wikidataId: str


class Qualification(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    category: str
    identifier: str
    level: str
    renewalPeriod: str
    status: str
    validIn: str
    verificationUrl: str
    field: Practice
    governed_by: Organization
    granted_by: Organization
    held_by: Person


class QuantityKind(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    key: str
    label: str
    dimension: Dimension
    parent: QuantityKind


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


class Reservation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    availableActions: list[str]
    baseAmount: float
    bookingTime: str
    bookingType: str
    checkinUrl: str
    conditions: Any
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    endTime: str
    icalUid: str
    modifiedTime: str
    partySize: int
    properties: Any
    recurrence: list[str]
    reservationId: str
    reservationType: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    startTime: str
    status: str
    taxAmount: float
    timezone: str
    totalAmount: float
    visibility: str
    voidWindowEndsAt: str
    account: Account
    at: Actor
    attachments: list[File]
    broker: Actor
    creator: Person
    derivedFrom: Offer
    event: Event
    involves: list[Person]
    location: Place
    order: Order
    organizer: Person
    passengers: list[Person]
    person: Person
    programMembership: Membership
    tickets: list[Pass]
    trips: list[Trip]
    underName: Person


class Result(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    community: str
    externalUrl: str
    indexedAt: str
    postId: str
    resultType: str
    score: int
    similarity: float


class Review(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    commentCount: int
    community: str
    externalUrl: str
    isVerified: bool
    postType: str
    rating: float
    ratingMax: float
    score: int
    tags: list[str]
    at: Actor
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
    allDay: bool
    currentUrl: str
    dateUpdated: str
    department: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    recurrence: list[str]
    roleType: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    title: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organization: Organization
    organizer: Person
    person: Person


class Seatmap(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aircraftCode: str
    availableSeats: int
    basicEconomyLocked: bool
    cabins: Any
    classOfService: str
    destination: str
    fareBasisCode: str
    flightNumber: str
    hasExitRow: bool
    hasFreeSeats: bool
    hasPaidSeats: bool
    origin: str
    tiers: Any
    totalSeats: int
    aircraft: Aircraft
    at: Actor
    flight: Flight
    reservation: Reservation


class Shelf(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    default_view: str
    icon_size: int
    isDefault: bool
    isExclusive: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str
    at: Actor
    background_image: Image
    belongsTo: Account
    contains: list[Book]


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
    applicationCategory: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    category: str
    codename: str
    currency: str
    customizationGroups: Any
    department: str
    images: Any
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    runtimePlatform: str
    servingSize: str
    sku: str
    soldByWeight: bool
    version: str
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    creator: list[Actor]
    inspiredBy: list[Product]
    manufacturer: Organization
    tagged: list[Tag]


class Sound(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    bitDepth: int
    channels: int
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    durationMs: int
    encoding: str
    filename: str
    format: str
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    purpose: str
    sampleRate: int
    sha: str
    size: int
    tags: list[str]
    attachedTo: Message
    contributors: list[Person]
    copyrightHolder: Person
    published_by: Actor
    repository: Repository
    written_by: Person


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
    scanner: str
    sourceId: str
    folder: List


class Spec(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    encoding: str
    endDate: str
    filename: str
    format: str
    icalUid: str
    kind: str
    labels: list[str]
    lineCount: int
    mimeType: str
    parentId: str
    path: str
    priority: int
    problem: str
    projectId: str
    properties: Any
    recurrence: list[str]
    remoteId: str
    sha: str
    showAs: str
    size: int
    sourceTitle: str
    sourceUrl: str
    startDate: str
    state: str
    status: str
    successCriteria: str
    target: Any
    targetDate: str
    timezone: str
    visibility: str
    assignedTo: Person
    at: Actor
    attachedTo: Message
    attachments: list[File]
    blockedBy: list[Task]
    blocks: list[Task]
    children: list[Task]
    creator: Person
    dependsOn: list[Spec]
    involves: list[Person]
    location: Place
    organizer: Person
    parent: Task
    person: Person
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
    annotated: bool
    color: str
    hash: str
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
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    labels: list[str]
    parentId: str
    priority: int
    projectId: str
    properties: Any
    recurrence: list[str]
    remoteId: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    state: str
    status: str
    target: Any
    targetDate: str
    timezone: str
    visibility: str
    assignedTo: Person
    at: Actor
    attachments: list[File]
    blockedBy: list[Task]
    blocks: list[Task]
    children: list[Task]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    parent: Task
    person: Person
    project: Project
    repository: Repository


class TaxLine(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    amount: float
    appliesToIndex: int
    code: str
    country: str
    currency: str
    description: str
    inclusive: bool
    kind: str
    merchantImposed: bool
    nature: str
    rate: float
    refundable: bool
    taxableAmount: float
    appliesTo: Fare
    at: Actor
    imposedBy: Actor
    location: Place
    offer: Offer
    reservation: Reservation
    segment: Leg


class Theme(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    defaultBackgroundColor: str
    description: str
    family: str
    startMenu: str
    style: str
    themeId: str
    represents: Product


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
    allDay: bool
    amount: float
    balance: float
    category: str
    currency: str
    currentUrl: str
    dateUpdated: str
    details: Any
    distinctId: str
    endDate: str
    icalUid: str
    notes: str
    pending: bool
    postingDate: str
    properties: Any
    recurrence: list[str]
    recurring: bool
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    type: str
    visibility: str
    account: FinancialAccount
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person


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


class Transition(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    additionalName: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    familyName: str
    gender: str
    givenName: str
    honorificPrefix: str
    honorificSuffix: str
    icalUid: str
    legalName: str
    maidenName: str
    nameOrder: str
    nickname: str
    phoneticFamilyName: str
    phoneticGivenName: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sortAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    person: Person


class Trip(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrivalTime: str
    bookingToken: str
    cabinClass: str
    carbonEmissions: Any
    currency: str
    currentUrl: str
    dateUpdated: str
    departureTime: str
    distance: str
    distinctId: str
    duration: str
    durationMinutes: int
    endDate: str
    fare: str
    fareAmount: float
    guest: Any
    icalUid: str
    isPool: bool
    isReserve: bool
    isScheduled: bool
    isSurge: bool
    marketplace: str
    properties: Any
    rating: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    stops: int
    timezone: str
    trackingUrl: str
    tripType: str
    vehicle: Any
    vehicleType: str
    visibility: str
    at: Actor
    attachments: list[File]
    carrier: Organization
    creator: Person
    destination: Place
    driver: Person
    involves: list[Person]
    legs: list[Leg]
    location: Place
    order: Order
    organizer: Person
    origin: Place
    person: Person


class Unit(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    iso4217: str
    iso4217Numeric: str
    kind: str
    label: str
    logBase: float
    minorExponent: int
    qudtUnitIri: str
    siDigitalFrameworkUri: str
    symbol: str
    toBaseFactor: float
    toBaseOffset: float
    ucumCode: str
    unCefactCommonCode: str
    wikidataId: str
    dimension: Dimension
    quantityKinds: list[QuantityKind]


class User(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    osUsername: str
    primaryUser: bool
    identified_as: Person


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
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    durationMs: int
    encoding: str
    filename: str
    format: str
    frameRate: float
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    resolution: str
    sha: str
    size: int
    tags: list[str]
    viewCount: int
    addTo: Playlist
    attachedTo: Message
    channel: Channel
    contributors: list[Person]
    copyrightHolder: Person
    published_by: Actor
    repository: Repository
    transcribe: Transcript
    written_by: Person


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
    status: str
    versionId: str
    domain: Domain
    ownedBy: Organization


# Raw YAML bodies — consumed by the skill worker to attach
# `__shape_yaml__` on every @returns(shape) response.
SHAPE_YAMLS: dict[str, str] = {
    'account': 'plural: accounts\nidentity:\n- at\n- identifier\ndisplay:\n  subtitle: identifier\nfields:\n  identifier: string\n  handle: string\n  displayName: string\n  display: string\n  email: string\n  phone: string\n  bio: text\n  accountType: string\n  color: string\n  isActive: boolean\n  joinedDate: datetime\n  lastActive: datetime\n  lastProfileFetch: datetime\n  userId: string\n  issuer: string\n  metadata: json\nrelations:\n  at: actor\n  via: product\n  operator: actor\n  protocol: protocol\n  owner: person\n  authenticatedVia: account\n  previousIdentity: account[]\n  follows: account[]\n  followers: account[]\nprior_art:\n- source: ActivityPub Actor model\n  url: https://www.w3.org/TR/activitypub/\n  notes: Account id is a URL; Server/Application/Operator are separate Actor objects.\n    We adopt the same separation but ground each in graph nodes rather than URLs,\n    so node lifecycle (rebrand, merge) propagates to all referencing accounts.\n- source: schema.org Offer.seller union\n  url: https://schema.org/Offer\n  notes: "seller: Person | Organization. The `actor` shape (which `at` and `operator`\\\n    \\ target) is our existing union of person/org/agent \\u2014 same pattern."\n- source: OpenID Connect Core 1.0 (`iss`/`sub`)\n  url: https://openid.net/specs/openid-connect-core-1_0.html\n  notes: OIDC keeps issuer as opaque URL because there\'s no shared graph across token\n    issuers. We have a graph; we replace the URL with a graph node, gaining mutability\n    and traversal at the cost of requiring a node to exist before an account can reference\n    it. Trade is worth it.\n- source: WebFinger (RFC 7033)\n  url: https://datatracker.ietf.org/doc/html/rfc7033\n  notes: \'Resolves issuer+identifier pairs to profile metadata. Our identifier aligns\n    with WebFinger\'\'s acct: URI scheme (user@host), but the `host` part becomes a\n    graph node (not a string).\'\n- source: vCard 4.0 (RFC 6350)\n  url: https://datatracker.ietf.org/doc/html/rfc6350\n  notes: Defines displayName/email/phone/org in contact cards. We adopt vCard\'s contact\n    semantics for the human-readable fields.\n',
    'activity': 'plural: activities\nalso:\n- event\ndisplay:\n  subtitle: action\nicon: activity\nfields:\n  action: string\n  changedKeys: string[]\n  toolName: string\n  duration: number\n  success: boolean\nrelations:\n  session: mcp_session\n  folder: list\nprior_art:\n- source: ActivityStreams 2.0\n  url: https://www.w3.org/TR/activitystreams-core/\n  notes: AS2\'s Create/Update/Delete activities match our action values. We diverge\n    by tracking changedKeys explicitly instead of encoding full object replacement.\n- source: OpenTelemetry Traces\n  url: https://opentelemetry.io/docs/concepts/signals/traces/\n  notes: "Closest fit for toolName/duration/success \\u2014 span-shaped. Our activity\\\n    \\ is closer to a span event than a full span."\n',
    'actor': 'plural: actors\ndisplay:\n  subtitle: actorType\nfields:\n  actorType: string\nprior_art:\n- source: FOAF Agent\n  url: http://xmlns.com/foaf/spec/#term_Agent\n  notes: FOAF Agent is the base class for Person, Organization, and Group. Our actorType\n    mirrors FOAF\'s agent taxonomy.\n- source: ActivityStreams 2.0 Actor\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#actor-types\n  notes: "AS2 defines Actor types (Person, Organization, Group, Service, Application).\\\n    \\ Our agent \\u2248 Service/Application."\n',
    'agent': "plural: agents\ndisplay:\n  subtitle: model\nalso:\n- actor\nfields:\n  model: string\n  provider: string\n  sessionId: string\nprior_art:\n- source: ActivityStreams 2.0 Service\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-service\n  notes: AS2's Service Actor is the closest peer for an automated agent. We add model/provider/sessionId\n    for AI-specific lineage.\n- source: Anthropic Tool Use API (Claude)\n  url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use\n  notes: Mirrors our model/provider fields. sessionId groups related tool invocations\n    from a single agent run.\n",
    'aircraft': 'plural: aircraft\nidentity: icaoCode\ndisplay:\n  subtitle: model\nalso:\n- product\nfields:\n  model: string\n  variant: string\n  seatCapacity: integer\n  rangeKm: integer\n  iataCode: string\n  icaoCode: string\nrelations:\n  manufacturer: organization\nprior_art:\n- source: ICAO Aircraft Type Designators (Doc 8643)\n  url: https://www.icao.int/publications/DOC8643/Pages/Search.aspx\n  notes: Our icaoCode is the canonical 4-char type code (B738, A320); iataCode is\n    the 3-char IATA equivalent (738, 320).\n- source: schema.org/Vehicle\n  url: https://schema.org/Vehicle\n  notes: Our model/seatCapacity map to vehicleModelDate/vehicleSeatingCapacity; manufacturer\n    matches directly.\n',
    'airline': "plural: airlines\nidentity: iataCode\ndisplay:\n  subtitle: iataCode\nalso:\n- organization\nfields:\n  iataCode: string\n  icaoCode: string\n  callsign: string\n  country: string\n  alliance: string\nprior_art:\n- source: IATA Airline Designators\n  url: https://www.iata.org/en/publications/directories/code-search/\n  notes: iataCode is 2-letter (UA, DL); icaoCode is 3-letter (UAL, DAL); callsign\n    is radio callsign (UNITED). Full IATA/ICAO alignment.\n- source: schema.org/Airline\n  url: https://schema.org/Airline\n  notes: schema.org's Airline is an Organization subtype. Our alliance is a free field;\n    schema.org doesn't model it.\n",
    'airport': 'plural: airports\nidentity: iataCode\ndisplay:\n  subtitle: iataCode\nfields:\n  iataCode: string\n  icaoCode: string\n  city: string\n  country: string\n  countryCode: string\n  timezone: string\n  elevationFt: integer\n  terminalCount: integer\nrelations:\n  location: place\n  operator: organization\nprior_art:\n- source: IATA/ICAO Airport Codes\n  url: https://www.iata.org/en/publications/directories/code-search/\n  notes: iataCode is 3-letter (LAX, JFK); icaoCode is 4-letter (KLAX, KJFK). Canonical\n    identifiers for global airport routing.\n- source: schema.org/Airport\n  url: https://schema.org/Airport\n  notes: "Our iataCode/icaoCode = iataCode/icaoCode; city/country = address fields;\\\n    \\ elevationFt \\u2248 elevation. Direct alignment."\n- source: OurAirports open dataset\n  url: https://ourairports.com/data/\n  notes: Practical open dataset covering terminalCount, elevation, and country codes\n    (ISO 3166-1) aligning with our countryCode field.\n',
    'app': 'plural: apps\nidentity:\n- id\ndisplay:\n  subtitle: name\nfields:\n  id: string\n  name: string\n  iconRole: string\n  route: string\n  defaultView: string\n  isSystem: boolean\n  handles: string[]\nprior_art:\n- source: macOS .app bundle (Info.plist)\n  url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html\n  notes: "CFBundleIdentifier \\u2248 id; CFBundleName \\u2248 name; CFBundleIconFile\\\n    \\ \\u2248 iconRole (we use a role rather than a file path so themes can override)."\n- source: freedesktop .desktop entry\n  url: https://specifications.freedesktop.org/desktop-entry-spec/latest/\n  notes: "Name, Icon, Exec \\u2014 the Linux/XDG peer. We model the launchable surface,\\\n    \\ not the executable (the engine knows how to spawn)."\n- source: Windows AppUserModelID\n  url: https://learn.microsoft.com/en-us/windows/win32/shell/appids\n  notes: "Stable per-app identity decoupled from the executable on disk. Our `id`\\\n    \\ plays the same role \\u2014 themes and bookmarks reference it, the binary is\\\n    \\ an implementation detail of seed_system_apps()."\n',
    'birth': 'plural: births\nalso:\n- event\ndisplay:\n  subtitle: location\n  highlights:\n  - startDate\n  - location\nfields:\n  givenName: string\n  additionalName: string\n  familyName: string\n  honorificPrefix: string\n  honorificSuffix: string\n  legalName: string\n  maidenName: string\n  sortAs: string\n  nameOrder: string\n  phoneticGivenName: string\n  phoneticFamilyName: string\n  gender: string\n  nickname: string\nprior_art:\n- source: schema.org/Person.birthDate / birthPlace\n  url: https://schema.org/birthDate\n  notes: schema.org collapses birth into two flat fields on Person; we lift to an\n    event-node so all birth particulars (name, gender, legal-doc form) co-locate per\n    platform README rule 1.\n- source: GEDCOM 7 INDI.BIRT\n  url: https://gedcom.io/specifications/FamilySearchGEDCOMv7.html\n  notes: "Genealogy\'s canonical model: a typed INDIVIDUAL_EVENT with DATE, PLAC, ADDR\\\n    \\ sub-records. Our `birth` shape is the equivalent \\u2014 sub-records map to event-base\\\n    \\ fields (startDate, location) plus the typed birth-particulars fields above."\n- source: GEDCOM-X Fact (FactType=Birth)\n  url: https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md\n  notes: FamilySearch\'s reified-fact model. We adopt the reified-event pattern; field\n    set is richer (legalName + phonetics + nameOrder) for present-day identity-document\n    interop.\n',
    'book': 'plural: books\nidentity_any:\n- isbn13\n- isbn\ndisplay:\n  subtitle: written_by\nalso:\n- creative_work\n- product\nfields:\n  isbn: string\n  isbn13: string\n  pages: integer\n  genres: string[]\n  series: string\n  format: string\n  language: string\n  originalTitle: string\n  places: string[]\n  characters: string[]\n  awardsWon: string[]\nrelations:\n  contributors: person[]\nprior_art:\n- source: schema.org/Book\n  url: https://schema.org/Book\n  notes: "Our isbn maps to isbn; writtenBy = author; publisher matches; pages = numberOfPages;\\\n    \\ language = inLanguage; format \\u2248 bookFormat (Hardcover/Paperback/EBook)."\n- source: ONIX for Books 3.0\n  url: https://www.editeur.org/83/Overview/\n  notes: Publishing-industry canonical. Our isbn/isbn13/pages/format/language/series/originalTitle\n    align with ONIX Product Identifier, Extent, ProductForm, Language, Collection,\n    and OriginalLanguageTitle composites.\n- source: Open Library Books API\n  url: https://openlibrary.org/developers/api\n  notes: Practical lookup by ISBN. Our genres/characters/places/awardsWon map to subjects/subject_people/subject_places/subject_times\n    (awards less standardized).\n',
    'booking_offer': 'plural: booking_offers\nidentity:\n- at\n- cartId\nalso:\n- event\ndisplay:\n  subtitle: totalAmount\nfields:\n  cartId: string\n  referenceNumber: string\n  status: string\n  preparedAt: datetime\n  presentedAt: datetime\n  approvedAt: datetime\n  expiresAt: datetime\n  currency: string\n  baseAmount: number\n  taxAmount: number\n  feesAmount: number\n  totalAmount: number\n  itineraryHash: string\n  signature: string\n  signatureAlg: string\n  signedBy: string\n  checkoutUrl: url\n  confirmEndpoint: url\n  isRefundable: boolean\n  isChangeable: boolean\n  hasVoidWindow: boolean\n  voidWindowEndsAt: datetime\n  conditions: json\n  blob: string\n  review: string\n  contactEmail: string\n  contactPhone: string\nrelations:\n  at: actor\n  derivedFrom: offer\n  trips: trip[]\n  reservedItems: pass[]\n  buyers: person[]\n  guests: person[]\n  underName: person\n  paymentMethod: payment_method\n  billingAddress: place\n  fares: fare[]\n  taxLines: tax_line[]\n  account: account\n  membership: membership\n  broker: actor\n  becameReservation: reservation\n  becameTransaction: transaction\nprior_art:\n- source: Duffel Offers API (pre-Order priced shape)\n  url: https://duffel.com/docs/api/offers/schema\n  notes: "Duffel\'s Offer is the \\"priced, held, about-to-become-an-order\\" state.\\\n    \\ Our baseAmount/taxAmount/totalAmount/currency map to Duffel\'s base_amount/tax_amount/total_amount/total_currency;\\\n    \\ expiresAt = offer.expires_at. Duffel rolls taxes into a single aggregate \\u2014\\\n    \\ we split them into tax_line[] nodes."\n- source: IATA NDC OfferPriceRQ / OfferPriceRS\n  url: https://developer.iata.org/en/ndc/\n  notes: NDC\'s OfferPrice is the mandatory "price this exact shape with these exact\n    passengers" step between Shop and OrderCreate. Our guests[] mirror NDC\'s PaxList;\n    taxLines[] mirror Taxes/ TaxSummary; signature mirrors OfferPriceRS\'s ShoppingResponseID\n    that the airline expects back on OrderCreateRQ.\n- source: Stripe Checkout Session\n  url: https://docs.stripe.com/api/checkout/sessions/object\n  notes: "Canonical \\"about-to-charge\\" object. Our cartId \\u2248 session.id; expiresAt\\\n    \\ \\u2248 session.expires_at; totalAmount \\u2248 session.amount_total; paymentMethod\\\n    \\ relation mirrors session.payment_method. Stripe assumes line_item shape; we\\\n    \\ use domain-specific relations (trips/reservedItems) instead."\n- source: Shopify Draft Order\n  url: https://shopify.dev/docs/api/admin-graphql/latest/objects/DraftOrder\n  notes: "Shopify\'s non-binding pre-order \\u2014 validates the \\"cart with a reference\\\n    \\ number that can be invoiced and converted\\" pattern. Our referenceNumber \\u2248\\\n    \\ DraftOrder.name; becameReservation / becameTransaction mirror DraftOrder ->\\\n    \\ Order conversion."\n- source: WebAuthn clientDataJSON + signed assertion\n  url: https://www.w3.org/TR/webauthn-3/\n  notes: "Precedent for \\"the thing the user saw is what got signed.\\" WebAuthn signs\\\n    \\ (challenge, origin, type); we sign (cartId, itineraryHash, total, expiresAt).\\\n    \\ Our itineraryHash plays the role of WebAuthn\'s challenge \\u2014 a commitment\\\n    \\ the verifier can match against the submitted shape."\n- source: CoinGate Invoice (short-TTL priced blob)\n  url: https://developer.coingate.com/reference/order-statuses\n  notes: "Validates the short-TTL pattern outside airlines. CoinGate invoices carry\\\n    \\ id, price locked ~20 min, and status (new, pending, paid, expired, canceled).\\\n    \\ Our status enum matches \\u2014 pre-commit objects need expiry as a first-class\\\n    \\ terminal."\n- source: schema.org/Order + schema.org/Invoice\n  url: https://schema.org/Order\n  notes: "schema.org models Offer -> Order -> Invoice. booking_offer sits between\\\n    \\ Offer and Order \\u2014 a priced, itemized, signed proposal awaiting explicit\\\n    \\ human commit. Our baseAmount + taxAmount + totalAmount align with UBL 2.1 LegalMonetaryTotal."\n',
    'bookmark': 'plural: bookmarks\nidentity:\n- target\ndisplay:\n  subtitle: name\nicon: "\\U0001F516"\nfields:\n  name: string\nrelations:\n  target: node\nprior_art:\n- source: Browser bookmarks (Mosaic / Netscape Navigator hotlist)\n  url: https://en.wikipedia.org/wiki/Bookmark_(digital)\n  notes: Direct precedent. A bookmark is a name + a target; the target is the contract;\n    the surface doesn\'t care what\'s behind it. We replace HTTP URLs with graph node\n    references; everything else maps 1:1.\n- source: macOS alias / Windows .lnk file\n  url: https://en.wikipedia.org/wiki/Alias_(Mac_OS)\n  notes: "OS-level shortcut primitive. Same shape: name + target. Per- instance position\\\n    \\ is handled by the parent folder/desktop in both \\u2014 for us that lives on\\\n    \\ the contains-edge."\n- source: Finder sidebar / Windows Explorer Quick Access\n  url: https://support.apple.com/guide/mac-help/customize-the-finder-sidebar-mchlp3014/mac\n  notes: "OS file managers use a bookmark sidebar as their universal navigation primitive\\\n    \\ (My Computer, Documents, Network). We treat every shape the same way \\u2014\\\n    \\ bookmark to any graph node, no FS bias."\n',
    'branch': 'plural: branches\ndisplay:\n  subtitle: commit\nfields:\n  commit: string\n  upstream: string\n  ahead: integer\n  behind: integer\n  isCurrent: boolean\n  isRemote: boolean\nrelations:\n  repository: repository\nprior_art:\n- source: "Git Internals \\u2014 Branches"\n  url: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell\n  notes: A branch is a movable pointer to a commit. Our commit field is the HEAD sha;\n    ahead/behind mirror `git rev-list --count`.\n- source: "GitHub REST \\u2014 branches"\n  url: https://docs.github.com/en/rest/branches/branches\n  notes: "Practical API surface. Our upstream \\u2248 the remote tracking ref; we flatten\\\n    \\ protection/commit metadata that GitHub nests."\n',
    'brand': 'plural: brands\nidentity: url\ndisplay:\n  subtitle: tagline\nfields:\n  tagline: string\n  country: string\n  primaryColor: string\n  textColor: string\nrelations:\n  ownedBy: organization\n  website: website\n  logo: image\nprior_art:\n- source: schema.org/Brand\n  url: https://schema.org/Brand\n  notes: "Our tagline \\u2248 slogan; founded = foundingDate; ownedBy \\u2248 parentOrganization\\\n    \\ (on the owning Organization); logo = logo. schema.org doesn\'t model color on\\\n    \\ Brand; that\'s a Wikidata extension."\n- source: Wikidata (Brand, Q431289)\n  url: https://www.wikidata.org/wiki/Q431289\n  notes: "Cross-reference identity for dedupe. country maps to P17 (country); founded\\\n    \\ to P571 (inception); ownedBy to P127 (owned by); primaryColor \\u2248 P465 \\"\\\n    hex color code\\" (Wikidata stores without the \\"#\\" prefix \\u2014 we include it\\\n    \\ to match CSS and our skill-frontmatter convention)."\n- source: Apple PassKit pkpass\n  url: https://developer.apple.com/documentation/walletpasses\n  notes: "Wallet passes carry backgroundColor / foregroundColor / labelColor \\u2014\\\n    \\ three-color palette aligned with our primaryColor / textColor. We ship two here\\\n    \\ (pairing primary with its paired text color) and defer the third until a renderer\\\n    \\ needs it. An itinerary PDF can derive a \\"label\\" color from a lighter tint\\\n    \\ of textColor at render time if needed, rather than fixing it at the data layer."\n- source: "Material Design 3 \\u2014 dynamic color roles"\n  url: https://m3.material.io/styles/color/roles\n  notes: Material\'s palette has paired slots (`primary` / `onPrimary`; `secondary`\n    / `onSecondary`; `surface` / `onSurface`). Our primaryColor/textColor follows\n    the primary/onPrimary pairing. Secondary tiers are deferred until renderers actually\n    need them.\n',
    'calendar': 'plural: calendars\nidentity:\n- at\n- calendarId\ndisplay:\n  subtitle: source\nfields:\n  calendarId: string\n  color: string\n  backgroundColor: string\n  foregroundColor: string\n  isPrimary: boolean\n  isReadonly: boolean\n  accessRole: string\n  source: string\n  timezone: string\nrelations:\n  at: actor\n  owner: person\n  events: event[]\nprior_art:\n- source: RFC 5545 VCALENDAR\n  url: https://datatracker.ietf.org/doc/html/rfc5545\n  notes: "Our calendarId \\u2248 VCALENDAR\'s X-WR-CALID; timezone = X-WR-TIMEZONE;\\\n    \\ events relation mirrors VCALENDAR\'s VEVENT components."\n- source: CalDAV (RFC 4791)\n  url: https://datatracker.ietf.org/doc/html/rfc4791\n  notes: CalDAV calendar collections define accessRole semantics (owner/writer/reader)\n    that match our field directly.\n- source: Google Calendar API CalendarList\n  url: https://developers.google.com/calendar/api/v3/reference/calendarList\n  notes: Practical API mirror. Our color/backgroundColor/foregroundColor, isPrimary,\n    accessRole come from Google\'s CalendarList resource.\n',
    'channel': 'plural: channels\ndisplay:\n  subtitle: subscriberCount\nidentity:\n- at\n- id\nfields:\n  banner: url\n  subscriberCount: integer\nrelations:\n  at: actor\nprior_art:\n- source: ActivityStreams 2.0 Collection\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection\n  notes: A channel is a platform-specific Collection of media items. Our banner is\n    channel branding; AS2 doesn\'t model that directly.\n- source: "YouTube Data API \\u2014 Channel resource"\n  url: https://developers.google.com/youtube/v3/docs/channels\n  notes: Practical source. Our channel id/banner map to YouTube\'s channelId and brandingSettings.image.bannerExternalUrl.\n- source: RSS 2.0 <channel>\n  url: https://www.rssboard.org/rss-specification\n  notes: "Original \\"channel\\" concept \\u2014 a grouped feed with title, image, and\\\n    \\ items. Our channel is the same pattern for video."\n',
    'class': 'plural: classes\ndisplay:\n  subtitle: activityType\nalso:\n- event\nfields:\n  activityType: string\n  capacity: integer\n  spotsRemaining: integer\n  isFull: boolean\nrelations:\n  instructor: person\n  venue: place\nprior_art:\n- source: schema.org/EducationEvent\n  url: https://schema.org/EducationEvent\n  notes: "schema.org\'s closest peer for a bookable class. Our instructor = performer;\\\n    \\ capacity = maximumAttendeeCapacity; spotsRemaining \\u2248 remainingAttendeeCapacity."\n- source: schema.org/ExerciseAction\n  url: https://schema.org/ExerciseAction\n  notes: "Fitness-specific vocabulary: activityType \\u2248 exerciseType; venue matches\\\n    \\ directly as location."\n- source: Mindbody Public API (class schedules)\n  url: https://developers.mindbodyonline.com/PublicDocumentation/V6\n  notes: Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody\'s\n    MaxCapacity/TotalBooked/IsWaitlistAvailable.\n',
    'community': 'plural: communities\nidentity:\n- at\n- id\ndisplay:\n  subtitle: text\nfields:\n  privacy: string\n  memberCount: integer\n  subscriberCount: integer\n  allowCrypto: boolean\nrelations:\n  at: actor\nprior_art:\n- source: ActivityPub Group Actor\n  url: https://www.w3.org/TR/activitypub/\n  notes: "AP Group Actor models shared-inbox communities (Lemmy, Kbin, Mbin). Our\\\n    \\ privacy \\u2248 audience/to visibility."\n- source: schema.org/Organization\n  url: https://schema.org/Organization\n  notes: A community-as-organization is a loose fit; privacy has no direct schema.org\n    property.\n- source: "Reddit API \\u2014 Subreddit"\n  url: https://www.reddit.com/dev/api/#GET_subreddits_where\n  notes: "Practical source. Our privacy \\u2248 subreddit_type (public/private/ restricted);\\\n    \\ text \\u2248 public_description."\n',
    'conversation': 'plural: conversations\nidentity:\n- at\n- id\ndisplay:\n  subtitle: text\nfields:\n  isGroup: boolean\n  isArchived: boolean\n  unreadCount: integer\n  messageCount: integer\n  accountEmail: string\n  historyId: string\n  source: string\n  cwd: string\n  gitBranch: string\nrelations:\n  at: actor\n  participant: actor[]\n  message: message[]\n  in: list\nprior_art:\n- source: ActivityStreams 2.0 context/inReplyTo\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context\n  notes: "Conversations are AS2 contexts \\u2014 the thread that groups replies. Our\\\n    \\ participant[] \\u2248 to/cc/audience."\n- source: Matrix Room (m.room)\n  url: https://spec.matrix.org/latest/client-server-api/#room-events\n  notes: "Practical thread model. Our isGroup \\u2248 room.join_rules; unreadCount\\\n    \\ \\u2248 unread_notifications.highlight_count."\n- source: "Gmail API \\u2014 Thread resource"\n  url: https://developers.google.com/gmail/api/reference/rest/v1/users.threads\n  notes: "Our messageCount \\u2248 messages.length; unreadCount derived from UNREAD\\\n    \\ labels on Thread messages."\n',
    'conversion': 'plural: conversions\nalso:\n- event\ndisplay:\n  subtitle: kind\nfields:\n  kind: string\n  factor: number\n  rate: number\nrelations:\n  from: unit\n  to: unit\n  parameter: node\nprior_art:\n- source: "NIH/NLM \\u2014 UCUM conversion service"\n  url: https://ucum.nlm.nih.gov/ucum-service.html\n  notes: "The NIH service requires a MOLWEIGHT parameter to convert between molar\\\n    \\ and mass concentration \\u2014 direct proof that the conversion is not intrinsic\\\n    \\ to the unit pair but depends on the substance."\n- source: "QUDT \\u2014 currency units carry no conversionMultiplier"\n  url: https://qudt.org/doc/2024/12/DOC_VOCAB-UNITS-CURRENCY.html\n  notes: "QUDT explicitly notes that FX rates are external data not encoded in QUDT\\\n    \\ \\u2014 the same reason fx conversions are their own node here rather than a\\\n    \\ property of the currency unit."\n- source: "ISO 4217 \\u2014 Currency codes"\n  url: https://www.iso.org/iso-4217-currency-codes.html\n  notes: Currency identity for the from/to units of an fx conversion.\n',
    'creative_work': 'plural: creative_works\ndisplay:\n  image: image\n  subtitle: written_by\n  highlights:\n  - datePublished\n  - published_by\n  body: description\nfields:\n  name: string\n  description: string\n  license: string\n  copyrightYear: integer\n  datePublished: date\n  dateCreated: date\n  url: string\n  language: string\n  coverage: string\n  tags: string[]\nrelations:\n  written_by: person\n  published_by: actor\n  contributors: person[]\n  copyrightHolder: person\nprior_art:\n- source: schema.org/CreativeWork\n  url: https://schema.org/CreativeWork\n  notes: "Our name=name; written_by\\u2248author; published_by\\u2248publisher; datePublished=datePublished;\\\n    \\ license=license; copyrightHolder= copyrightHolder; copyrightYear=copyrightYear;\\\n    \\ description= description; url=url; language=inLanguage; tags=keywords."\n- source: Dublin Core Metadata Element Set (ISO 15836)\n  url: https://www.dublincore.org/specifications/dublin-core/dces/\n  notes: Maps cleanly to all 15 DC elements except `type` (carried by the shape discriminator),\n    `format` (subtype-specific), `identifier` (universal node id), `relation` (graph\n    edges), `subject` (tags).\n- source: FRBR (IFLA, 1998)\n  url: https://www.ifla.org/files/assets/cataloguing/frbr/frbr.pdf\n  notes: creative_work corresponds to FRBR\'s Work tier (the abstract intellectual\n    creation). Expression / Manifestation / Item not modeled in v1; subtype shapes\n    carry equivalents as array fields (font.weights, font.formats).\n',
    'credential': 'plural: credentials\nidentity:\n- domain\n- identifier\n- itemType\ndisplay:\n  subtitle: source\nfields:\n  domain: string\n  identifier: string\n  itemType: string\n  source: string\n  obtainedAt: datetime\n  lastVerified: datetime\n  refreshable: boolean\n  storeRowId: integer\nrelations:\n  at: organization\n  account: account\n  writtenBy: skill\nprior_art:\n- source: OAuth 2.0 Token Introspection (RFC 7662)\n  url: https://datatracker.ietf.org/doc/html/rfc7662\n  notes: \'RFC 7662 describes token metadata as a separate addressable resource from\n    the token itself (active, exp, iss, sub, scope). Same split here: descriptor is\n    queryable graph metadata, encrypted value is retrieved by a separate call (`auth_store.read`\n    by identifier). Our obtainedAt/expiresAt/lastVerified mirror iat/exp/auth_time.\'\n- source: FIDO Metadata Service (MDS3)\n  url: https://fidoalliance.org/metadata/\n  notes: "FIDO separates authenticator metadata from the authenticator itself \\u2014\\\n    \\ metadata is queryable, the cryptographic material is not. Mirrors our descriptor/vault\\\n    \\ split."\n- source: macOS Keychain SecItem attributes\n  url: https://developer.apple.com/documentation/security/keychain_services/keychain_items/item_attribute_keys_and_values\n  notes: "Keychain separates `kSecAttr*` (metadata \\u2014 server, account, creation/modification\\\n    \\ dates) from `kSecValueData` (the secret). Attributes are queryable without decrypting\\\n    \\ the value. Our fields map: kSecAttrServer \\u2192 domain, kSecAttrAccount \\u2192\\\n    \\ identifier, kSecAttrCreationDate \\u2192 obtainedAt, kSecAttrModificationDate\\\n    \\ \\u2192 lastVerified."\n- source: schema.org/DigitalDocument (WebAuthn credentials stored as)\n  url: https://schema.org/DigitalDocument\n  notes: "Weak alignment \\u2014 schema.org has no native credential type. Cited only\\\n    \\ to note that existing web ontologies deliberately stop short of secret material;\\\n    \\ descriptor-only is the established pattern."\n',
    'dimension': 'plural: dimensions\nidentity:\n- key\ndisplay:\n  subtitle: label\nfields:\n  key: string\n  label: string\n  length: integer\n  mass: integer\n  time: integer\n  current: integer\n  temperature: integer\n  amount: integer\n  luminous: integer\n  dimensionless: boolean\nrelations:\n  baseUnit: unit\nprior_art:\n- source: "BIPM \\u2014 SI Brochure, 9th edition (2019)"\n  url: https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf\n  notes: "Defines the 7 base quantities (length, mass, time, electric current, thermodynamic\\\n    \\ temperature, amount of substance, luminous intensity) and their dimensions L,\\\n    \\ M, T, I, \\u0398, N, J. The seven exponent fields here are exactly those base\\\n    \\ dimensions."\n- source: "ISO 80000-1 \\u2014 Quantities and units, Part 1: General"\n  url: https://www.iso.org/standard/76921.html\n  notes: "The ISQ (International System of Quantities) \\u2014 the rigorous definition\\\n    \\ of a quantity dimension as a product of base-quantity powers. This shape is\\\n    \\ a direct encoding of an ISQ dimension."\n- source: "QUDT \\u2014 QuantityKindDimensionVector"\n  url: https://www.qudt.org/doc/DOC_SCHEMA-QUDT.html\n  notes: QUDT encodes the same 7 exponents as separate properties (qudt:dimensionExponentForMass\n    etc.) plus a compact vector IRI. Our `key` mirrors that compact form; the seven\n    integer fields mirror the per-dimension properties.\n',
    'dns_record': 'plural: dns_records\nidentity:\n- domain\n- recordType\n- recordName\ndisplay:\n  subtitle: recordType\nfields:\n  domain: string\n  recordName: string\n  recordType: string\n  type: string\n  ttl: integer\n  priority: integer\n  recordId: string\n  values: string[]\nprior_art:\n- source: RFC 1035 (DNS)\n  url: https://datatracker.ietf.org/doc/html/rfc1035\n  notes: Foundational spec. Our domain/recordName/recordType/ttl/values map directly\n    to NAME/TYPE/CLASS/TTL/RDATA.\n- source: RFC 7208 (SPF), RFC 6376 (DKIM), RFC 7489 (DMARC)\n  url: https://datatracker.ietf.org/doc/html/rfc7208\n  notes: TXT-record vocabularies that frequently populate our values[] for SPF, DKIM,\n    and DMARC policy records.\n',
    'document': 'plural: documents\ndisplay:\n  subtitle: contentType\n  highlights:\n  - datePublished\n  - author\n  - wordCount\n  body: abstract\nalso:\n- file\nfields:\n  contentType: string\n  language: string\n  wordCount: integer\n  abstract: text\n  tableOfContents: text\nrelations:\n  author: actor\n  references: document[]\n  citedBy: document[]\nprior_art:\n- source: Dublin Core Metadata Initiative\n  url: https://www.dublincore.org/specifications/dublin-core/dces/\n  notes: "Our contentType \\u2248 dc:format; language = dc:language; author = dc:creator;\\\n    \\ references/citedBy \\u2248 dc:relation."\n- source: schema.org/DigitalDocument\n  url: https://schema.org/DigitalDocument\n  notes: "Our abstract \\u2248 abstract; tableOfContents = hasPart or accessModeSufficient;\\\n    \\ wordCount = wordCount."\n- source: W3C Web Annotation Data Model\n  url: https://www.w3.org/TR/annotation-model/\n  notes: Our references[]/citedBy[] are annotation target/body relationships between\n    documents.\n',
    'domain': 'plural: domains\ndisplay:\n  subtitle: registrar\nidentity: name\nfields:\n  status: string\n  registrar: string\n  autoRenew: boolean\n  nameservers: string[]\nprior_art:\n- source: RFC 1035 (Domain Names)\n  url: https://datatracker.ietf.org/doc/html/rfc1035\n  notes: Canonical domain-name syntax + nameservers + TTL. Our nameservers are NS\n    records for the apex.\n- source: RFC 3912 (WHOIS)\n  url: https://datatracker.ietf.org/doc/html/rfc3912\n  notes: Our registrar/status/expiresAt/autoRenew come from WHOIS response fields.\n',
    'email': "plural: emails\nidentity:\n- at\n- id\ndisplay:\n  subtitle: author\nalso:\n- message\nfields:\n  subject: string\n  messageId: string\n  inReplyTo: string\n  isUnread: boolean\n  isStarred: boolean\n  isDraft: boolean\n  isSent: boolean\n  isTrash: boolean\n  isSpam: boolean\n  hasAttachments: boolean\n  draftId: string\n  conversationId: string\n  accountEmail: string\n  sizeEstimate: integer\n  references: string\n  replyTo: string\n  deliveredTo: string\n  attachments: json\n  toRaw: string\n  ccRaw: string\n  bccRaw: string\n  unsubscribe: string\n  unsubscribeOneClick: boolean\n  manageSubscription: string\n  listId: string\n  isAutomated: boolean\n  precedence: string\n  mailer: string\n  returnPath: string\n  authResults: string\n  bodyHtml: text\nrelations:\n  from: account\n  to: account[]\n  cc: account[]\n  bcc: account[]\n  domain: domain\n  toDomain: domain[]\n  ccDomain: domain[]\n  tag: tag[]\nprior_art:\n- source: RFC 5322 (Internet Message Format)\n  url: https://datatracker.ietf.org/doc/html/rfc5322\n  notes: Supersedes RFC 2822. Our messageId/inReplyTo/references/replyTo map directly\n    to Message-ID/In-Reply-To/References/Reply-To headers; toRaw/ccRaw/bccRaw are\n    the literal header values.\n- source: RFC 2369 + RFC 8058 (List headers, one-click unsubscribe)\n  url: https://datatracker.ietf.org/doc/html/rfc2369\n  notes: Our unsubscribe/unsubscribeOneClick/listId are List-Unsubscribe/List-Unsubscribe-Post/List-ID.\n    RFC 8058 defines the one-click POST semantics.\n- source: Gmail API Message resource\n  url: https://developers.google.com/gmail/api/reference/rest/v1/users.messages\n  notes: Practical API mirror. Our sizeEstimate and isUnread/isStarred/isDraft/isSent/isTrash/isSpam\n    correspond to Gmail's sizeEstimate and labelIds (UNREAD, STARRED, DRAFT, SENT,\n    TRASH, SPAM).\n",
    'episode': 'plural: episodes\ndisplay:\n  subtitle: author\nfields:\n  durationMs: integer\n  episodeNumber: integer\n  seasonNumber: integer\nrelations:\n  series: podcast\n  transcribe: transcript\n  guest: person[]\nprior_art:\n- source: Apple Podcasts RSS Extensions (itunes:episode)\n  url: https://help.apple.com/itc/podcasts_connect/#/itcb54353390\n  notes: De-facto podcast metadata standard. Our episodeNumber/seasonNumber/ durationMs\n    = itunes:episode/itunes:season/itunes:duration.\n- source: schema.org/PodcastEpisode\n  url: https://schema.org/PodcastEpisode\n  notes: "Our series \\u2248 partOfSeries (PodcastSeries); transcribe \\u2248 transcript;\\\n    \\ guest \\u2248 actor."\n- source: Podcast Namespace (podcast:*)\n  url: https://podcastindex.org/namespace/1.0\n  notes: Modern open extension to RSS. Covers our guest, season, episode, and transcript\n    relations via podcast:person, podcast:season, etc.\n',
    'event': 'plural: events\nidentity:\n- at\n- id\ndisplay:\n  subtitle: startDate\n  highlights:\n  - startDate\n  - endDate\n  - location\nfields:\n  startDate: datetime\n  endDate: datetime\n  timezone: string\n  allDay: boolean\n  recurrence: string[]\n  status: string\n  visibility: string\n  showAs: string\n  dateUpdated: datetime\n  sourceUrl: url\n  sourceTitle: string\n  icalUid: string\n  distinctId: string\n  currentUrl: string\n  properties: json\nrelations:\n  at: actor\n  involves: person[]\n  location: place\n  organizer: person\n  creator: person\n  person: person\n  attachments: file[]\nprior_art:\n- source: schema.org/Event\n  url: https://schema.org/Event\n  notes: Core event type. Our startDate/endDate map 1:1; eventType is free-form vs.\n    schema.org\'s subtype hierarchy (Concert, Conference, BusinessEvent). organizer/location\n    match directly.\n- source: RFC 5545 (iCalendar) VEVENT\n  url: https://datatracker.ietf.org/doc/html/rfc5545\n  notes: "Our icalUid is their UID; recurrence is their RRULE; status maps to STATUS\\\n    \\ (TENTATIVE/CONFIRMED/CANCELLED); showAs \\u2248 TRANSP; involves[] \\u2248 ATTENDEE."\n- source: ActivityStreams 2.0 Event\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-event\n  notes: "Fediverse inbox format. Thinner than iCal \\u2014 no native recurrence or\\\n    \\ showAs; our involves[] \\u2248 attendees via as:Relationship."\n',
    'fare': 'plural: fares\nidentity:\n- at\n- identifier\ndisplay:\n  subtitle: fareFamily\nfields:\n  identifier: string\n  bookingCode: string\n  productType: string\n  fareFamily: string\n  class: string\n  basePrice: number\n  currency: string\n  passengerType: string\n  milesEarned: integer\n  pointsEarned: integer\n  components: integer\n  refundable: boolean\n  changeable: boolean\n  restrictions: string[]\n  conditions: json\nrelations:\n  at: actor\n  for: trip\n  legs: leg[]\n  offer: offer\n  reservation: reservation\n  taxLines: tax_line[]\n  earnsInto: membership\nprior_art:\n- source: IATA Fare Basis Code / ATPCO filings\n  url: https://en.wikipedia.org/wiki/Fare_basis_code\n  notes: Airline canonical. First char = RBD/booking class (our `bookingCode`); remainder\n    = airline-proprietary pointer into ATPCO-filed fare rules (our `identifier` as\n    opaque string, `conditions` for the rule blob). Codes are 3-8 chars; we don\'t\n    parse beyond the first char.\n- source: IATA NDC FareDetail / FareComponent\n  url: https://developer.iata.org/en/ndc/\n  notes: NDC\'s FareDetail.FareComponent carries FareBasis.FareBasisCode, FareBasis.RBD,\n    Price.BaseAmount, FareRules.Penalty, and CabinType.CabinTypeCode. Our identifier/bookingCode/basePrice/\n    class/refundable map directly.\n- source: Duffel Offer Slice / fare_basis_code\n  url: https://duffel.com/docs/api/v2/offers\n  notes: Duffel surfaces fare_basis_code on each slice\'s segments along with cabin_class,\n    cabin_class_marketing_name (our fareFamily), and passenger-level base_amount.\n    Our basePrice = base_amount; class = cabin_class; fareFamily = cabin_class_marketing_name.\n- source: Amtrak / Rail Europe fare types\n  url: https://www.amtrak.com/routes/fares\n  notes: "Non-airline generalization. Amtrak fares are Saver / Value / Flexible /\\\n    \\ Premium / Business / First / Acela First / Acela First Refundable \\u2014 their\\\n    \\ tier codes fit `identifier`; their names fit `fareFamily`; their rules fit `refundable`/\\\n    \\ `changeable`/`restrictions`."\n- source: GTFS fare_products.txt (transit)\n  url: https://gtfs.org/documentation/schedule/reference/#fare_productstxt\n  notes: Open transit standard for fare products. Their fare_product_id = our identifier;\n    fare_product_name = fareFamily; amount = basePrice; currency_code = currency.\n    rider_category matches passengerType (adult/child/senior/student).\n- source: schema.org/Offer price + FlightReservation\n  url: https://schema.org/FlightReservation\n  notes: schema.org\'s Offer.price + Offer.priceCurrency align with our basePrice +\n    currency. schema.org has no fare-basis concept; NDC and GTFS fill that gap.\n',
    'file': 'plural: files\ndisplay:\n  subtitle: path\nfields:\n  filename: string\n  mimeType: string\n  size: integer\n  path: string\n  format: string\n  encoding: string\n  lineCount: integer\n  kind: string\n  sha: string\nrelations:\n  attachedTo: message\n  repository: repository\nprior_art:\n- source: IANA Media Types (RFC 6838)\n  url: https://datatracker.ietf.org/doc/html/rfc6838\n  notes: Our mimeType follows type/subtype syntax (text/plain, application/pdf). Canonical\n    source for format identification.\n- source: schema.org/DigitalDocument\n  url: https://schema.org/DigitalDocument\n  notes: "Our filename \\u2248 name; size \\u2248 contentSize; mimeType \\u2248 encodingFormat."\n- source: Git Internals (blob objects)\n  url: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects\n  notes: Our sha is a Git blob SHA-1 (40-hex). Git\'s content-addressable model underlies\n    our repo-file identity.\n',
    'financial_account': 'plural: financial_accounts\nidentity:\n- at\n- identifier\ndisplay:\n  subtitle: last4\nfields:\n  identifier: string\n  accountId: string\n  accountNumber: string\n  routingNumber: string\n  last4: string\n  currency: string\n  accountType: string\n  balance: number\n  available: number\n  creditLimit: number\n  minimumPayment: number\n  cardType: string\n  interestRate: number\nrelations:\n  at: actor\n  accessedVia: account\n  owner: person\nprior_art:\n- source: OFX (Open Financial Exchange)\n  url: https://financialdataexchange.org/ofx\n  notes: Bank-feed canonical. Our accountNumber / routingNumber / balance / available\n    map to OFX BANKACCTFROM / LEDGERBAL / AVAILBAL.\n- source: ISO 20022 Financial Messaging\n  url: https://www.iso20022.org/\n  notes: Modern bank-messaging standard. Our last4 / cardType / creditLimit / interestRate\n    align with ISO 20022 Card / Account components.\n- source: schema.org/BankAccount\n  url: https://schema.org/BankAccount\n  notes: "Our accountNumber \\u2248 accountId; balance / available are accountMinimumInflow\\\n    \\ / accountOverdraftLimit loosely; cardType fits schema.org/CreditCard."\n- source: 1Password Bank Account item\n  url: https://1password.com/\n  notes: "1P\'s Bank Account category holds institution + account number + routing\\\n    \\ + type \\u2014 same shape. Their Crypto Wallet and Credit Card are separate categories;\\\n    \\ we treat them as different `accountType` values on the same shape for now, splitting\\\n    \\ only if the field diversity forces it."\n',
    'flight': 'plural: flights\ndisplay:\n  subtitle: airline\nalso:\n- leg\nfields:\n  flightNumber: string\n  durationMinutes: integer\n  cabinClass: string\n  stops: integer\n  carbonEmissions: json\nrelations:\n  airline: airline\n  departsFrom: airport\n  arrivesAt: airport\n  aircraft: aircraft\nprior_art:\n- source: IATA Resolution 753 / Flight Codeshare\n  url: https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/\n  notes: Our flightNumber follows IATA carrier-code + digits format (UA 1234). Canonical\n    for cross-carrier flight identity.\n- source: Duffel / IATA NDC Slice+Segment\n  url: https://duffel.com/docs/api/v2/overview\n  notes: NDC models a trip (slice) as multiple flights (segments). Our flight shape\n    = NDC segment; our trip = NDC slice.\n- source: schema.org/Flight\n  url: https://schema.org/Flight\n  notes: "Our flightNumber = flightNumber; departsFrom/arrivesAt = departureAirport/arrivalAirport;\\\n    \\ departureTime/arrivalTime match directly; carbonEmissions \\u2248 estimatedFlightDuration\\\n    \\ + emissions extensions."\n',
    'font': 'plural: fonts\nidentity_any:\n- family\n- postscriptName\ndisplay:\n  subtitle: author\nalso:\n- creative_work\nfields:\n  family: string\n  genericFamily: string\n  postscriptName: string\n  weights: integer[]\n  styles: string[]\n  formats: string[]\n  scripts: string[]\n  glyphCount: integer\n  designerUrl: string\n  vendorUrl: string\n  licenseInfoUrl: string\nprior_art:\n- source: schema.org/Typeface\n  url: https://schema.org/Typeface\n  notes: "Schema.org added Typeface in 2024. Sparse compared to OpenType (fontFamily,\\\n    \\ format only) \\u2014 we lean on the OpenType `name` table for most fields."\n- source: OpenType `name` table (ISO/IEC 14496-22)\n  url: https://learn.microsoft.com/en-us/typography/opentype/spec/name\n  notes: nameID 1=family; 6=postscriptName; 8=manufacturer (publisher in our model,\n    via creative_work); 9=designer (author via creative_work); 13=licenseDescription\n    (license via creative_work); 14=licenseInfoUrl; 11=vendorUrl; 12=designerUrl.\n    Our font shape is a graph-native projection of this table; .woff2 metadata can\n    round-trip losslessly.\n- source: Google Fonts metadata\n  url: https://fonts.google.com/specimen/Roboto\n  notes: "Treats fonts as \\"families\\" with weights / styles arrays. Same model we\\\n    \\ adopt. Google Fonts also tracks subsets (Latin / Cyrillic / Greek) \\u2014 equivalent\\\n    \\ to our scripts field."\n- source: ISO 15924 (script codes)\n  url: https://www.unicode.org/iso15924/iso15924-codes.html\n  notes: Our scripts field uses ISO 15924 four-letter codes (Latn / Cyrl / Grek /\n    Arab / Hans / Hant / Jpan / Kore / etc.). Canonical identification of writing\n    systems.\n',
    'git_commit': 'plural: git_commits\nalso:\n- event\ndisplay:\n  subtitle: author\nfields:\n  sha: string\n  shortHash: string\n  message: text\n  additions: integer\n  deletions: integer\n  filesChanged: integer\n  committedAt: datetime\nrelations:\n  author: account\n  committer: account\n  repository: repository\n  parent: git_commit\nprior_art:\n- source: "Git Internals \\u2014 commit object"\n  url: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects\n  notes: Our sha/shortHash/message/parent match the commit object exactly. author/committer\n    follow Git\'s distinct author-vs-committer model.\n- source: Conventional Commits 1.0\n  url: https://www.conventionalcommits.org/en/v1.0.0/\n  notes: "Practical structure for message field (type(scope): subject). Optional \\u2014\\\n    \\ we don\'t enforce but it\'s compatible."\n',
    'group': 'plural: groups\nidentity:\n- at\n- id\ndisplay:\n  subtitle: category\nfields:\n  memberCount: integer\n  category: string\nprior_art:\n- source: schema.org/Group (via Organization/memberOf)\n  url: https://schema.org/Organization\n  notes: "schema.org models groups as Organization. Our memberCount \\u2248 numberOfEmployees\\\n    \\ loosely; category \\u2248 naics/knowsAbout."\n- source: FOAF Group\n  url: http://xmlns.com/foaf/spec/#term_Group\n  notes: Foundational social-graph vocabulary. foaf:member populates membership; category\n    has no direct FOAF peer.\n',
    'hardware': 'plural: hardware\nidentity: serialNumber\ndisplay:\n  subtitle: author\nalso:\n- product\nfields:\n  modelNumber: string\n  serialNumber: string\n  specs: json\nrelations:\n  manufacturer: organization\nprior_art:\n- source: schema.org/Product (IndividualProduct subtype)\n  url: https://schema.org/IndividualProduct\n  notes: "Our serialNumber = serialNumber; modelNumber \\u2248 model; specs \\u2248\\\n    \\ additionalProperty (PropertyValue list)."\n- source: GS1 Global Trade Item Number (GTIN)\n  url: https://www.gs1.org/standards/id-keys/gtin\n  notes: "Hardware bar-codes are GTIN-12/13/14 \\u2014 we reuse the product shape\'s\\\n    \\ barcode alignment."\n',
    'health-biomarker': 'plural: health-biomarkers\nidentity_any:\n- loincCode\n- measure\ndisplay:\n  subtitle: category\nfields:\n  measure: string\n  category: string\n  loincCode: string\n  analyteType: string\n  description: text\nrelations:\n  panels: health-panel[]\nprior_art:\n- source: "HL7 FHIR R5 \\u2014 ObservationDefinition"\n  url: https://www.hl7.org/fhir/observationdefinition.html\n  notes: "FHIR\'s ObservationDefinition is the reusable definition of an observable,\\\n    \\ separate from the Observation that records a value. Our measure/category map\\\n    \\ to its code + quantitativeDetails. We deliberately do NOT include its qualifiedInterval\\\n    \\ \\u2014 reference ranges are their own shape (health-reference-range)."\n- source: "LOINC \\u2014 Logical Observation Identifiers Names and Codes"\n  url: https://loinc.org/\n  notes: "The universal code system for lab and clinical observations. loincCode is\\\n    \\ the join key \\u2014 every lab observable has a LOINC code (TSH 3016-3, LDL 2089-1,\\\n    \\ HbA1c 4548-4). LOINC identifies the observable only; it carries no reference\\\n    \\ range."\n',
    'health-condition': 'plural: health-conditions\nidentity_any:\n- snomedCode\n- name\ndisplay:\n  subtitle: clinicalStatus\nfields:\n  clinicalStatus: string\n  verificationStatus: string\n  proximity: string\n  bodySite: string\n  severity: string\n  snomedCode: string\n  icd10Code: string\n  clinicalArea: string\n  mitigation: text\nrelations:\n  subject: person\n  evidence: file[]\nprior_art:\n- source: "HL7 FHIR R5 \\u2014 Condition"\n  url: https://www.hl7.org/fhir/condition.html\n  notes: The resource for a problem/diagnosis. Our clinicalStatus, verificationStatus,\n    severity, bodySite, onsetDate, abatementDate map directly. proximity=\'self\' is\n    a plain FHIR Condition.\n- source: "HL7 FHIR R5 \\u2014 FamilyMemberHistory"\n  url: https://www.hl7.org/fhir/familymemberhistory.html\n  notes: "FHIR\'s separate resource for hereditary risk. We fold it in via proximity\\\n    \\ \\u2014 proximity=\'father\'|\'extended-family\' makes a condition node a family-history\\\n    \\ entry. FamilyMemberHistory.condition \\u2248 this node; FamilyMemberHistory.relationship\\\n    \\ \\u2248 our proximity. Deliberate divergence from FHIR\'s two-resource split."\n- source: SNOMED CT\n  url: https://www.snomed.org/\n  notes: The universal clinical terminology. snomedCode is the canonical identity\n    (asthma 195967001, eczema 43116000). FHIR Condition.code is SNOMED-coded; this\n    is the join key to the wider clinical world.\n- source: ICD-10-CM\n  url: https://www.cdc.gov/nchs/icd/icd-10-cm.htm\n  notes: "The diagnosis/billing code system. icd10Code captures the code when it appears\\\n    \\ on an insurance claim or discharge summary \\u2014 complements (does not replace)\\\n    \\ SNOMED."\n',
    'health-immunization': 'plural: health-immunizations\nalso:\n- event\ndisplay:\n  subtitle: dateAdministered\nfields:\n  dateAdministered: datetime\n  cvxCode: string\n  manufacturer: string\n  lotNumber: string\n  doseNumber: integer\n  seriesDoses: integer\n  site: string\n  route: string\n  diseaseTarget: string\n  notes: text\nrelations:\n  administeredAt: health-lab\n  subject: person\n  evidence: file[]\nprior_art:\n- source: "HL7 FHIR R5 \\u2014 Immunization"\n  url: https://www.hl7.org/fhir/immunization.html\n  notes: "The resource for an administered vaccine. dateAdministered \\u2248 occurrenceDateTime;\\\n    \\ manufacturer \\u2248 manufacturer; lotNumber \\u2248 lotNumber; site/route \\u2248\\\n    \\ site/route; doseNumber \\u2248 protocolApplied.doseNumber; seriesDoses \\u2248\\\n    \\ protocolApplied.seriesDoses."\n- source: "CDC CVX \\u2014 Vaccine Administered code set"\n  url: https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx\n  notes: The US standard vaccine code system. cvxCode is the canonical vaccine identity\n    (CVX 208 = COVID-19 Pfizer, CVX 20 = DTaP). FHIR Immunization.vaccineCode is CVX-coded.\n- source: "HL7 v2.x \\u2014 VXU (Unsolicited Vaccination Update)"\n  url: https://www.cdc.gov/vaccines/programs/iis/technical-guidance/hl7.html\n  notes: "The message format Immunization Information Systems exchange. The RXA segment\\\n    \\ carries date, CVX, lot, manufacturer, site, route \\u2014 confirms the field\\\n    \\ set."\n',
    'health-lab': 'plural: health-labs\nalso:\n- organization\nidentity_any:\n- cliaNumber\n- url\ndisplay:\n  subtitle: labType\nfields:\n  cliaNumber: string\n  npi: string\n  ccn: string\n  labType: string\n  accreditation: string\nprior_art:\n- source: schema.org/MedicalOrganization / DiagnosticLab\n  url: https://schema.org/DiagnosticLab\n  notes: "schema.org\'s DiagnosticLab is a MedicalOrganization subtype, which is an\\\n    \\ Organization subtype \\u2014 exactly our also:[organization] chain. Our labType\\\n    \\ refines what schema.org leaves implicit."\n- source: "CLIA \\u2014 Clinical Laboratory Improvement Amendments"\n  url: https://www.cms.gov/medicare/quality/clinical-laboratory-improvement-amendments\n  notes: cliaNumber, npi (the organizational/type-2 National Provider Identifier),\n    and ccn (the Medicare CMS Certification Number) are all CMS-issued identifiers\n    a US testing facility carries. cliaNumber is the canonical identity for a US clinical\n    lab.\n- source: "HL7 FHIR R5 \\u2014 Organization (role: laboratory)"\n  url: https://www.hl7.org/fhir/organization.html\n  notes: "FHIR models a lab as an Organization with a laboratory role code, not a\\\n    \\ distinct resource \\u2014 consistent with our also:[organization]. FHIR Observation.performer\\\n    \\ / DiagnosticReport.performer reference it; our health-panel.performedAt and\\\n    \\ health-reference-range. issuingLab edges are the same linkage."\n',
    'health-observation': 'plural: health-observations\nalso:\n- result\n- event\ndisplay:\n  subtitle: startDate\nfields:\n  value: number\n  valueText: string\n  refLow: number\n  refHigh: number\n  refText: string\n  flag: string\n  status: string\n  notes: text\nrelations:\n  measures: health-biomarker\n  fromPanel: health-panel\n  reportedRange: health-reference-range\n  document: file\n  subject: person\nprior_art:\n- source: "HL7 FHIR R5 \\u2014 Observation"\n  url: https://www.hl7.org/fhir/observation.html\n  notes: "The canonical resource for a measured value. value (with its UCUM unit)\\\n    \\ \\u2248 valueQuantity; effectiveDate \\u2248 effectiveDateTime; refLow/refHigh/refText\\\n    \\ \\u2248 the referenceRange backbone (the inline snapshot); flag \\u2248 interpretation;\\\n    \\ status \\u2248 status. `measures` \\u2248 code resolved to a biomarker. FHIR has\\\n    \\ no normalized-range link \\u2014 our `reportedRange` edge adds that."\n- source: "HL7 v2.x \\u2014 OBX segment"\n  url: https://hl7-definition.caristix.com/v2/HL7v2.5/Segments/OBX\n  notes: "The legacy lab-result segment most labs still emit. OBX-5 (value) and OBX-6\\\n    \\ (units) together \\u2248 our value-with-unit; OBX-7 (reference range), OBX-8\\\n    \\ (abnormal flag), OBX-14 (datetime) map to refText/ flag/effectiveDate. Confirms\\\n    \\ the snapshot field set against real lab feeds."\n- source: LOINC\n  url: https://loinc.org/\n  notes: "The observation itself is not LOINC-coded \\u2014 its `biomarker` is. The\\\n    \\ `measures` edge carries the LOINC identity."\n- source: "UCUM \\u2014 Unified Code for Units of Measure"\n  url: https://ucum.org/\n  notes: "The unit on every numeric val (mg/dL, mmol/L, 10*3/uL) follows UCUM \\u2014\\\n    \\ the unit system FHIR mandates for Observation.valueQuantity, so observations\\\n    \\ round-trip into FHIR cleanly."\n',
    'health-panel': 'plural: health-panels\nalso:\n- list\n- event\ndisplay:\n  subtitle: startDate\nfields:\n  panelCode: string\n  fasting: boolean\n  description: text\nrelations:\n  performedAt: health-lab\n  document: file\n  subject: person\nprior_art:\n- source: "HL7 FHIR R5 \\u2014 DiagnosticReport"\n  url: https://www.hl7.org/fhir/diagnosticreport.html\n  notes: "A dated panel is a DiagnosticReport: a set of observations grouped under\\\n    \\ one report with an effective date and a performer. Our `contains` edges (from\\\n    \\ `list`) \\u2248 DiagnosticReport.result; effectiveDate \\u2248 effectiveDateTime;\\\n    \\ performedAt \\u2248 performer."\n- source: "LOINC \\u2014 Panels and Forms"\n  url: https://loinc.org/panels/\n  notes: "LOINC defines panel codes and their member observables (CBC panel 58410-2\\\n    \\ enumerates hemoglobin, hematocrit, WBC, \\u2026). panelCode plus the contains\\u2192\\\n    biomarker edges mirror a LOINC panel definition."\n- source: schema.org/MedicalTest\n  url: https://schema.org/MedicalTest\n  notes: "Lighter-weight precedent \\u2014 a diagnostic test with usedToDiagnose /\\\n    \\ normalRange. Our panel is the grouping; biomarkers and health-reference-range\\\n    \\ carry the observable detail and the ranges."\n',
    'health-procedure': 'plural: health-procedures\nalso:\n- event\nidentity_any:\n- cptCode\n- snomedCode\n- id\ndisplay:\n  subtitle: performedDate\nfields:\n  performedDate: datetime\n  procedureType: string\n  bodySite: string\n  outcome: string\n  status: string\n  cptCode: string\n  snomedCode: string\n  findings: text\n  followUp: text\nrelations:\n  treats: health-condition\n  performer: person\n  orderedBy: person\n  performedAt: health-lab\n  subject: person\n  evidence: file[]\nprior_art:\n- source: "HL7 FHIR R5 \\u2014 Procedure"\n  url: https://www.hl7.org/fhir/procedure.html\n  notes: "The resource for an action performed on a patient. performedDate \\u2248\\\n    \\ occurrenceDateTime/occurrencePeriod; status \\u2248 status; bodySite \\u2248 bodySite;\\\n    \\ outcome \\u2248 outcome; findings \\u2248 report + note; `treats` edge \\u2248\\\n    \\ reason; performer \\u2248 performer.actor. `orderedBy` \\u2248 basedOn \\u2192\\\n    \\ ServiceRequest.requester \\u2014 the clinician who ordered the study, which on\\\n    \\ imaging/scopes is rarely the one who performs it."\n- source: "CPT \\u2014 Current Procedural Terminology (AMA)"\n  url: https://www.ama-assn.org/practice-management/cpt\n  notes: The US procedure code system used for billing. cptCode is the identity on\n    insurance claims and operative records (septoplasty 30520, colonoscopy 45378).\n- source: "SNOMED CT \\u2014 Procedure axis"\n  url: https://www.snomed.org/\n  notes: SNOMED\'s procedure hierarchy provides the clinical (non-billing) code. FHIR\n    Procedure.code is SNOMED-coded; snomedCode is the join key to the clinical ontology.\n',
    'health-reference-range': 'plural: health-reference-ranges\nalso:\n- event\nidentity:\n- analyte\n- issuingLab\n- method\n- startDate\ndisplay:\n  subtitle: refText\nfields:\n  low: number\n  high: number\n  unit: string\n  refText: string\n  category: string\n  provenance: string\n  method: string\n  ageLow: number\n  ageHigh: number\n  sex: string\n  pregnancy: string\n  gestationalAge: string\n  fasting: boolean\n  timeOfDay: string\nrelations:\n  analyte: health-biomarker\n  issuingLab: health-lab\nprior_art:\n- source: "CLSI EP28-A3c \\u2014 Defining, Establishing, and Verifying Reference Intervals"\n  url: https://clsi.org/shop/standards/ep28/\n  notes: The authoritative protocol. Each lab must establish (de novo, min n=120 per\n    partition) or verify (min n=20) its own intervals. `provenance` (established/verified/manufacturer-claimed)\n    comes directly from this guideline; it is why two same-instrument labs legitimately\n    diverge.\n- source: "HL7 FHIR R5 \\u2014 ObservationDefinition.qualifiedInterval"\n  url: https://www.hl7.org/fhir/observationdefinition.html\n  notes: "The closest standard precedent \\u2014 a reusable, multi-context interval.\\\n    \\ Our category maps to its rangeCategory; range to range; age/gestationalAge/sex\\\n    \\ to the same; condition \\u2248 our population fields. But qualifiedInterval has\\\n    \\ NO issuingLab and NO validity window \\u2014 this shape adds both. qualifiedInterval\\\n    \\ is the lossy EXPORT projection of this shape, not its equal."\n- source: "HL7 FHIR R5 \\u2014 Observation.referenceRange"\n  url: https://www.hl7.org/fhir/observation.html\n  notes: "FHIR\'s other reference-range model \\u2014 inlined on the result as a denormalized\\\n    \\ snapshot (low/high/normalValue/type/appliesTo/age/ text). health-observation\\\n    \\ keeps that snapshot too (its refLow/ refHigh fields); this shape is the normalized,\\\n    \\ reusable form the snapshot can point back to."\n- source: "OMOP CDM v5.4 \\u2014 MEASUREMENT.range_low / range_high"\n  url: https://ohdsi.github.io/CommonDataModel/cdm54.html\n  notes: "OMOP inlines range_low/range_high as columns on the measurement row \\u2014\\\n    \\ \\"no separate standalone table for reference ranges.\\" Confirms the gap: no\\\n    \\ major model makes the range first-class."\n',
    'icon': 'plural: icons\nidentity_any:\n- component\n- url\ndisplay:\n  subtitle: purpose\nalso:\n- creative_work\nfields:\n  dimension: integer\n  format: string\n  url: string\n  component: string\n  purpose: string\n  style: string\nprior_art:\n- source: schema.org/ImageObject\n  url: https://schema.org/ImageObject\n  notes: "Icons could be modeled as ImageObject \\u2014 we chose a distinct shape because\\\n    \\ the role-specific `purpose` field has no counterpart on ImageObject (which is\\\n    \\ purpose-agnostic by design) and because component-backed icons aren\'t fetchable\\\n    \\ as image URLs."\n- source: Iconify metadata\n  url: https://iconify.design/\n  notes: Iconify treats icons as named entries within an icon set, each with a category\n    and tags. Our `purpose` field plays the same role as Iconify\'s category; our `style`\n    plays the same role as Iconify\'s iconset style attribute (filled / outline / pixel).\n- source: Material Symbols metadata\n  url: https://fonts.google.com/icons\n  notes: "Material Symbols ship as a variable icon font with `fill`, `weight`, `grade`,\\\n    \\ and `optical-size` axes. Our shape doesn\'t model variable axes (Material Symbols\\\n    \\ would be one font, not one icon-per-glyph) \\u2014 we model icons that live OUTSIDE\\\n    \\ icon fonts."\n- source: macOS / Windows system icon naming\n  url: https://learn.microsoft.com/en-us/windows/win32/uxguide/vis-icons\n  notes: Both platforms standardize on role-named icons (e.g. "back", "forward", "close")\n    rather than file-named icons. Our `purpose` field follows the same convention;\n    theme authors register icons by their semantic role, not by a filename slug.\n',
    'image': 'plural: images\ndisplay:\n  subtitle: format\nidentity_any:\n- url\nalso:\n- creative_work\n- file\nfields:\n  width: integer\n  height: integer\n  format: string\n  altText: string\n  appName: string\n  windowId: integer\n  displayId: integer\n  displayIndex: integer\nprior_art:\n- source: schema.org/ImageObject\n  url: https://schema.org/ImageObject\n  notes: "Our width/height = width/height; format \\u2248 encodingFormat; altText =\\\n    \\ caption/accessibilityCaption."\n- source: IANA Media Types (image/*)\n  url: https://www.iana.org/assignments/media-types/media-types.xhtml#image\n  notes: Our format values (PNG, JPEG, WebP, SVG) align with registered image/* media\n    types.\n- source: Exif 2.3 (JEITA CP-3451)\n  url: https://www.cipa.jp/std/documents/e/DC-008-Translation-2019-E.pdf\n  notes: Source of most image metadata fields. width/height come from Exif PixelXDimension/PixelYDimension.\n',
    'intellectual_property': 'plural: intellectual_properties\ndisplay:\n  subtitle: category\n  highlights:\n  - identifier\n  - status\n  - granted_by\nidentity_any:\n- identifier\nfields:\n  category: string\n  mark: string\n  identifier: string\n  register: string\n  status: string\n  filingBasis: string\n  niceClass: integer[]\n  validIn: string\n  renewalPeriod: string\n  verificationUrl: url\nrelations:\n  held_by: actor\n  granted_by: organization\n  covers: creative_work\nprior_art:\n- source: "Wikidata \\u2014 trademark (Q167270) / registered trademark (Q111048186)"\n  url: https://www.wikidata.org/wiki/Q167270\n  notes: "Trademark is a subclass of `intellectual property right` and of `mark`;\\\n    \\ holder via `owned by` (P127). registered-vs-pending is a status of one type,\\\n    \\ not a separate type \\u2014 our `status` field."\n- source: "WIPO Standard ST.96 \\u2014 Trademark Components"\n  url: https://www.wipo.int/standards/en/st96/v8-0/release_notes.html\n  notes: "Canonical IP-office XML model. Source for mark, identifier, register, niceClass,\\\n    \\ status. Splits schemas by Trademark / Patent / Design Components \\u2014 confirms\\\n    \\ `category` as the discriminator across one `intellectual_property` concept."\n- source: "WIPO Standard ST.87 \\u2014 IP event codes"\n  url: https://www.wipo.int/standards/en/\n  notes: "Standard lifecycle-event vocabulary (KeyEventCode). The filed/published/granted/lapsed\\\n    \\ milestones are dated edges to the granting office, not node fields \\u2014 events-as-edges\\\n    \\ rule 1."\n- source: Nice Classification (Nice Agreement 1957; NCL 13-2026)\n  url: https://www.wipo.int/en/web/classification-nice\n  notes: "45-class system (1-34 goods, 35-45 services). `niceClass` is an integer[]\\\n    \\ of class numbers \\u2014 a standard code. ADAVIA is Class 42."\n- source: "USPTO \\u2014 trademark process & intent-to-use basis"\n  url: https://www.uspto.gov/trademarks/basics/trademark-process\n  notes: Lifecycle and the use-vs-intent-to-use fork. Source for the `status` value\n    set and `filingBasis`.\n- source: schema.org/Intangible, schema.org/Brand\n  url: https://schema.org/Intangible\n  notes: "Weak alignment \\u2014 schema.org has no Trademark type; `Brand` is the marketing\\\n    \\ concept, not the legal right. Cited to mark the gap web ontologies leave: the\\\n    \\ IP right needs its own shape."\n',
    'invitation': 'plural: invitations\nidentity:\n- at\n- id\nalso:\n- event\ndisplay:\n  subtitle: invitationType\nfields:\n  invitationType: string\n  email: string\n  role: string\n  status: string\n  token: string\n  acceptedAt: datetime\n  revokedAt: datetime\n  message: text\nrelations:\n  inviter: account\n  invitee: account\n  organization: organization\n  at: actor\nprior_art:\n- source: ActivityStreams 2.0 Invite activity\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-invite\n  notes: AS2 Invite is the canonical fediverse verb. Our inviter = actor; invitee\n    = target; status tracks Accept/Reject/TentativeAccept responses.\n- source: iCalendar ATTENDEE + PARTSTAT (RFC 5545)\n  url: https://datatracker.ietf.org/doc/html/rfc5545\n  notes: Calendar-style invitations. Our status maps to PARTSTAT (NEEDS-ACTION/ACCEPTED/DECLINED/DELEGATED).\n- source: "SCIM 2.0 (RFC 7644) \\u2014 user provisioning"\n  url: https://datatracker.ietf.org/doc/html/rfc7644\n  notes: Enterprise invitation/provisioning. Our email/role/organization align with\n    SCIM User resource\'s email + entitlements + group membership.\n',
    'launch': "plural: launches\nalso:\n- event\ndisplay:\n  subtitle: rocketId\n  highlights:\n  - startDate\n  - rocketId\n  - launchpadId\nfields:\n  flightNumber: integer\n  rocketId: string\n  launchpadId: string\n  crewIds: string[]\n  reusedBoosters: string[]\n  landingOutcomes: json\n  articleUrl: url\n  webcastUrl: url\n  wikipediaUrl: url\n  patchImage: url\nprior_art:\n- source: SpaceX r/SpaceX API v4\n  url: https://github.com/r-spacex/SpaceX-API\n  notes: Original source of these fields. The fly-by-night-launch.com skill maps the\n    v4 launches endpoint onto this shape; the per-booster landing outcomes JSON mirrors\n    that API's `cores` sub-document.\n",
    'leg': 'plural: legs\nalso:\n- event\ndisplay:\n  subtitle: flightNumber\nfields:\n  sequence: integer\n  departureTime: datetime\n  arrivalTime: datetime\n  duration: string\n  durationMinutes: integer\n  flightNumber: string\n  cabinClass: string\n  vehicleType: string\n  layoverMinutes: integer\n  carbonEmissions: json\n  trace: json\n  tracePointCount: integer\n  polyline: string\nrelations:\n  origin: place\n  destination: place\n  carrier: organization\n  aircraft: aircraft\n  trip: trip\nprior_art:\n- source: IATA NDC "segment"\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: NDC segment = our leg. flightNumber, departureTime, arrivalTime, cabinClass\n    come straight from NDC OfferItem Segment.\n- source: GTFS stop_times.txt\n  url: https://gtfs.org/documentation/schedule/reference/#stop_timestxt\n  notes: Transit leg model. Our sequence = stop_sequence; departureTime/ arrivalTime\n    = arrival_time/departure_time.\n- source: Google Encoded Polyline Algorithm\n  url: https://developers.google.com/maps/documentation/utilities/polylinealgorithmformat\n  notes: Our polyline field is the standard Google encoded polyline. trace is a denser\n    GPS breadcrumb alternative (GeoJSON-adjacent).\n',
    'list': 'plural: lists\nidentity:\n- at\n- id\ndisplay:\n  subtitle: name\nfields:\n  id: string\n  listId: string\n  listType: string\n  ordering_mode: string\n  privacy: string\n  isDefault: boolean\n  isPublic: boolean\n  itemCount: integer\n  default_view: string\n  icon_size: integer\n  sort_by: string\n  path: string\nrelations:\n  at: actor\n  belongsTo: account\n  contains: node[]\n  background_image: image\nprior_art:\n- source: schema.org/ItemList\n  url: https://schema.org/ItemList\n  notes: "listType \\u2248 itemListOrder; contains \\u2248 itemListElement; isPublic\\\n    \\ \\u2248 publicAccess."\n- source: ActivityStreams 2.0 Collection / OrderedCollection\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection\n  notes: "contains[] \\u2248 items; ordering_mode=\'linear\' \\u2248 OrderedCollection,\\\n    \\ ordering_mode=\'unordered\' \\u2248 Collection."\n- source: WinFS Item / FolderMember\n  url: https://learn.microsoft.com/en-us/archive/msdn-magazine/2004/january/winfs-lets-users-search-and-manage-files-based-on-content\n  notes: \'WinFS unified Folder + Contact + Photo under a single Item base, with FolderMember\n    as a holding edge. Our list-with-contains is the same pattern: one shape, one\n    edge mechanism, view-time projections handle the "I want it to look like an album"\n    case.\'\n- source: "Vannevar Bush \\u2014 As We May Think (Memex trails)"\n  url: https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/\n  notes: A Memex trail is a named, ordered list of associative jumps. A `list` with\n    ordering_mode=\'linear\' and contains-bookmarks IS Bush\'s trail. Foundational precedent\n    for the everything-is-a-list thesis.\n- source: POSIX / Single Unix Specification (directories)\n  url: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html\n  notes: listType=\'folder\' with optional `path` field mirrors a POSIX directory. The\n    engine treats it as a list; the filesystem mirror is a projection, not a separate\n    primitive.\n',
    'loaded_model': 'plural: loaded_models\nalso:\n- event\ndisplay:\n  subtitle: size\nfields:\n  size: string\n  quantization: string\n  vramUsage: string\n  sizeVram: integer\n  digest: string\nprior_art:\n- source: "Ollama API \\u2014 /api/ps"\n  url: https://github.com/ollama/ollama/blob/main/docs/api.md#list-running-models\n  notes: Direct source. Our size/vramUsage/sizeVram/quantization/digest/ expiresAt\n    map to Ollama\'s ListRunningModelsResponse fields.\n- source: OpenTelemetry Resource semconv (ML/AI)\n  url: https://opentelemetry.io/docs/specs/semconv/gen-ai/\n  notes: Emerging conventions for GenAI observability. Our size/digest align with\n    gen_ai.model.* resource attributes.\n',
    'mcp_session': 'plural: mcp_sessions\nidentity:\n- client\n- projectId\n- gitBranch\ndisplay:\n  subtitle: client\nicon: terminal\nfields:\n  client: string\n  projectId: string\n  gitBranch: string\n  sessionType: string\n  startedAt: datetime\n  endedAt: datetime\n  messageCount: integer\n  tokenCount: integer\nrelations:\n  participant: actor\n  folder: list\nprior_art:\n- source: Model Context Protocol (MCP) session\n  url: https://modelcontextprotocol.io/specification\n  notes: Direct source. Our client/sessionType come from MCP\'s client/transport concepts\n    (STDIO, HTTP+SSE).\n- source: "OpenTelemetry Spans (root span \\u2248 session)"\n  url: https://opentelemetry.io/docs/concepts/signals/traces/\n  notes: Our startedAt/endedAt/messageCount/tokenCount align with span lifecycle +\n    attributes in a trace context.\n- source: OpenID Connect Session Management 1.0\n  url: https://openid.net/specs/openid-connect-session-1_0.html\n  notes: "Classical web-session model. Our participant \\u2248 authenticated subject;\\\n    \\ projectId/gitBranch are AgentOS-specific scoping."\n',
    'meeting': 'plural: meetings\ndisplay:\n  subtitle: location\nalso:\n- event\nfields:\n  calendarLink: url\n  isVirtual: boolean\n  meetingUrl: url\n  conferenceProvider: string\n  phoneDialIn: string\n  meetingType: string\nrelations:\n  transcribe: transcript\nprior_art:\n- source: RFC 5545 VEVENT + conference property (RFC 7986)\n  url: https://datatracker.ietf.org/doc/html/rfc7986#section-5.11\n  notes: "Our meetingUrl \\u2248 CONFERENCE URI; phoneDialIn = tel: URI in CONFERENCE\\\n    \\ feature=PHONE; conferenceProvider \\u2248 CONFERENCE LABEL."\n- source: "schema.org/Event \\u2014 location.VirtualLocation"\n  url: https://schema.org/VirtualLocation\n  notes: "Our isVirtual triggers VirtualLocation; meetingUrl \\u2248 VirtualLocation.url."\n- source: Google Calendar Event conferenceData\n  url: https://developers.google.com/calendar/api/v3/reference/events\n  notes: "Practical API mirror. Our conferenceProvider \\u2248 conferenceData.conferenceSolution.name;\\\n    \\ meetingUrl = entryPoints[uri]."\n',
    'membership': 'plural: memberships\nidentity:\n- at\n- id\nalso:\n- event\ndisplay:\n  subtitle: status\nfields:\n  status: string\n  tier: string\n  autoRenew: boolean\n  price: number\n  currency: string\n  billingType: string\n  useCount: integer\n  guestPassQuantity: integer\nrelations:\n  at: actor\n  account: account\n  member: person\n  plan: product\n  location: place\nprior_art:\n- source: schema.org/ProgramMembership\n  url: https://schema.org/ProgramMembership\n  notes: "schema.org\'s canonical membership type. Our member = member; plan \\u2248\\\n    \\ programName/membershipNumber; at \\u2248 hostingOrganization. ProgramMembership\\\n    \\ covers gym, loyalty, society memberships without requiring a billing cycle \\u2014\\\n    \\ matches our non-commercial framing."\n- source: schema.org/Subscription\n  url: https://schema.org/Subscription\n  notes: "Streaming/SaaS subscriptions fit this shape \\u2014 one model covers gym\\\n    \\ memberships and Spotify Premium. billingType maps to billingPeriod; autoRenew\\\n    \\ maps directly."\n- source: Stripe Subscriptions API\n  url: https://docs.stripe.com/api/subscriptions\n  notes: "Practical API mirror for commercial memberships. Our status values (active/paused/cancelled/past_due)\\\n    \\ mirror Stripe Subscription.status. nextBillDate \\u2248 current_period_end."\n- source: Mindbody Contracts/Memberships\n  url: https://developers.mindbodyonline.com/PublicDocumentation/V6\n  notes: Gym-industry API. Our useCount, guestPassQuantity, startEffectiveDate / endEffectiveDate\n    are lifted from Mindbody\'s Membership record shape.\n- source: FOAF member / membershipClass\n  url: http://xmlns.com/foaf/spec/#term_member\n  notes: "Social-web vocabulary for \\"X is a member of Y\\". Our member \\u2194 at edge\\\n    \\ mirrors foaf:member; our tier \\u2248 foaf:membershipClass."\n',
    'memex': 'plural: memex\nalso:\n- event\ndisplay:\n  subtitle: description\nicon: brain\nfields:\n  description: text\n  origin: string\n  filePath: string\n  nodeCount: integer\n  edgeCount: integer\n  fileSize: string\n  published: boolean\nrelations:\n  owner: person\n  forkedFrom: memex\n  snapshots: memex[]\nprior_art:\n- source: "Vannevar Bush \\u2014 \\"As We May Think\\" (1945)"\n  url: https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/\n  notes: The original concept. Our memex is named after and modeled on Bush\'s personal\n    knowledge store with associative trails.\n- source: W3C RDF 1.1 + Named Graphs\n  url: https://www.w3.org/TR/rdf11-concepts/\n  notes: "Formal underpinning. Our nodeCount/edgeCount mirror RDF subject-predicate-object\\\n    \\ triples; snapshots \\u2248 named-graph versioning."\n- source: Roam Research / Obsidian / Logseq PKM model\n  url: https://obsidian.md/\n  notes: Practical modern precedents. Our origin values (personal, domain, fork) generalize\n    the single-user PKM model to shareable graphs.\n',
    'message': 'plural: messages\nidentity:\n- at\n- id\ndisplay:\n  subtitle: from\nfields:\n  isOutgoing: boolean\n  isStarred: boolean\n  conversationId: string\nrelations:\n  at: actor\n  from: actor\n  inConversation: conversation\n  repliesTo: message\n  toolCalls: tool_call[]\nprior_art:\n- source: ActivityStreams 2.0 Note/Activity\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-note\n  notes: "Closest open standard for generic messages. Our from \\u2248 actor; inConversation\\\n    \\ \\u2248 context/conversation; repliesTo \\u2248 inReplyTo."\n- source: Matrix m.room.message\n  url: https://spec.matrix.org/latest/client-server-api/#mroommessage\n  notes: "Practical cross-platform message event schema. Our isOutgoing has no Matrix\\\n    \\ analog (sender identity instead); repliesTo \\u2248 m.relates_to rel_type m.thread/m.in_reply_to."\n- source: XMPP (RFC 6121) message stanza\n  url: https://datatracker.ietf.org/doc/html/rfc6121\n  notes: IETF instant-messaging baseline. from/to/thread correspond to our from/inConversation;\n    no standardized isStarred.\n',
    'model': "plural: models\nidentity:\n- at\n- name\ndisplay:\n  subtitle: name\nfields:\n  contextLength: integer\n  contextWindow: integer\n  maxOutput: integer\n  pricingInput: string\n  pricingOutput: string\n  modality: string[]\n  modelType: string\n  quantization: string\n  quantizationLevel: string\n  size: string\n  parameterSize: string\n  format: string\n  family: string\n  digest: string\nrelations:\n  at: actor\nprior_art:\n- source: Hugging Face Model Cards\n  url: https://huggingface.co/docs/hub/en/model-cards\n  notes: Our provider/contextLength/modality/family/quantization/ parameterSize align\n    with HF model-card metadata conventions.\n- source: Ollama /api/show + Modelfile\n  url: https://github.com/ollama/ollama/blob/main/docs/modelfile.md\n  notes: Our quantization/quantizationLevel/format/digest/parameterSize come directly\n    from Ollama's show-model response.\n- source: OpenRouter Models API\n  url: https://openrouter.ai/docs/models\n  notes: Our contextLength/contextWindow/maxOutput/pricingInput/ pricingOutput mirror\n    OpenRouter's model spec.\n",
    'note': 'plural: notes\ndisplay:\n  subtitle: noteType\nfields:\n  noteType: string\n  isPinned: boolean\nrelations:\n  createdBy: person\n  references: note[]\n  extractedFrom: webpage\nprior_art:\n- source: Zettelkasten / Luhmann slip-box\n  url: https://zettelkasten.de/overview/\n  notes: "Our noteType (fleeting/literature/permanent) is the canonical Zettelkasten\\\n    \\ triad; references[] \\u2248 Luhmann\'s permanent links."\n- source: W3C Web Annotation Data Model\n  url: https://www.w3.org/TR/annotation-model/\n  notes: Our extractedFrom = target; createdBy = creator. Notes are annotations without\n    a structured position selector.\n- source: Obsidian / Roam / Logseq PKM conventions\n  url: https://obsidian.md/\n  notes: Practical PKM lineage. isPinned/noteType mirror the "pinned/daily/permanent"\n    UX of modern note apps.\n',
    'offer': 'plural: offers\nidentity:\n- id\nalso:\n- event\ndisplay:\n  subtitle: price\nfields:\n  price: number\n  currency: string\n  offerType: string\n  availability: string\n  bookingToken: string\n  departureToken: string\nrelations:\n  for: product\n  offeredBy: organization\n  trips: trip[]\nprior_art:\n- source: schema.org/Offer\n  url: https://schema.org/Offer\n  notes: Our price = price; currency = priceCurrency; availability = availability;\n    validFrom/validUntil match directly.\n- source: IATA NDC OfferItem\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: "Our bookingToken \\u2248 OfferItemID; validUntil \\u2248 TimeLimits/ OfferExpirationDateTime;\\\n    \\ trips[] \\u2248 Itinerary."\n- source: schema.org/AggregateOffer\n  url: https://schema.org/AggregateOffer\n  notes: For price-range offers (SerpAPI flight results). offerType is AgentOS-specific.\n',
    'order': 'plural: orders\nidentity:\n- at\n- orderId\nalso:\n- event\ndisplay:\n  subtitle: total\nfields:\n  orderId: string\n  orderDate: datetime\n  total: string\n  totalAmount: number\n  originalTotal: string\n  originalTotalAmount: number\n  savings: number\n  currency: string\n  status: string\n  deliveryDate: datetime\n  eta: string\n  subtotal: number\n  tipAmount: number\n  deliveryFee: number\n  taxes: number\n  summary: string\n  fareBreakdown: json\n  deliveryInstructions: string\n  interactionType: string\n  orderUuid: string\n  body: text\n  head: text\n  messages: json\n  timeline: json\n  itemStates: json\n  latestArrival: datetime\n  progress: number\n  progressTotal: number\nrelations:\n  at: actor\n  contains: product[]\n  shippingAddress: place\n  store: place\n  delivery: trip\n  tracking: webpage\nprior_art:\n- source: schema.org/Order\n  url: https://schema.org/Order\n  notes: Our orderId = orderNumber; orderDate = orderDate; total = totalPaymentDue;\n    status = orderStatus; shippingAddress = orderDelivery.\n- source: schema.org/OrderStatus (enum)\n  url: https://schema.org/OrderStatus\n  notes: Our status values (placed, confirmed, delivering, completed, cancelled) map\n    to OrderProcessing/OrderInTransit/OrderDelivered/ OrderCancelled.\n- source: Amazon Order Reports (MWS / SP-API)\n  url: https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference\n  notes: Practical source. Our orderId, fareBreakdown, savings, eta are lifted from\n    Amazon/Uber Eats order structures.\n',
    'organization': 'plural: organizations\nidentity: url\ndisplay:\n  image: image\n  subtitle: industry\n  highlights:\n  - headquarters\nalso:\n- actor\nfields:\n  industry: string\nrelations:\n  member: person[]\n  domain: domain\n  website: website\n  headquarters: place\n  parentOrganization: organization\nprior_art:\n- source: schema.org/Organization\n  url: https://schema.org/Organization\n  notes: "Our industry \\u2248 naics/isicV4 (loosely); founded = foundingDate; member[]\\\n    \\ = member; headquarters = location; parentOrganization maps directly (schema.org\'s\\\n    \\ subOrganization is its declared inverse)."\n- source: vCard 4.0 KIND=org (RFC 6350)\n  url: https://datatracker.ietf.org/doc/html/rfc6350\n  notes: "Organization-as-contact. Our website/domain \\u2248 URL; headquarters \\u2248\\\n    \\ ADR. Thinner than schema.org for industry/founded."\n- source: Wikidata (Organization, Q43229)\n  url: https://www.wikidata.org/wiki/Q43229\n  notes: Cross-reference identity. Useful for deduping; no direct field alignment\n    but industry maps to P452 (industry) and founded to P571 (inception).\n',
    'pass': "plural: passes\nidentity:\n- at\n- id\nalso:\n- event\ndisplay:\n  subtitle: status\nfields:\n  status: string\n  quantity: integer\n  purchasedQuantity: integer\n  useCount: integer\n  isAllDayPass: boolean\n  price: number\n  currency: string\n  ticketNumber: string\n  nameOnTicket: string\n  seatAssignment: string\n  boardingGroup: string\n  ticketClass: string\n  gate: string\n  terminal: string\n  checkinStatus: string\nrelations:\n  at: actor\n  account: account\n  holder: person\n  grantedBy: membership\n  type: product\n  location: place\n  for: leg\n  reservation: reservation\nprior_art:\n- source: schema.org/Ticket\n  url: https://schema.org/Ticket\n  notes: schema.org's peer for a claim-check right-of-entry. Our purchasedDate = issuedAt;\n    holder = underName; price matches directly. Ticket is event-bound; we generalize\n    to any right-of-use.\n- source: Mindbody Services (pricing options)\n  url: https://developers.mindbodyonline.com/PublicDocumentation/V6\n  notes: Gym-industry reference. Our quantity/purchasedQuantity/ useCount/depletedDate\n    are lifted from Mindbody's ClientService.Remaining / Count / DateCompleted.\n- source: GTFS fare rules / IATA fare basis\n  url: https://gtfs.org/documentation/schedule/reference/#fare_productstxt\n  notes: 'Transit-pass vocabulary: single-ride, day-pass, period-pass all fit `isAllDayPass`\n    + `startEffectiveDate` + `endEffectiveDate`.'\n",
    'payment_method': 'plural: payment_methods\nidentity:\n- at\n- identifier\ndisplay:\n  subtitle: displayName\nfields:\n  identifier: string\n  type: string\n  subtype: string\n  brand: string\n  displayName: string\n  customDescription: string\n  holderName: string\n  last4: string\n  binRange: string\n  expMonth: integer\n  expYear: integer\n  expirationDate: string\n  currency: string\n  balance: number\n  fingerprint: string\n  isDefault: boolean\n  isPrimary: boolean\n  isExpired: boolean\n  isSelected: boolean\n  status: string\n  providerTokens: json\n  metadata: json\nrelations:\n  at: actor\n  account: account\n  holder: person\n  billingAddress: place\n  fundingAccount: financial_account\n  issuer: actor\n  membership: membership\nprior_art:\n- source: Stripe PaymentMethod API\n  url: https://docs.stripe.com/api/payment_methods/object\n  notes: "The gold standard. Our type/subtype \\u2248 Stripe\'s `type` + `card.brand`;\\\n    \\ last4/expMonth/expYear/fingerprint map 1:1 to `card.last4/exp_month/exp_year/fingerprint`.\\\n    \\ Stripe\'s billing_details is our `billingAddress` relation. Stripe\'s `pm_xxx`\\\n    \\ id is the canonical opaque handle."\n- source: PCI DSS v4.0 Requirement 3 (Protect Stored Account Data)\n  url: https://www.pcisecuritystandards.org/document_library/\n  notes: "Defines what\'s storable: PAN truncated, expiry, cardholder name, service\\\n    \\ code. FORBIDS full PAN (unencrypted), CVV/CVC2/CID, PIN/PIN block, track data.\\\n    \\ This shape carries only the permitted subset. Opaque tokens are NOT card data\\\n    \\ under PCI \\u2014 they\'re the merchant/provider\'s detokenization references;\\\n    \\ storing them is the recommended mitigation (Req. 3.5 tokenization)."\n- source: IATA Resolution 890 / PADIS Form-of-Payment codes\n  url: https://www.iata.org/en/publications/store/passenger-and-baggage-tariffs/\n  notes: \'Source for the airline 2-char `subtype` codes: AX (Amex), VI (Visa), MC\n    (MasterCard), DS (Discover), DC (Diners), TP (UATP), JC (JCB), UP (UnionPay).\n    These are the codes embedded in PNR FOP fields and EMD records. We keep them verbatim\n    so airline checkout round-trips work without translation.\'\n- source: W3C Payment Request API / Payment Method Identifiers\n  url: https://www.w3.org/TR/payment-method-id/\n  notes: "Browser-standard payment abstraction. `basic-card`, `https://apple.com/apple-pay`,\\\n    \\ `https://google.com/pay`, `https://paypal.com` are the method identifiers \\u2014\\\n    \\ our type/subtype combo is a normalized form."\n- source: Apple Pay Payment Token / Google Pay Network Token\n  url: https://developer.apple.com/documentation/passkit/apple_pay/payment_token_format_reference\n  notes: Device-bound token replaces the PAN on-chain. The DPAN and cryptogram live\n    in `providerTokens`; `last4` on the wallet surfaces the DEVICE last-4, not the\n    funding card\'s last-4.\n- source: schema.org/PaymentMethod + LoyaltyProgram\n  url: https://schema.org/PaymentMethod\n  notes: schema.org\'s PaymentMethod is a thin enum (CreditCard, Cash, PaymentCard,\n    ByInvoice). We extend it into a real shape with tokens and holder. Our `type`\n    overlaps its enumeration values.\n- source: PayPal Billing Agreements / Vault\n  url: https://developer.paypal.com/docs/multiparty/vault/\n  notes: "PayPal\'s saved-method pattern \\u2014 billingAgreementId is the opaque handle,\\\n    \\ used like our `providerTokens`. Payer given_name \\u2192 `holderName`. No last4\\\n    \\ (PayPal-as-wallet has no card number surface); our shape accommodates via nullable\\\n    \\ last4."\n- source: EMVCo Tokenisation Framework v2.0\n  url: https://www.emvco.com/specifications/payment-tokenisation/\n  notes: "Industry spec for network tokens (Visa Token Service, Mastercard MDES).\\\n    \\ Defines token requestor, token reference id, PAR (Payment Account Reference)\\\n    \\ \\u2014 PAR is the cross-token dedupe primitive our `fingerprint` field aligns\\\n    \\ with when the provider surfaces it."\n',
    'person': 'plural: people\nidentity_any:\n- url\ndisplay:\n  image: image\n  subtitle: about\n  highlights:\n  - born_in.startDate\n  - gender\n  body: notes\nalso:\n- actor\nfields:\n  url: string\n  givenName: string\n  additionalName: string\n  familyName: string\n  honorificPrefix: string\n  honorificSuffix: string\n  legalName: string\n  preferredName: string\n  maidenName: string\n  nickname: string\n  sortAs: string\n  nameOrder: string\n  phoneticGivenName: string\n  phoneticFamilyName: string\n  notes: text\n  gender: string\n  about: text\nrelations:\n  accounts: account[]\n  roles: role[]\n  memberships: membership[]\n  passes: pass[]\n  qualifications: qualification[]\n  practices: practice[]\n  website: website\nprior_art:\n- source: schema.org/Person\n  url: https://schema.org/Person\n  notes: "Our givenName / familyName / additionalName / honorificPrefix / honorificSuffix\\\n    \\ map directly. schema.org has no `middleName` (additionalName is the slot); no\\\n    \\ `firstName`/`lastName` either \\u2014 those are informal Wikipedia-style labels,\\\n    \\ not spec. about \\u2248 description. schema.org\'s `birthDate` lives on the `--born_in-->\\\n    \\ event(birth) { startDate }` relationship per rule 1, not as a flat field. `location`\\\n    \\ likewise \\u2014 dated `lived_at` edges per rule 3, not a single pointer. We\\\n    \\ diverge by modeling accounts[] as a first-class relation rather than sameAs\\\n    \\ URLs."\n- source: "vCard 4.0 (RFC 6350) \\xA76.2.2 N property + \\xA75.9 SORT-AS"\n  url: https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.2\n  notes: The N property is `family;given;additional;prefixes;suffixes`, each comma-multi-valued.\n    Our five structured fields round-trip exactly. sortAs mirrors RFC 6350\'s SORT-AS\n    parameter for particled surnames ("van der Harten" sorts under H).\n- source: Google People API Name resource\n  url: https://developers.google.com/people/api/rest/v1/people#Name\n  notes: Google uses givenName / familyName / middleName / honorificPrefix / honorificSuffix\n    + phoneticGivenName / phoneticFamilyName + displayName + unstructuredName. We\n    follow the same naming, using schema.org\'s `additionalName` where Google says\n    `middleName` (schema.org wins for multi-value support).\n- source: Apple CNContact\n  url: https://developer.apple.com/documentation/contacts/cncontact\n  notes: "Apple exposes givenName / middleName / familyName + phonetic* variants +\\\n    \\ nameSuffix / namePrefix + previousFamilyName (\\u2248 maidenName). Same shape\\\n    \\ as Google; reinforces the field set."\n- source: IATA PNR NM field + ICAO Doc 9303 (MRZ)\n  url: https://en.wikipedia.org/wiki/Machine-readable_passport\n  notes: Airline ticketing and passport MRZ require a specific string form (SURNAME/GIVENNAME\n    TITLE, all caps, Latin-only, diacritics stripped, 30-char limits). Structured\n    parts can\'t losslessly reconstruct this; we store it verbatim in `legalName`.\n- source: "W3C i18n \\u2014 Personal names around the world"\n  url: https://www.w3.org/International/questions/qa-personal-names\n  notes: Canonical reference for why "first/last" is a Western bias. CJK names put\n    family first. Spanish uses two surnames. Icelandic uses patronymics without family\n    names. The `nameOrder` field captures the rendering rule; structured fields stay\n    neutral.\n- source: FOAF (Friend of a Friend)\n  url: http://xmlns.com/foaf/spec/\n  notes: "Original social-graph vocabulary. foaf:Person with givenName/familyName/nick/homepage;\\\n    \\ foaf:account \\u2248 our accounts[]. Largely superseded by schema.org but still\\\n    \\ a reference for account-centric modeling."\n',
    'place': 'plural: places\nidentity_any:\n- googlePlaceId\n- mapboxId\ndisplay:\n  image: image\n  subtitle: featureType\n  highlights:\n  - city\n  - country\n  - rating\n  body: fullAddress\nfields:\n  fullAddress: string\n  placeFormatted: string\n  streetNumber: string\n  street: string\n  neighborhood: string\n  locality: string\n  city: string\n  district: string\n  region: string\n  postalCode: string\n  country: string\n  countryCode: string\n  latitude: number\n  longitude: number\n  accuracy: string\n  featureType: string\n  categories: string[]\n  phone: string\n  website: url\n  hours: json\n  businessStatus: string\n  rating: number\n  reviewCount: integer\n  priceLevel: string\n  timezone: string\n  eta: string\n  isOrderable: boolean\n  closedMessage: string\n  productCount: integer\n  mapboxId: string\n  wikidataId: string\n  googlePlaceId: string\nrelations:\n  at: actor\n  brand: organization\n  offers: product[]\nprior_art:\n- source: schema.org/Place + PostalAddress\n  url: https://schema.org/Place\n  notes: "Our latitude/longitude = geo.latitude/longitude; street/city/region/postalCode/countryCode\\\n    \\ map to PostalAddress streetAddress/addressLocality/addressRegion/postalCode/addressCountry;\\\n    \\ hours \\u2248 openingHoursSpecification; rating/reviewCount \\u2248 aggregateRating."\n- source: Google Places API (Place resource)\n  url: https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places\n  notes: "Practical POI schema. Our googlePlaceId = id; featureType/categories \\u2248\\\n    \\ types/primaryType; businessStatus, priceLevel, rating match directly."\n- source: GeoJSON (RFC 7946) + ISO 3166-1\n  url: https://datatracker.ietf.org/doc/html/rfc7946\n  notes: Our latitude/longitude are a GeoJSON Point [lon, lat]; countryCode follows\n    ISO 3166-1 alpha-2.\n',
    'playlist': 'plural: playlists\ndisplay:\n  subtitle: text\nalso:\n- list\nrelations:\n  contains: video[]\nprior_art:\n- source: schema.org/MusicPlaylist / ItemList\n  url: https://schema.org/MusicPlaylist\n  notes: "Our contains(video[]) \\u2248 track/itemListElement. We generalize beyond\\\n    \\ music to any ordered media list."\n- source: "YouTube Data API \\u2014 Playlist"\n  url: https://developers.google.com/youtube/v3/docs/playlists\n  notes: "Practical source. Playlist = ordered Video collection \\u2014 inherits list\\\n    \\ identity semantics."\n',
    'podcast': 'plural: podcasts\nidentity:\n- at\n- id\ndisplay:\n  subtitle: host\nfields:\n  feedUrl: url\nrelations:\n  host: person[]\n  at: actor\n  episode: episode[]\nprior_art:\n- source: RSS 2.0 (feed + channel)\n  url: https://www.rssboard.org/rss-specification\n  notes: "Our feedUrl is a canonical RSS feed URL; episodes relation \\u2248 channel\'s\\\n    \\ item elements."\n- source: Apple Podcasts RSS extensions (itunes:*)\n  url: https://help.apple.com/itc/podcasts_connect/#/itcb54353390\n  notes: "De-facto standard. Our host[] \\u2248 itunes:author; our series-episode hierarchy\\\n    \\ aligns with itunes:episode/itunes:season."\n- source: Podcast Namespace (podcast:*)\n  url: https://podcastindex.org/namespace/1.0\n  notes: Modern open extension. podcast:person covers guests/hosts; podcast:transcript\n    covers our transcribe relation.\n',
    'post': 'plural: posts\nidentity:\n- at\n- id\ndisplay:\n  subtitle: author\nfields:\n  externalUrl: url\n  postType: string\n  score: integer\n  commentCount: integer\n  community: string\nrelations:\n  at: actor\n  postedBy: account\n  publish: community\n  repliesTo: post\n  replies: post[]\n  contains: video[]\n  media: image[]\n  attachment: file[]\nprior_art:\n- source: ActivityStreams 2.0 (Note/Article + Create)\n  url: https://www.w3.org/TR/activitystreams-vocabulary/\n  notes: "Fediverse post model. Our postedBy \\u2248 actor/attributedTo; publish(community)\\\n    \\ \\u2248 audience/to; repliesTo/replies \\u2248 inReplyTo/replies; media/attachment\\\n    \\ \\u2248 attachment."\n- source: OpenGraph protocol\n  url: https://ogp.me/\n  notes: How posts surface when linked. Our externalUrl + media[] correspond to og:url\n    and og:image/og:video; postType loosely parallels og:type (article, video).\n- source: ATProto app.bsky.feed.post\n  url: https://atproto.com/lexicons/app-bsky-feed\n  notes: "Modern practical lexicon. Our repliesTo \\u2248 reply.parent; media \\u2248\\\n    \\ embed.images; externalUrl \\u2248 embed.external."\n',
    'practice': 'plural: practices\ndisplay:\n  subtitle: parent\nfields:\n  description: text\n  code: string\n  codeSystem: string\n  aliases: string[]\nrelations:\n  parent: practice\nprior_art:\n- source: NUCC Health Care Provider Taxonomy\n  url: https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40\n  notes: "US medical-specialty code set \\u2014 3 levels (Grouping / Classification\\\n    \\ / Specialization), 10-char alphanumeric codes. The source for codeSystem=NUCC\\\n    \\ and for the parent-edge hierarchy."\n- source: Standard Occupational Classification (SOC) / O*NET-SOC\n  url: https://www.bls.gov/soc/\n  notes: "US occupational taxonomy spanning every profession \\u2014 4 levels (Major\\\n    \\ / Minor / Broad / Detailed). codeSystem=SOC."\n- source: ISCED Fields of Education and Training 2013 (ISCED-F)\n  url: https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/international-standard-classification-education-fields-education-and\n  notes: "UNESCO field-of-study taxonomy \\u2014 3 levels (Broad / Narrow / Detailed).\\\n    \\ The field-of-study side, for a qualification\'s `field`."\n- source: schema.org CategoryCode / occupationalCategory\n  url: https://schema.org/occupationalCategory\n  notes: "schema.org has no dedicated discipline type \\u2014 only the pluggable CategoryCode\\\n    \\ (codeValue + inCodeSet). Confirms code + codeSystem as a loose optional pair,\\\n    \\ not a hard taxonomy dependency."\n',
    'product': 'plural: products\nidentity_any:\n- url\ndisplay:\n  subtitle: brand\nfields:\n  category: string\n  price: string\n  priceAmount: number\n  originalPrice: string\n  originalPriceAmount: number\n  currency: string\n  categories: string[]\n  availability: string\n  images: json\n  quantity: integer\n  weight: string\n  weightValue: number\n  weightUnit: string\n  soldByWeight: boolean\n  department: string\n  aisle: string\n  sku: string\n  barcode: string\n  nutritionScore: string\n  novaGroup: integer\n  calories: number\n  servingSize: string\n  customizationGroups: json\nrelations:\n  brand: brand\n  manufacturer: organization\n  creator: actor[]\n  inspiredBy: product[]\n  tagged: tag[]\nprior_art:\n- source: schema.org/Product + Offer\n  url: https://schema.org/Product\n  notes: Product on schema.org, price/priceAmount/currency/availability on nested\n    Offer. Our sku/barcode map to sku/gtin13/gtin12; brand/manufacturer match directly.\n    schema.org has `releaseDate` on Product (mirrors our `released`) but no formalized\n    end-of-life property.\n- source: Wikidata P2669 (discontinued date)\n  url: https://www.wikidata.org/wiki/Property:P2669\n  notes: "Wikidata\'s canonical \\"discontinued date\\" property \\u2014 broadly used\\\n    \\ across Wikidata\'s product entities (software, hardware, vehicles, consumer goods)\\\n    \\ with consistent semantics (\\"date when a product ceased to be manufactured,\\\n    \\ supported, or available\\"). Our `discontinued` field aligns directly. Wikidata\\\n    \\ P577 (publication date) similarly aligns with our `released`."\n- source: schema.org/CreativeWork (creator, isBasedOn)\n  url: https://schema.org/CreativeWork\n  notes: \'Our `creator: actor[]` mirrors schema.org/creator (Person|Organization).\n    Our `inspiredBy: product[]` maps to schema.org/isBasedOn (CreativeWork derivation/credit\n    edge); we keep the more readable name and broaden the target to any product so\n    non-CreativeWork lineages (one aircraft type inspired by another, one OS inspired\n    by another) work the same way.\'\n- source: GS1 GTIN (UPC/EAN)\n  url: https://www.gs1.org/standards/id-keys/gtin\n  notes: Canonical barcode standard. Our barcode field is a GTIN-8/12/13/14; GS1 also\n    underlies schema.org\'s gtin* properties.\n- source: Open Food Facts API\n  url: https://openfoodfacts.github.io/openfoodfacts-server/api/\n  notes: Best practical source for food attributes. Our nutritionScore/novaGroup/calories/servingSize\n    mirror nutriscore_grade/nova_group/nutriments.energy-kcal/serving_size.\n',
    'project': 'plural: projects\nidentity:\n- at\n- id\ndisplay:\n  subtitle: state\nfields:\n  state: string\n  color: string\n  parentId: string\nrelations:\n  at: actor\nprior_art:\n- source: "Linear API \\u2014 Project"\n  url: https://developers.linear.app/docs/graphql/working-with-the-graphql-api\n  notes: Our state/color come directly from Linear\'s Project model.\n- source: GitHub Projects (v2)\n  url: https://docs.github.com/en/graphql/reference/objects#projectv2\n  notes: "Canonical open-source project-board model. state \\u2248 ProjectV2SingleSelectFieldOption;\\\n    \\ color is per-field metadata."\n- source: schema.org/Project\n  url: https://schema.org/Project\n  notes: Generic project-as-effort type. Thinner than the practical APIs; mainly useful\n    for outbound JSON-LD.\n',
    'protocol': 'plural: protocols\nidentity:\n- name\ndisplay:\n  subtitle: name\nfields:\n  name: string\n  homepage: url\n  rfc: string\n  wikidataId: string\nprior_art:\n- source: schema.org/CreativeWork\n  url: https://schema.org/CreativeWork\n  notes: "Closest match in schema.org \\u2014 protocols are creative works in the broadest\\\n    \\ sense. We narrow to protocols and technical specifications used as identity\\\n    \\ namespaces."\n- source: Wikidata (Communication protocol, Q15836568)\n  url: https://www.wikidata.org/wiki/Q15836568\n  notes: wikidataId enables cross-reference for dedupe across other knowledge graphs.\n    Most well-known protocols have Q-IDs.\n- source: IANA Protocol Registry\n  url: https://www.iana.org/protocols\n  notes: Authoritative registry for many protocols. Our `name` aligns with IANA protocol\n    slugs where applicable.\n',
    'qualification': 'plural: qualifications\nidentity_any:\n- identifier\ndisplay:\n  subtitle: category\n  highlights:\n  - identifier\n  - validIn\n  - granted_by\nfields:\n  category: string\n  identifier: string\n  status: string\n  renewalPeriod: string\n  level: string\n  validIn: string\n  verificationUrl: url\nrelations:\n  held_by: person\n  granted_by: organization\n  governed_by: organization\n  field: practice\nprior_art:\n- source: schema.org EducationalOccupationalCredential\n  url: https://schema.org/EducationalOccupationalCredential\n  notes: "Single credential class with a credentialCategory discriminator; recognizedBy,\\\n    \\ validFor, validIn, educationalLevel. Person.hasCredential links the holder \\u2014\\\n    \\ our `held_by` edge."\n- source: "CTDL \\u2014 Credential Transparency Description Language (Credential Engine)"\n  url: https://credreg.net/ctdl/terms/CredentialType\n  notes: "The most thorough credential ontology \\u2014 a Credential superclass with\\\n    \\ ~40 subtypes and four distinct org roles (ownedBy / offeredBy vs accreditedBy\\\n    \\ / regulatedBy / recognizedBy). The source for splitting `granted_by` from `governed_by`;\\\n    \\ we collapse the regulator family into one edge \\u2014 four roles is over-modeled\\\n    \\ for a personal graph."\n- source: W3C Verifiable Credentials Data Model 2.0\n  url: https://www.w3.org/TR/vc-data-model-2.0/\n  notes: "Separates the issuer + validFrom / validUntil (the issuing act) from credentialSubject\\\n    \\ (the claim); credentialStatus models revocation \\u2014 our `status` covers revoked\\\n    \\ / suspended, which schema.org omits."\n- source: Open Badges 3.0 (1EdTech)\n  url: https://www.imsglobal.org/spec/ob/v3p0/impl\n  notes: "Achievement.achievementType enum (Certificate, Certification, Degree, License,\\\n    \\ Badge, MicroCredential) \\u2014 confirms one shape plus a category enum across\\\n    \\ every credential kind."\n- source: LinkedIn Licenses & Certifications\n  url: https://www.linkedin.com/help/linkedin/answer/a567169\n  notes: "Real-world minimal field set \\u2014 name, issuing organization, issue date,\\\n    \\ expiration date, credential ID, credential URL. Its Education / Licenses UI\\\n    \\ split is the seam this shape unifies."\n',
    'quantity-kind': 'plural: quantity-kinds\nidentity:\n- key\ndisplay:\n  subtitle: label\nfields:\n  key: string\n  label: string\nrelations:\n  dimension: dimension\n  parent: quantity-kind\nprior_art:\n- source: "ISO 80000-1 \\u2014 kind of quantity"\n  url: https://www.iso.org/standard/76921.html\n  notes: "ISO 80000 makes \\"kind of quantity\\" a rigorous first-class notion, distinct\\\n    \\ from dimension \\u2014 quantities of the same dimension are not necessarily of\\\n    \\ the same kind."\n- source: "QUDT \\u2014 QuantityKind"\n  url: https://www.qudt.org/doc/DOC_SCHEMA-QUDT.html\n  notes: qudt:QuantityKind is exactly this layer. Its hasDimensionVector property\n    corresponds to our `dimension` edge; QUDT\'s broader/ narrower kind hierarchy corresponds\n    to our `parent` edge.\n',
    'quote': 'plural: quotes\ndisplay:\n  subtitle: year\nfields:\n  context: string\n  year: integer\nprior_art:\n- source: schema.org/Quotation\n  url: https://schema.org/Quotation\n  notes: "Our context \\u2248 about; year \\u2248 datePublished. schema.org models spokenByCharacter/creator\\\n    \\ \\u2014 we model attribution via graph edges instead."\n- source: Wikiquote data model\n  url: https://en.wikiquote.org/wiki/Help:Sources\n  notes: Practical canonical quote source. Our provenance-via-edges (document --contains-->\n    quote --attributedTo--> person) matches Wikiquote\'s source-citation discipline.\n',
    'repository': 'plural: repositories\nidentity_any:\n- path\n- url\ndisplay:\n  subtitle: language\nfields:\n  stars: integer\n  forks: integer\n  language: string\n  topics: string[]\n  openIssues: integer\n  isArchived: boolean\n  isPrivate: boolean\n  defaultBranch: string\n  license: string\n  size: integer\nrelations:\n  forkedFrom: repository\n  owner: account\nprior_art:\n- source: Git internals + Git refs\n  url: https://git-scm.com/book/en/v2/Git-Internals-Git-References\n  notes: Our defaultBranch is a Git ref (refs/heads/main); forkedFrom is explicit\n    in our model vs. implicit in Git (recorded only by forges).\n- source: "GitHub REST API \\u2014 Repository"\n  url: https://docs.github.com/en/rest/repos/repos\n  notes: Direct source. Our stars/forks/openIssues/topics/defaultBranch/ license/size/isArchived/isPrivate\n    all come from the GitHub Repository resource.\n- source: SPDX License List\n  url: https://spdx.org/licenses/\n  notes: Our license values are SPDX identifiers (MIT, Apache-2.0, GPL-3.0-or-later).\n',
    'reservation': 'plural: reservations\nidentity:\n- at\n- reservationId\nalso:\n- event\ndisplay:\n  subtitle: reservationType\nfields:\n  reservationType: string\n  reservationId: string\n  status: string\n  bookingType: string\n  bookingTime: datetime\n  modifiedTime: datetime\n  startTime: datetime\n  endTime: datetime\n  partySize: integer\n  totalAmount: number\n  baseAmount: number\n  taxAmount: number\n  currency: string\n  checkinUrl: url\n  conditions: json\n  voidWindowEndsAt: datetime\n  availableActions: string[]\nrelations:\n  at: actor\n  trips: trip[]\n  location: place\n  event: event\n  passengers: person[]\n  underName: person\n  account: account\n  broker: actor\n  programMembership: membership\n  order: order\n  tickets: pass[]\n  derivedFrom: offer\nprior_art:\n- source: schema.org/Reservation\n  url: https://schema.org/Reservation\n  notes: "Base vocabulary: reservationFor, reservationId, reservationStatus, reservedTicket,\\\n    \\ underName, bookingTime, modifiedTime, totalPrice, priceCurrency. We fold FlightReservation\\\n    \\ / LodgingReservation / FoodEstablishmentReservation into a single shape with\\\n    \\ a reservationType discriminator (AgentOS convention \\u2014 see `trip.tripType`,\\\n    \\ `event.eventType`). Flight-specific fields (boardingGroup, seat) live on pass,\\\n    \\ not here."\n- source: schema.org/ReservationStatusType\n  url: https://schema.org/ReservationStatusType\n  notes: "Extended beyond schema.org\'s ConfirmedCancelledHoldPending set to add `no_show`\\\n    \\ and `completed` \\u2014 values that matter for post-hoc reasoning but schema.org\\\n    \\ lacks."\n- source: Duffel Orders API\n  url: https://duffel.com/docs/api/v2/orders\n  notes: Canonical flight-booking top-level entity. Our `reservationId` = booking_reference;\n    `availableActions` = available_actions; `voidWindowEndsAt` = void_window_ends_at;\n    `conditions` = conditions (change_before_departure, refund_before_departure).\n    Duffel names the entity `Order`; we chose `reservation` to free up `order` for\n    pure-commerce semantics.\n- source: IATA NDC OrderViewRS\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: "NDC normalizes passengers to a top-level PaxList referenced by ID. Our graph\\\n    \\ gets the same effect with `passengers: person[]` \\u2014 people are first-class\\\n    \\ nodes and the same `person` can appear on many reservations. Services (seat,\\\n    \\ baggage, meal) live on `pass`."\n- source: ActivityStreams 2.0 (Invite / Accept / Leave / Reject)\n  url: https://www.w3.org/TR/activitystreams-vocabulary/\n  notes: "Commitment lifecycle is an append-only stream of activities (booked, held,\\\n    \\ checked_in, rebooked, cancelled) rather than a single lossy enum. We use `status`\\\n    \\ for the snapshot and rely on back-edges from `activity` nodes for the history\\\n    \\ \\u2014 the same pattern FEP-8a8e recommends for ActivityPub event-side state."\n- source: FEP-8a8e Event interop\n  url: https://w3id.org/fep/8a8e\n  notes: Splits supply-side status (on the event/flight) from demand-side status (on\n    the attendee/passenger). We mirror this by keeping `status` on reservation (passenger-side)\n    separate from any cancellation/delay state on the `flight` or `trip` itself.\n- source: "Valueflows / REA \\u2014 Commitment"\n  url: https://www.valueflo.ws/concepts/flows/\n  notes: \'REA accounting framing: a reservation IS a commitment with provider, receiver,\n    resourceConformsTo, quantity, and time window. Useful lens for future extension\n    (hotel nights, car rental days).\'\n',
    'result': 'plural: results\ndisplay:\n  subtitle: url\nfields:\n  indexedAt: datetime\n  resultType: string\n  externalUrl: url\n  postId: string\n  score: integer\n  similarity: number\n  community: string\nprior_art:\n- source: OpenSearch Description Document\n  url: https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md\n  notes: "Result-pointer model: each hit has a URL + metadata. Our resultType \\u2248\\\n    \\ Url template\'s type attribute."\n- source: Web Search API conventions (Brave/Bing)\n  url: https://api.search.brave.com/app/documentation/web-search/get-started\n  notes: Practical source. Our indexedAt/resultType align with common fields across\n    Brave, Bing, and Exa web APIs.\n',
    'review': 'plural: reviews\ndisplay:\n  subtitle: author\nalso:\n- post\nfields:\n  rating: number\n  ratingMax: number\n  tags: string[]\n  isVerified: boolean\nrelations:\n  reviews: product\n  postedBy: account\nprior_art:\n- source: schema.org/Review\n  url: https://schema.org/Review\n  notes: "Our rating \\u2248 reviewRating.ratingValue; ratingMax \\u2248 bestRating;\\\n    \\ reviews = itemReviewed; isVerified has no direct property (extension)."\n- source: schema.org/AggregateRating\n  url: https://schema.org/AggregateRating\n  notes: For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating;\n    reviewCount is inherited when computed.\n',
    'role': 'plural: roles\nalso:\n- event\ndisplay:\n  subtitle: name\nfields:\n  title: string\n  department: string\n  roleType: string\nrelations:\n  person: person\n  organization: organization\nprior_art:\n- source: schema.org/Role + OrganizationRole\n  url: https://schema.org/OrganizationRole\n  notes: "Our title = roleName; startDate/endDate match; department \\u2248 name of\\\n    \\ a subOrganization; person/organization = Role\'s nested pattern."\n- source: FOAF + Bio vocabularies (position)\n  url: http://vocab.org/bio/0.1/.html\n  notes: "Period-of-employment modeling. Our startDate/endDate \\u2248 bio:date; roleType\\\n    \\ has no FOAF peer."\n',
    'seatmap': 'plural: seatmaps\nidentity:\n- id\ndisplay:\n  title: flightNumber\nfields:\n  flightNumber: string\n  origin: string\n  destination: string\n  fareBasisCode: string\n  classOfService: string\n  aircraftCode: string\n  totalSeats: integer\n  availableSeats: integer\n  cabins: json\n  tiers: json\n  hasExitRow: boolean\n  hasFreeSeats: boolean\n  hasPaidSeats: boolean\n  basicEconomyLocked: boolean\nrelations:\n  at: actor\n  flight: flight\n  aircraft: aircraft\n  reservation: reservation\n',
    'shelf': 'plural: shelves\ndisplay:\n  subtitle: isExclusive\nalso:\n- list\nfields:\n  isExclusive: boolean\nrelations:\n  contains: book[]\nprior_art:\n- source: "Goodreads API \\u2014 Shelves"\n  url: https://www.goodreads.com/api\n  notes: Direct source. Our isExclusive maps to Goodreads\' "exclusive shelves" (read,\n    to-read, currently-reading).\n- source: schema.org/ItemList (bookshelf)\n  url: https://schema.org/ItemList\n  notes: "Generic collection peer. contains(book[]) \\u2248 itemListElement."\n',
    'simulation': 'plural: simulations\ndisplay:\n  subtitle: status\nicon: shield\nfields:\n  status: string\n  profile: string\n  task: text\n  graphMode: string\n  startedAt: datetime\n  endedAt: datetime\n  actionCount: integer\n  writeCount: integer\nrelations:\n  primaryMemex: memex\n  mountedMemex: memex[]\n  agent: agent\n  tether: hardware\n  forkedFrom: simulation\n  startedBy: person\nprior_art:\n- source: OpenTelemetry Traces (root span + attributes)\n  url: https://opentelemetry.io/docs/concepts/signals/traces/\n  notes: "Span-shaped observation of an agent run. Our startedAt/endedAt/ actionCount/writeCount\\\n    \\ \\u2248 span attributes; status \\u2248 span status."\n- source: QEMU / VM snapshots\n  url: https://qemu-project.gitlab.io/qemu/system/images.html\n  notes: "\\"Disk image vs. VM\\" metaphor is direct. Our primaryMemex \\u2248 writable\\\n    \\ disk; mountedMemex[] \\u2248 read-only overlays; forkedFrom \\u2248 snapshot-based\\\n    \\ fork."\n- source: Kubernetes Pod + Volume mounts\n  url: https://kubernetes.io/docs/concepts/workloads/pods/\n  notes: "Our tether (hardware kill-switch) \\u2248 Pod security context; mountedMemex[]\\\n    \\ \\u2248 ConfigMap/PVC read-only mounts."\n',
    'skill': 'plural: skills\ndisplay:\n  subtitle: description\nfields:\n  skillId: string\n  description: text\n  color: string\n  status: string\n  error: text\nrelations:\n  website: website\n  privacyPolicy: webpage\n  termsOfService: webpage\nprior_art:\n- source: "Model Context Protocol (MCP) \\u2014 Server"\n  url: https://modelcontextprotocol.io/specification\n  notes: "Our skill = an MCP-registerable capability provider. skillId \\u2248 MCP\\\n    \\ server name; status tracks connection lifecycle."\n- source: OpenAPI 3.1 (Info + Servers)\n  url: https://spec.openapis.org/oas/v3.1.0\n  notes: "Our description/website/privacyPolicy/termsOfService \\u2248 OpenAPI info.description/info.termsOfService/info.license/contact."\n- source: Anthropic Tool Use (skills-as-tools)\n  url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use\n  notes: Each AgentOS skill publishes tools consumed via MCP/Tool-Use. status/error\n    surface tool-call health back to the agent.\n',
    'software': 'plural: software\nidentity_any:\n- url\ndisplay:\n  subtitle: applicationCategory\n  highlights:\n  - version\n  - runtimePlatform\nalso:\n- product\nfields:\n  version: string\n  applicationCategory: string\n  runtimePlatform: string\n  codename: string\nrelations:\n  manufacturer: organization\nprior_art:\n- source: schema.org/SoftwareApplication\n  url: https://schema.org/SoftwareApplication\n  notes: "Our applicationCategory mirrors schema.org applicationCategory (free-form\\\n    \\ string, common values include \\"GameApplication\\", \\"BusinessApplication\\",\\\n    \\ \\"BrowserApplication\\"). Our version maps to softwareVersion; runtimePlatform\\\n    \\ maps to operatingSystem (the closest analog \\u2014 schema.org uses `operatingSystem`\\\n    \\ to mean \\"which platform the software runs on\\", which matches our intent).\\\n    \\ Codename has no schema.org equivalent."\n- source: schema.org/SoftwareSourceCode\n  url: https://schema.org/SoftwareSourceCode\n  notes: For libraries / open-source code (XP.css, 98.css), schema.org has a separate\n    SoftwareSourceCode type with codeRepository / programmingLanguage fields. We keep\n    one `software` shape and let the product\'s url field carry the repo URL when applicable.\n- source: Wikidata Q7397 (software)\n  url: https://www.wikidata.org/wiki/Q7397\n  notes: "Wikidata software entities use P348 (software version identifier), P178\\\n    \\ (developer) \\u2248 our manufacturer/creator, P306 (operating system) \\u2248\\\n    \\ our runtimePlatform, and P2669 (discontinued date) \\u2014 inherited from product.\\\n    \\ Cross-reference identity rather than direct field alignment."\n',
    'sound': 'plural: sounds\nidentity_any:\n- url\ndisplay:\n  subtitle: purpose\nalso:\n- creative_work\n- file\nfields:\n  durationMs: integer\n  channels: integer\n  sampleRate: integer\n  bitDepth: integer\n  purpose: string\nprior_art:\n- source: schema.org/AudioObject\n  url: https://schema.org/AudioObject\n  notes: "Our durationMs \\u2248 duration (ISO 8601 period). Most metadata comes from\\\n    \\ creative_work via `also`; AudioObject\'s surface is sparse (contentUrl, encodingFormat,\\\n    \\ transcript)."\n- source: ID3v2 (audio metadata in MP3)\n  url: https://id3.org/id3v2.4.0-structure\n  notes: TPE1=artist (author via creative_work); TALB=album; TIT2=title (name via\n    creative_work); TYER=year (copyrightYear via creative_work); TCOP=copyright; TCOM=composer.\n- source: WAV LIST INFO chunks\n  url: https://www.recordingblogs.com/wiki/list-chunk-of-a-wave-file\n  notes: IART=artist; ICOP=copyright; ICRD=creation date; INAM=name; IGNR=genre. Inherited\n    from creative_work where they apply.\n- source: Broadcast Wave Format (BWF) bext chunk\n  url: https://tech.ebu.ch/docs/tech/tech3285.pdf\n  notes: "BWF carries Originator (creator), OriginationDate, OriginatorReference \\u2014\\\n    \\ production-pipeline provenance for broadcast audio. Inherited via creative_work;\\\n    \\ AgentOS doesn\'t currently parse bext chunks."\n',
    'source': 'plural: sources\nidentity: address\ndisplay:\n  subtitle: sourceId\nicon: "\\U0001F4E6"\nfields:\n  sourceId: string\n  address: string\n  scanner: string\n  enabled: boolean\n  description: text\n  lastSynced: datetime\nrelations:\n  folder: list\nprior_art:\n- source: Homebrew Taps\n  url: https://docs.brew.sh/Taps\n  notes: Direct precedent. Our sourceId/address match tap name/URL; our platform=agentos\n    parallels tap formulae discovery.\n- source: Cydia / Sileo (APT repos for iOS)\n  url: https://wiki.theapebox.com/index.php/Package_Management\n  notes: Namespaced third-party source model. Our sourceId prefix is the Cydia repo-namespace\n    pattern.\n- source: Debian APT sources.list\n  url: https://wiki.debian.org/SourcesList\n  notes: "Canonical third-party source mechanism. Our enabled flag parallels APT source\\\n    \\ enable/disable; lastSynced \\u2248 apt-get update timestamp."\n',
    'spec': 'plural: specs\ndisplay:\n  subtitle: state\nalso:\n- task\n- file\nfields:\n  problem: text\n  successCriteria: text\nrelations:\n  dependsOn: spec[]\n  supersedes: spec[]\nprior_art:\n- source: IETF RFC process\n  url: https://www.ietf.org/standards/rfcs/\n  notes: Canonical "design doc with problem statement and success criteria" lineage.\n    Our problem/successCriteria mirror the RFC structure.\n- source: Architectural Decision Records (ADR / MADR)\n  url: https://adr.github.io/\n  notes: Modern in-repo equivalent. supersedes[] matches ADR\'s "Supersedes" link;\n    dependsOn[] has no direct ADR peer.\n- source: Python PEP (spec-as-markdown)\n  url: https://peps.python.org/pep-0001/\n  notes: PEP states problem, rationale, spec, rejected alternatives. Our fields are\n    a slim version of the PEP template.\n',
    'tag': 'plural: tags\nidentity: name\ndisplay:\n  title: name\n  subtitle: tagType\nfields:\n  color: string\n  tagType: string\n  annotated: boolean\n  hash: string\nprior_art:\n- source: "GitHub REST API \\u2014 Labels"\n  url: https://docs.github.com/en/rest/issues/labels\n  notes: "Our color/name/tagType \\u2248 GitHub Label\'s color/name/default."\n- source: "Gmail API \\u2014 Labels"\n  url: https://developers.google.com/gmail/api/reference/rest/v1/users.labels\n  notes: Practical source. Our tagType distinguishes Gmail\'s SYSTEM vs USER label\n    types.\n- source: Dublin Core dc:subject\n  url: https://www.dublincore.org/specifications/dublin-core/dces/\n  notes: "Generic classification vocabulary \\u2014 tags on any resource."\n',
    'task': 'plural: tasks\nidentity:\n- at\n- id\nalso:\n- event\ndisplay:\n  subtitle: state\nfields:\n  remoteId: string\n  priority: integer\n  state: string\n  labels: string[]\n  targetDate: datetime\n  target: json\n  parentId: string\n  projectId: string\nrelations:\n  at: actor\n  assignedTo: person\n  project: project\n  repository: repository\n  parent: task\n  children: task[]\n  blockedBy: task[]\n  blocks: task[]\nprior_art:\n- source: "GitHub REST API \\u2014 Issues"\n  url: https://docs.github.com/en/rest/issues/issues\n  notes: Direct source. Our remoteId/state/labels/assignedTo/parent/ children/blockedBy/blocks\n    map to GitHub Issue + sub-issues + task-list tracking.\n- source: "Linear GraphQL API \\u2014 Issue"\n  url: https://developers.linear.app/docs/graphql/working-with-the-graphql-api\n  notes: Practical canonical. Our priority/state/project/targetDate align with Linear\'s\n    Issue model exactly.\n- source: "Todoist REST API v2 \\u2014 Tasks"\n  url: https://developer.todoist.com/rest/v2/\n  notes: "Consumer-grade task model. Our startedAt/targetDate \\u2248 created_at/due;\\\n    \\ labels match directly."\n',
    'tax_line': 'plural: tax_lines\nidentity:\n- at\n- id\ndisplay:\n  subtitle: description\nfields:\n  code: string\n  description: string\n  amount: number\n  currency: string\n  kind: string\n  nature: string\n  country: string\n  appliesToIndex: integer\n  refundable: boolean\n  merchantImposed: boolean\n  rate: number\n  taxableAmount: number\n  inclusive: boolean\nrelations:\n  at: actor\n  appliesTo: fare\n  offer: offer\n  reservation: reservation\n  segment: leg\n  imposedBy: actor\n  location: place\nprior_art:\n- source: IATA List of Ticket and Airport Taxes and Fees (ILTATF)\n  url: https://www.iata.org/en/publications/store/list-of-ticket-and-airport-taxes-and-fees/\n  notes: Canonical 1500+ entry registry of 2-char airline tax codes, grouped AT (airport),\n    PC (passenger charge), ST (stamp), TT (ticket), MT (misc). Our `code` = ILTATF\n    code when applicable; `nature` corresponds to ILTATF\'s grouping.\n- source: IATA NDC Tax / TaxBreakdown element\n  url: https://developer.iata.org/en/ndc/\n  notes: NDC\'s Price structure carries Taxes/Tax with TaxCode, CollectionPoint, CountryCode,\n    Nature, Amount, Description. Our code/country/nature/amount/description map 1:1.\n    NDC\'s Nature enum (security, fuel, facility, tax) informs our values.\n- source: schema.org/UnitPriceSpecification + PriceComponentTypeEnumeration\n  url: https://schema.org/UnitPriceSpecification\n  notes: Generic commerce. priceComponentType ("Tax"), valueAddedTaxIncluded (our\n    `inclusive`), priceCurrency. Lightweight; we add code, country, `imposedBy` to\n    cover the authority-chain gap.\n- source: "UBL 2.1 / Peppol BIS Billing 3.0 \\u2014 TaxSubtotal / TaxCategory"\n  url: https://docs.peppol.eu/poacc/billing/3.0/\n  notes: European eInvoicing. TaxSubtotal carries TaxableAmount, TaxAmount, Percent,\n    TaxCategory/TaxScheme (VAT/GST). Our taxableAmount/amount/rate/nature align directly.\n- source: Stripe Invoice tax_amounts[]\n  url: https://docs.stripe.com/api/invoices/object\n  notes: Stripe\'s line-item tax_amounts[] carries amount, inclusive, tax_rate, taxability_reason,\n    taxable_amount. Our inclusive/ rate/taxableAmount match; jurisdiction/jurisdiction_level\n    inspired the country + `imposedBy` split.\n- source: Shopify Order tax_lines[]\n  url: https://shopify.dev/docs/api/admin-rest/latest/resources/order\n  notes: "Minimal commerce model: price, rate, title, channel_liable. Our amount/rate/description\\\n    \\ map 1:1. Shopify allows multiple tax_lines per line item with same title + different\\\n    \\ rates \\u2014 same pattern we need (US Transportation Tax recurring per segment).\\\n    \\ We disambiguate via appliesToIndex."\n- source: Avalara / TaxJar tax breakdown\n  url: https://developer.avalara.com/\n  notes: \'Commerce tax engines. Jurisdiction hierarchy (country / state / county /\n    city / special) and combined tax rate. Informs the `imposedBy: actor` relation\n    for layered jurisdictions (hotel occupancy + tourism + state sales tax, each their\n    own line).\'\n',
    'theme': 'plural: themes\nidentity: themeId\ndisplay:\n  subtitle: family\nfields:\n  themeId: string\n  family: string\n  description: text\n  style: string\n  startMenu: string\n  defaultBackgroundColor: string\nrelations:\n  represents: product\nprior_art:\n- source: System theme APIs (macOS NSAppearance, Windows WinUI)\n  url: https://developer.apple.com/documentation/appkit/nsappearance\n  notes: OS-level theme abstraction. Our `family` parallels NSAppearance.Name (aqua,\n    darkAqua) and Windows theme families.\n',
    'tool_call': "plural: tool_calls\nidentity:\n- platform\n- id\ndisplay:\n  subtitle: name\nfields:\n  name: string\n  input: text\n  output: text\n  isError: boolean\n  durationMs: integer\nrelations:\n  platform: product\n  from: actor\n  inMessage: message\n  repliesTo: tool_call\nprior_art:\n- source: Anthropic Tool Use API\n  url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use\n  notes: Our name/input/output/isError map to tool_use/tool_result blocks in Claude's\n    message API.\n- source: OpenAI Function Calling / tool_calls\n  url: https://platform.openai.com/docs/guides/function-calling\n  notes: Our name/input = function.name/function.arguments; output is the tool-result\n    message content.\n- source: OpenTelemetry GenAI semconv\n  url: https://opentelemetry.io/docs/specs/semconv/gen-ai/\n  notes: Emerging observability standard. Our durationMs/isError align with gen_ai.tool.*\n    span attributes.\n",
    'transaction': 'plural: transactions\nidentity:\n- at\n- id\nalso:\n- event\ndisplay:\n  subtitle: category\n  highlights:\n  - amount\n  - postingDate\n  - currency\n  body: notes\nfields:\n  amount: number\n  currency: string\n  balance: number\n  category: string\n  postingDate: datetime\n  pending: boolean\n  recurring: boolean\n  notes: string\n  type: string\n  details: json\nrelations:\n  at: actor\n  account: financial_account\nprior_art:\n- source: OFX (Open Financial Exchange) STMTTRN\n  url: https://financialdataexchange.org/ofx\n  notes: Direct source. Our amount/type/postingDate/balance map to STMTTRN TRNAMT/TRNTYPE/DTPOSTED/BALAMT.\n- source: ISO 20022 payments messaging\n  url: https://www.iso20022.org/\n  notes: "Modern bank-messaging. Our currency = Ccy; category \\u2248 purpose code;\\\n    \\ details \\u2248 RemittanceInformation."\n- source: Plaid Transactions API\n  url: https://plaid.com/docs/api/products/transactions/\n  notes: Practical mirror. Our category/pending/recurring/notes match Plaid\'s category/pending/personal_finance_category/name\n    fields.\n',
    'transcript': 'plural: transcripts\ndisplay:\n  subtitle: language\nfields:\n  language: string\n  sourceType: string\n  contentRole: string\n  durationMs: integer\n  segmentCount: integer\n  segments: json\nprior_art:\n- source: WebVTT (W3C)\n  url: https://www.w3.org/TR/webvtt1/\n  notes: Our segments are WebVTT cues (start/end/text). language follows WebVTT\'s\n    LANGUAGE header.\n- source: SRT SubRip Subtitles\n  url: https://matroska.org/technical/subtitles.html#srt-subtitles\n  notes: Practical alternative cue format. Same segment shape.\n- source: Whisper JSON output\n  url: https://github.com/openai/whisper\n  notes: "Practical source \\u2014 many transcript skills return Whisper-shaped JSON\\\n    \\ (segments with start/end/text). Direct match."\n',
    'transition': 'plural: transitions\nalso:\n- event\ndisplay:\n  subtitle: startDate\n  highlights:\n  - startDate\n  - givenName\n  - familyName\n  - gender\nfields:\n  givenName: string\n  additionalName: string\n  familyName: string\n  honorificPrefix: string\n  honorificSuffix: string\n  legalName: string\n  maidenName: string\n  sortAs: string\n  nameOrder: string\n  phoneticGivenName: string\n  phoneticFamilyName: string\n  gender: string\n  nickname: string\nprior_art:\n- source: Event Sourcing (Fowler)\n  url: https://martinfowler.com/eaaDev/EventSourcing.html\n  notes: "Past-tense events as facts; entity state = fold over the event stream. `transition`\\\n    \\ is the past-tense event-node; the `latest:` resolver is the fold. Reuses canonical\\\n    \\ field names \\u2014 no `new_*` prefix per the event-sourcing convention."\n- source: "Palantir Foundry \\u2014 Action Log Objects"\n  url: https://www.palantir.com/docs/foundry/announcements/2022-10/index.html\n  notes: "Palantir reifies every mutation as a queryable Action Log Object \\u2014\\\n    \\ same shape as our reified `transition` event. They type Actions per-mutation\\\n    \\ (`AssignEmployee` etc.); we collapse to one umbrella shape with optional fields\\\n    \\ for agent-OS ergonomics (operations not known in advance)."\n- source: "IMO / GISIS maritime registry \\u2014 particulars change"\n  url: https://gisis.imo.org/public/default.aspx\n  notes: "50-year-old domain proves the pattern: stable identifier (IMO number) +\\\n    \\ canonical property names + reified change events (name/flag/owner change). `Person.id`\\\n    \\ \\u2194 `Ship.imo`; `transition.gender` \\u2194 a `flag_change` on a ship."\n- source: FHIR R5 HumanName.use + HumanName.period\n  url: https://hl7.org/fhir/datatypes.html#HumanName\n  notes: FHIR encodes dated names via multi-value on the Patient (no event-node).\n    We lift the same pattern to an event-node because the change has its own date\n    + place + authority context worth capturing as a first-class graph entity.\n- source: Wikidata P735/P734/P21 + P580/P582 qualifiers\n  url: https://www.wikidata.org/wiki/Property:P735\n  notes: Property statements with start-time/end-time qualifiers. Validates "reuse\n    canonical field name + date positions in time".\n',
    'trip': 'plural: trips\nidentity:\n- at\n- id\nalso:\n- event\ndisplay:\n  subtitle: tripType\nfields:\n  tripType: string\n  status: string\n  departureTime: datetime\n  arrivalTime: datetime\n  duration: string\n  durationMinutes: integer\n  distance: string\n  vehicleType: string\n  cabinClass: string\n  fare: string\n  fareAmount: number\n  currency: string\n  rating: string\n  trackingUrl: url\n  isSurge: boolean\n  isScheduled: boolean\n  stops: integer\n  bookingToken: string\n  carbonEmissions: json\n  isPool: boolean\n  isReserve: boolean\n  guest: json\n  marketplace: string\n  vehicle: json\nrelations:\n  at: actor\n  origin: place\n  destination: place\n  legs: leg[]\n  carrier: organization\n  driver: person\n  order: order\nprior_art:\n- source: schema.org/Trip + subTrip\n  url: https://schema.org/Trip\n  notes: "Our origin/destination/departureTime/arrivalTime map exactly; legs[] \\u2248\\\n    \\ subTrip or itinerary."\n- source: IATA NDC Slice (airline itineraries)\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: NDC slice = our trip; NDC segment = our leg. cabinClass, bookingToken come\n    from NDC offer items.\n- source: "Uber API \\u2014 Trip resource"\n  url: https://developer.uber.com/docs/riders/references/api\n  notes: Practical source for ride trips. Our fare/fareAmount/ trackingUrl/isSurge/isScheduled\n    lifted from Uber\'s Trip model.\n',
    'unit': 'plural: units\nidentity_any:\n- ucumCode\n- siDigitalFrameworkUri\n- iso4217\ndisplay:\n  subtitle: symbol\nfields:\n  ucumCode: string\n  symbol: string\n  label: string\n  kind: string\n  siDigitalFrameworkUri: string\n  unCefactCommonCode: string\n  qudtUnitIri: string\n  wikidataId: string\n  toBaseFactor: number\n  toBaseOffset: number\n  iso4217: string\n  iso4217Numeric: string\n  minorExponent: integer\n  logBase: number\nrelations:\n  dimension: dimension\n  quantityKinds: quantity-kind[]\nprior_art:\n- source: "UCUM \\u2014 Unified Code for Units of Measure"\n  url: https://ucum.org/ucum\n  notes: "ucumCode is the primary working identity \\u2014 case-sensitive variant (mg\\\n    \\ is not MG; h hour is not H henry). Compositional, and the de-facto healthcare\\\n    \\ standard (FHIR Quantity mandates it, LOINC and HL7 use it). Machine-readable\\\n    \\ database: ucum-essence.xml."\n- source: "BIPM \\u2014 SI Digital Framework / SI Reference Point"\n  url: https://www.si-digital-framework.org/\n  notes: "Launched March 2024 by the BIPM CIPM Task Group on the Digital SI. Publishes\\\n    \\ resolvable persistent URIs for SI units, prefixes, and defining constants (base\\\n    \\ namespace si-digital-framework.org/SI/ units/), served as TTL plus a JSON/XML\\\n    \\ API. The most authoritative source for SI units \\u2014 treaty-level. siDigitalFrameworkUri\\\n    \\ carries it; null for non-SI units, and that null is meaningful."\n- source: "UN/CEFACT Recommendation 20 \\u2014 Codes for Units of Measure Used in International\\\n    \\ Trade"\n  url: https://unece.org/trade/uncefact/cl-recommendations\n  notes: "Around 700 short codes (KGM kilogram, MTR metre, LTR litre, CEL degree Celsius).\\\n    \\ Rev 17 (2021), freely downloadable as XLSX or genericode XML. schema.org\'s unitCode\\\n    \\ property uses exactly these codes \\u2014 unCefactCommonCode is the interop join\\\n    \\ key."\n- source: "QUDT \\u2014 Quantities, Units, Dimensions and Types"\n  url: https://www.qudt.org/doc/DOC_VOCAB-UNITS.html\n  notes: "qudtUnitIri cross-references QUDT, itself a cross-reference hub (QUDT units\\\n    \\ carry qudt:ucumCode, qudt:uneceCommonCode, qudt:wikidataMatch). toBaseFactor/toBaseOffset\\\n    \\ correspond to qudt:conversionMultiplier / conversionOffset; kind=currency corresponds\\\n    \\ to qudt:CurrencyUnit, which also carries NO conversion multiplier \\u2014 FX\\\n    \\ is external."\n- source: Wikidata\n  url: https://www.wikidata.org/wiki/Q11570\n  notes: "wikidataId (kilogram = Q11570) is a universal glue identifier \\u2014 links\\\n    \\ to every Wikipedia language edition and many external databases. Free SPARQL\\\n    \\ endpoint plus dumps."\n- source: "ISO 4217 \\u2014 Currency codes"\n  url: https://www.iso.org/iso-4217-currency-codes.html\n  notes: "iso4217 (alpha) plus iso4217Numeric and minorExponent for currency units.\\\n    \\ ISO 4217 IS the authoritative currency-code registry \\u2014 notably, currency\\\n    \\ is the ONE unit family with a single authoritative code system; physical units\\\n    \\ have none."\n- source: "schema.org \\u2014 unitCode"\n  url: https://schema.org/unitCode\n  notes: Precedent that the minimum unit model is (value, unitCode), and that unitCode\n    in practice means a UN/CEFACT Rec 20 code.\n- source: "NIST SP 811 / SP 330 \\u2014 and why NIST is NOT a field"\n  url: https://www.nist.gov/pml/special-publication-811\n  notes: "Recorded deliberately. NIST publishes SI usage guidance (SP 811) and the\\\n    \\ US edition of the SI Brochure (SP 330) \\u2014 prose only. NIST assigns no unit\\\n    \\ codes and maintains no unit registry; there is nothing to cross-reference, so\\\n    \\ no NIST field exists on this shape. Same for ISO 80000 \\u2014 it defines units\\\n    \\ in prose and assigns no codes."\n',
    'user': 'plural: users\ndisplay:\n  subtitle: name\nalso:\n- actor\nidentity_any:\n- osUsername\nfields:\n  osUsername: string\n  primaryUser: boolean\nrelations:\n  identified_as: person\nprefsSchemas:\n  ui:\n  - key: themeId\n    kind: select\n    label: Theme\n    description: "Desktop theme \\u2014 window chrome, fonts, sounds."\n    group: Theme\n    optionsShape: theme\n    optionsValue: themeId\n    optionsLabel: name\n  - key: fontSize\n    kind: number\n    label: Font Size\n    description: Base UI font size in pixels.\n    group: Fonts\n    tab: Fonts\n    min: 8\n    max: 20\n    step: 1\n    default: 12\n  - key: background.color\n    kind: color\n    label: Background Color\n    description: Solid background tone for this view.\n    group: Background\n    tab: Background\n    default: \'#3A6EA5\'\n  - key: background.position\n    kind: select\n    label: Position\n    description: How the wallpaper fills the surface.\n    group: Background\n    tab: Background\n    default: fill\n    options:\n    - value: fill\n      label: Fill\n    - value: fit\n      label: Fit\n    - value: stretch\n      label: Stretch\n    - value: center\n      label: Center\n    - value: tile\n      label: Tile\n  - key: icons.iconSize\n    kind: number\n    label: Icon Size\n    description: Icon side length in pixels.\n    group: Icons\n    tab: Icons\n    min: 24\n    max: 96\n    step: 4\n    default: 32\n  - key: icons.iconSpacing\n    kind: number\n    label: Icon Spacing\n    description: Pixels between icon cells.\n    group: Icons\n    tab: Icons\n    min: 4\n    max: 48\n    step: 2\n    default: 8\n  - key: icons.showIcons\n    kind: boolean\n    label: Show Icons\n    description: Render icons on this view.\n    group: Icons\n    tab: Icons\n    default: true\n  - key: icons.startingCorner\n    kind: select\n    label: Starting Corner\n    description: Where the first icon lands.\n    group: Icons\n    tab: Icons\n    default: top-left\n    options:\n    - value: top-left\n      label: Top Left\n    - value: top-right\n      label: Top Right\n    - value: bottom-left\n      label: Bottom Left\n    - value: bottom-right\n      label: Bottom Right\n  - key: icons.flowDirection\n    kind: select\n    label: Flow Direction\n    description: Whether icons fill columns or rows first.\n    group: Icons\n    tab: Icons\n    default: vertical-first\n    options:\n    - value: vertical-first\n      label: Vertical First\n    - value: horizontal-first\n      label: Horizontal First\nprior_art:\n- source: POSIX getpwuid (passwd database)\n  url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/getpwuid.html\n  notes: "The OS-level \\"user\\" \\u2014 uid + login name + home dir. Our `osUsername`\\\n    \\ mirrors `pw_name`; identity-by-OS-account follows the same pattern. We diverge\\\n    \\ by separating the OS seat (`user`) from the human (`person`); POSIX conflates\\\n    \\ them."\n- source: schema.org/Audience\n  url: https://schema.org/Audience\n  notes: "Loose fit. schema.org has no \\"OS user\\" concept \\u2014 user accounts are\\\n    \\ product-specific. We model it explicitly because AgentOS is the product, and\\\n    \\ the user-as-pref-carrier is load-bearing."\n- source: macOS NSUserDefaults\n  url: https://developer.apple.com/documentation/foundation/nsuserdefaults\n  notes: \'The Apple model: per-user preference store, keyed by the OS account. Our\n    `pref:ui` / `pref:system` blobs play the same role, but live in the graph (queryable,\n    multi-process safe) rather than a plist file.\'\n',
    'video': 'plural: videos\ndisplay:\n  subtitle: author\nalso:\n- creative_work\n- file\nfields:\n  durationMs: integer\n  resolution: string\n  frameRate: number\n  codec: string\n  viewCount: integer\nrelations:\n  channel: channel\n  transcribe: transcript\n  addTo: playlist\nprior_art:\n- source: schema.org/VideoObject\n  url: https://schema.org/VideoObject\n  notes: "Our durationMs \\u2248 duration (ISO 8601 period); resolution \\u2248 videoFrameSize;\\\n    \\ frameRate has no direct property; codec \\u2248 encodingFormat."\n- source: IANA Media Types (video/*)\n  url: https://www.iana.org/assignments/media-types/media-types.xhtml#video\n  notes: Our codec values map to registered video/* media types (mp4, webm, ogg).\n- source: MPEG / ITU video codec specs\n  url: https://www.itu.int/rec/T-REC-H.264\n  notes: Canonical codec definitions. Our codec values are MPEG/ITU codec short names\n    (h264, vp9, av1).\n',
    'webpage': 'plural: webpages\nidentity: url\ndisplay:\n  subtitle: url\nfields:\n  visitCount: integer\n  lastVisitUnix: integer\n  contentType: string\n  error: string\nprior_art:\n- source: schema.org/WebPage\n  url: https://schema.org/WebPage\n  notes: "Our URL-as-identity matches schema.org\'s @id/url convention; contentType\\\n    \\ \\u2248 encodingFormat."\n- source: HTTP semantics (RFC 9110)\n  url: https://datatracker.ietf.org/doc/html/rfc9110\n  notes: "Our contentType is the Content-Type response header; error \\u2248 non-2xx\\\n    \\ status text."\n- source: Chrome history / WebExtensions History API\n  url: https://developer.chrome.com/docs/extensions/reference/api/history\n  notes: Practical source. Our visitCount/lastVisitUnix lift from the history API\'s\n    VisitItem structure.\n',
    'website': 'plural: websites\nidentity: url\ndisplay:\n  subtitle: url\nfields:\n  status: string\n  versionId: string\n  anonymous: boolean\n  claimToken: string\n  claimUrl: url\nrelations:\n  domain: domain\n  ownedBy: organization\nprior_art:\n- source: schema.org/WebSite\n  url: https://schema.org/WebSite\n  notes: "Our url-as-identity matches; ownedBy \\u2248 publisher; domain relation \\u2248\\\n    \\ url host."\n- source: WHOIS (RFC 3912)\n  url: https://datatracker.ietf.org/doc/html/rfc3912\n  notes: Our expiresAt/domain source from WHOIS records; claimToken has no direct\n    WHOIS peer (HERE.NOW-specific).\n- source: RFC 7033 WebFinger (host-meta)\n  url: https://datatracker.ietf.org/doc/html/rfc7033\n  notes: Website metadata discovery. Our claimUrl parallels /.well-known/host-meta\n    patterns.\n',
}

# Identity keys per shape — sidecars for the skill worker.
SHAPE_IDENTITIES: dict[str, list[str]] = {
    'account': ['at', 'identifier'],
    'aircraft': ['icaoCode'],
    'airline': ['iataCode'],
    'airport': ['iataCode'],
    'app': ['id'],
    'booking_offer': ['at', 'cartId'],
    'bookmark': ['target'],
    'brand': ['url'],
    'calendar': ['at', 'calendarId'],
    'channel': ['at', 'id'],
    'community': ['at', 'id'],
    'conversation': ['at', 'id'],
    'credential': ['domain', 'identifier', 'itemType'],
    'dimension': ['key'],
    'dns_record': ['domain', 'recordType', 'recordName'],
    'domain': ['name'],
    'email': ['at', 'id'],
    'event': ['at', 'id'],
    'fare': ['at', 'identifier'],
    'financial_account': ['at', 'identifier'],
    'group': ['at', 'id'],
    'hardware': ['serialNumber'],
    'health-reference-range': ['analyte', 'issuingLab', 'method', 'startDate'],
    'invitation': ['at', 'id'],
    'list': ['at', 'id'],
    'mcp_session': ['client', 'projectId', 'gitBranch'],
    'membership': ['at', 'id'],
    'message': ['at', 'id'],
    'model': ['at', 'name'],
    'offer': ['id'],
    'order': ['at', 'orderId'],
    'organization': ['url'],
    'pass': ['at', 'id'],
    'payment_method': ['at', 'identifier'],
    'podcast': ['at', 'id'],
    'post': ['at', 'id'],
    'project': ['at', 'id'],
    'protocol': ['name'],
    'quantity-kind': ['key'],
    'reservation': ['at', 'reservationId'],
    'seatmap': ['id'],
    'source': ['address'],
    'tag': ['name'],
    'task': ['at', 'id'],
    'tax_line': ['at', 'id'],
    'theme': ['themeId'],
    'tool_call': ['platform', 'id'],
    'transaction': ['at', 'id'],
    'trip': ['at', 'id'],
    'webpage': ['url'],
    'website': ['url'],
}

SHAPE_IDENTITIES_ANY: dict[str, list[str]] = {
    'book': ['isbn13', 'isbn'],
    'font': ['family', 'postscriptName'],
    'health-biomarker': ['loincCode', 'measure'],
    'health-condition': ['snomedCode', 'name'],
    'health-lab': ['cliaNumber', 'url'],
    'health-procedure': ['cptCode', 'snomedCode', 'id'],
    'icon': ['component', 'url'],
    'image': ['url'],
    'intellectual_property': ['identifier'],
    'person': ['url'],
    'place': ['googlePlaceId', 'mapboxId'],
    'product': ['url'],
    'qualification': ['identifier'],
    'repository': ['path', 'url'],
    'software': ['url'],
    'sound': ['url'],
    'unit': ['ucumCode', 'siDigitalFrameworkUri', 'iso4217'],
    'user': ['osUsername'],
}

# YAML declaration order per shape — author order is meaning.
SHAPE_FIELD_ORDER: dict[str, list[str]] = {
    'account': ['identifier', 'handle', 'displayName', 'display', 'email', 'phone', 'bio', 'accountType', 'color', 'isActive', 'joinedDate', 'lastActive', 'lastProfileFetch', 'userId', 'issuer', 'metadata'],
    'activity': ['action', 'changedKeys', 'toolName', 'duration', 'success', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'actor': ['actorType'],
    'agent': ['model', 'provider', 'sessionId', 'actorType'],
    'aircraft': ['model', 'variant', 'seatCapacity', 'rangeKm', 'iataCode', 'icaoCode', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'airline': ['iataCode', 'icaoCode', 'callsign', 'country', 'alliance', 'industry', 'actorType'],
    'airport': ['iataCode', 'icaoCode', 'city', 'country', 'countryCode', 'timezone', 'elevationFt', 'terminalCount'],
    'app': ['id', 'name', 'iconRole', 'route', 'defaultView', 'isSystem', 'handles'],
    'birth': ['givenName', 'additionalName', 'familyName', 'honorificPrefix', 'honorificSuffix', 'legalName', 'maidenName', 'sortAs', 'nameOrder', 'phoneticGivenName', 'phoneticFamilyName', 'gender', 'nickname', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'book': ['isbn', 'isbn13', 'pages', 'genres', 'series', 'format', 'language', 'originalTitle', 'places', 'characters', 'awardsWon', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'coverage', 'tags', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'booking_offer': ['cartId', 'referenceNumber', 'status', 'preparedAt', 'presentedAt', 'approvedAt', 'expiresAt', 'currency', 'baseAmount', 'taxAmount', 'feesAmount', 'totalAmount', 'itineraryHash', 'signature', 'signatureAlg', 'signedBy', 'checkoutUrl', 'confirmEndpoint', 'isRefundable', 'isChangeable', 'hasVoidWindow', 'voidWindowEndsAt', 'conditions', 'blob', 'review', 'contactEmail', 'contactPhone', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'bookmark': ['name'],
    'branch': ['commit', 'upstream', 'ahead', 'behind', 'isCurrent', 'isRemote'],
    'brand': ['tagline', 'country', 'primaryColor', 'textColor'],
    'calendar': ['calendarId', 'color', 'backgroundColor', 'foregroundColor', 'isPrimary', 'isReadonly', 'accessRole', 'source', 'timezone'],
    'channel': ['banner', 'subscriberCount'],
    'class': ['activityType', 'capacity', 'spotsRemaining', 'isFull', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'community': ['privacy', 'memberCount', 'subscriberCount', 'allowCrypto'],
    'conversation': ['isGroup', 'isArchived', 'unreadCount', 'messageCount', 'accountEmail', 'historyId', 'source', 'cwd', 'gitBranch'],
    'conversion': ['kind', 'factor', 'rate', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'creative_work': ['name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags'],
    'credential': ['domain', 'identifier', 'itemType', 'source', 'obtainedAt', 'lastVerified', 'refreshable', 'storeRowId'],
    'dimension': ['key', 'label', 'length', 'mass', 'time', 'current', 'temperature', 'amount', 'luminous', 'dimensionless'],
    'dns_record': ['domain', 'recordName', 'recordType', 'type', 'ttl', 'priority', 'recordId', 'values'],
    'document': ['contentType', 'language', 'wordCount', 'abstract', 'tableOfContents', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'domain': ['status', 'registrar', 'autoRenew', 'nameservers'],
    'email': ['subject', 'messageId', 'inReplyTo', 'isUnread', 'isStarred', 'isDraft', 'isSent', 'isTrash', 'isSpam', 'hasAttachments', 'draftId', 'conversationId', 'accountEmail', 'sizeEstimate', 'references', 'replyTo', 'deliveredTo', 'attachments', 'toRaw', 'ccRaw', 'bccRaw', 'unsubscribe', 'unsubscribeOneClick', 'manageSubscription', 'listId', 'isAutomated', 'precedence', 'mailer', 'returnPath', 'authResults', 'bodyHtml', 'isOutgoing'],
    'episode': ['durationMs', 'episodeNumber', 'seasonNumber'],
    'event': ['startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'fare': ['identifier', 'bookingCode', 'productType', 'fareFamily', 'class', 'basePrice', 'currency', 'passengerType', 'milesEarned', 'pointsEarned', 'components', 'refundable', 'changeable', 'restrictions', 'conditions'],
    'file': ['filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'financial_account': ['identifier', 'accountId', 'accountNumber', 'routingNumber', 'last4', 'currency', 'accountType', 'balance', 'available', 'creditLimit', 'minimumPayment', 'cardType', 'interestRate'],
    'flight': ['flightNumber', 'durationMinutes', 'cabinClass', 'stops', 'carbonEmissions', 'sequence', 'departureTime', 'arrivalTime', 'duration', 'vehicleType', 'layoverMinutes', 'trace', 'tracePointCount', 'polyline', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'font': ['family', 'genericFamily', 'postscriptName', 'weights', 'styles', 'formats', 'scripts', 'glyphCount', 'designerUrl', 'vendorUrl', 'licenseInfoUrl', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags'],
    'git_commit': ['sha', 'shortHash', 'message', 'additions', 'deletions', 'filesChanged', 'committedAt', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'group': ['memberCount', 'category'],
    'hardware': ['modelNumber', 'serialNumber', 'specs', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'health-biomarker': ['measure', 'category', 'loincCode', 'analyteType', 'description'],
    'health-condition': ['clinicalStatus', 'verificationStatus', 'proximity', 'bodySite', 'severity', 'snomedCode', 'icd10Code', 'clinicalArea', 'mitigation'],
    'health-immunization': ['dateAdministered', 'cvxCode', 'manufacturer', 'lotNumber', 'doseNumber', 'seriesDoses', 'site', 'route', 'diseaseTarget', 'notes', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-lab': ['cliaNumber', 'npi', 'ccn', 'labType', 'accreditation', 'industry', 'actorType'],
    'health-observation': ['value', 'valueText', 'refLow', 'refHigh', 'refText', 'flag', 'status', 'notes', 'indexedAt', 'resultType', 'externalUrl', 'postId', 'score', 'similarity', 'community', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-panel': ['panelCode', 'fasting', 'description', 'id', 'listId', 'listType', 'ordering_mode', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'default_view', 'icon_size', 'sort_by', 'path', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-procedure': ['performedDate', 'procedureType', 'bodySite', 'outcome', 'status', 'cptCode', 'snomedCode', 'findings', 'followUp', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-reference-range': ['low', 'high', 'unit', 'refText', 'category', 'provenance', 'method', 'ageLow', 'ageHigh', 'sex', 'pregnancy', 'gestationalAge', 'fasting', 'timeOfDay', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'icon': ['dimension', 'format', 'url', 'component', 'purpose', 'style', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'language', 'coverage', 'tags'],
    'image': ['width', 'height', 'format', 'altText', 'appName', 'windowId', 'displayId', 'displayIndex', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'encoding', 'lineCount', 'kind', 'sha'],
    'intellectual_property': ['category', 'mark', 'identifier', 'register', 'status', 'filingBasis', 'niceClass', 'validIn', 'renewalPeriod', 'verificationUrl'],
    'invitation': ['invitationType', 'email', 'role', 'status', 'token', 'acceptedAt', 'revokedAt', 'message', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'launch': ['flightNumber', 'rocketId', 'launchpadId', 'crewIds', 'reusedBoosters', 'landingOutcomes', 'articleUrl', 'webcastUrl', 'wikipediaUrl', 'patchImage', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'leg': ['sequence', 'departureTime', 'arrivalTime', 'duration', 'durationMinutes', 'flightNumber', 'cabinClass', 'vehicleType', 'layoverMinutes', 'carbonEmissions', 'trace', 'tracePointCount', 'polyline', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'list': ['id', 'listId', 'listType', 'ordering_mode', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'default_view', 'icon_size', 'sort_by', 'path'],
    'loaded_model': ['size', 'quantization', 'vramUsage', 'sizeVram', 'digest', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'mcp_session': ['client', 'projectId', 'gitBranch', 'sessionType', 'startedAt', 'endedAt', 'messageCount', 'tokenCount'],
    'meeting': ['calendarLink', 'isVirtual', 'meetingUrl', 'conferenceProvider', 'phoneDialIn', 'meetingType', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'membership': ['status', 'tier', 'autoRenew', 'price', 'currency', 'billingType', 'useCount', 'guestPassQuantity', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'memex': ['description', 'origin', 'filePath', 'nodeCount', 'edgeCount', 'fileSize', 'published', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'message': ['isOutgoing', 'isStarred', 'conversationId'],
    'model': ['contextLength', 'contextWindow', 'maxOutput', 'pricingInput', 'pricingOutput', 'modality', 'modelType', 'quantization', 'quantizationLevel', 'size', 'parameterSize', 'format', 'family', 'digest'],
    'note': ['noteType', 'isPinned'],
    'offer': ['price', 'currency', 'offerType', 'availability', 'bookingToken', 'departureToken', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'order': ['orderId', 'orderDate', 'total', 'totalAmount', 'originalTotal', 'originalTotalAmount', 'savings', 'currency', 'status', 'deliveryDate', 'eta', 'subtotal', 'tipAmount', 'deliveryFee', 'taxes', 'summary', 'fareBreakdown', 'deliveryInstructions', 'interactionType', 'orderUuid', 'body', 'head', 'messages', 'timeline', 'itemStates', 'latestArrival', 'progress', 'progressTotal', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'organization': ['industry', 'actorType'],
    'pass': ['status', 'quantity', 'purchasedQuantity', 'useCount', 'isAllDayPass', 'price', 'currency', 'ticketNumber', 'nameOnTicket', 'seatAssignment', 'boardingGroup', 'ticketClass', 'gate', 'terminal', 'checkinStatus', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'payment_method': ['identifier', 'type', 'subtype', 'brand', 'displayName', 'customDescription', 'holderName', 'last4', 'binRange', 'expMonth', 'expYear', 'expirationDate', 'currency', 'balance', 'fingerprint', 'isDefault', 'isPrimary', 'isExpired', 'isSelected', 'status', 'providerTokens', 'metadata'],
    'person': ['url', 'givenName', 'additionalName', 'familyName', 'honorificPrefix', 'honorificSuffix', 'legalName', 'preferredName', 'maidenName', 'nickname', 'sortAs', 'nameOrder', 'phoneticGivenName', 'phoneticFamilyName', 'notes', 'gender', 'about', 'actorType'],
    'place': ['fullAddress', 'placeFormatted', 'streetNumber', 'street', 'neighborhood', 'locality', 'city', 'district', 'region', 'postalCode', 'country', 'countryCode', 'latitude', 'longitude', 'accuracy', 'featureType', 'categories', 'phone', 'website', 'hours', 'businessStatus', 'rating', 'reviewCount', 'priceLevel', 'timezone', 'eta', 'isOrderable', 'closedMessage', 'productCount', 'mapboxId', 'wikidataId', 'googlePlaceId'],
    'playlist': ['id', 'listId', 'listType', 'ordering_mode', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'default_view', 'icon_size', 'sort_by', 'path'],
    'podcast': ['feedUrl'],
    'post': ['externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'practice': ['description', 'code', 'codeSystem', 'aliases'],
    'product': ['category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'project': ['state', 'color', 'parentId'],
    'protocol': ['name', 'homepage', 'rfc', 'wikidataId'],
    'qualification': ['category', 'identifier', 'status', 'renewalPeriod', 'level', 'validIn', 'verificationUrl'],
    'quantity-kind': ['key', 'label'],
    'quote': ['context', 'year'],
    'repository': ['stars', 'forks', 'language', 'topics', 'openIssues', 'isArchived', 'isPrivate', 'defaultBranch', 'license', 'size'],
    'reservation': ['reservationType', 'reservationId', 'status', 'bookingType', 'bookingTime', 'modifiedTime', 'startTime', 'endTime', 'partySize', 'totalAmount', 'baseAmount', 'taxAmount', 'currency', 'checkinUrl', 'conditions', 'voidWindowEndsAt', 'availableActions', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'result': ['indexedAt', 'resultType', 'externalUrl', 'postId', 'score', 'similarity', 'community'],
    'review': ['rating', 'ratingMax', 'tags', 'isVerified', 'externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'role': ['title', 'department', 'roleType', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'seatmap': ['flightNumber', 'origin', 'destination', 'fareBasisCode', 'classOfService', 'aircraftCode', 'totalSeats', 'availableSeats', 'cabins', 'tiers', 'hasExitRow', 'hasFreeSeats', 'hasPaidSeats', 'basicEconomyLocked'],
    'shelf': ['isExclusive', 'id', 'listId', 'listType', 'ordering_mode', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'default_view', 'icon_size', 'sort_by', 'path'],
    'simulation': ['status', 'profile', 'task', 'graphMode', 'startedAt', 'endedAt', 'actionCount', 'writeCount'],
    'skill': ['skillId', 'description', 'color', 'status', 'error'],
    'software': ['version', 'applicationCategory', 'runtimePlatform', 'codename', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'sound': ['durationMs', 'channels', 'sampleRate', 'bitDepth', 'purpose', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'source': ['sourceId', 'address', 'scanner', 'enabled', 'description', 'lastSynced'],
    'spec': ['problem', 'successCriteria', 'remoteId', 'priority', 'state', 'labels', 'targetDate', 'target', 'parentId', 'projectId', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'tag': ['color', 'tagType', 'annotated', 'hash'],
    'task': ['remoteId', 'priority', 'state', 'labels', 'targetDate', 'target', 'parentId', 'projectId', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'tax_line': ['code', 'description', 'amount', 'currency', 'kind', 'nature', 'country', 'appliesToIndex', 'refundable', 'merchantImposed', 'rate', 'taxableAmount', 'inclusive'],
    'theme': ['themeId', 'family', 'description', 'style', 'startMenu', 'defaultBackgroundColor'],
    'tool_call': ['name', 'input', 'output', 'isError', 'durationMs'],
    'transaction': ['amount', 'currency', 'balance', 'category', 'postingDate', 'pending', 'recurring', 'notes', 'type', 'details', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'transcript': ['language', 'sourceType', 'contentRole', 'durationMs', 'segmentCount', 'segments'],
    'transition': ['givenName', 'additionalName', 'familyName', 'honorificPrefix', 'honorificSuffix', 'legalName', 'maidenName', 'sortAs', 'nameOrder', 'phoneticGivenName', 'phoneticFamilyName', 'gender', 'nickname', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'trip': ['tripType', 'status', 'departureTime', 'arrivalTime', 'duration', 'durationMinutes', 'distance', 'vehicleType', 'cabinClass', 'fare', 'fareAmount', 'currency', 'rating', 'trackingUrl', 'isSurge', 'isScheduled', 'stops', 'bookingToken', 'carbonEmissions', 'isPool', 'isReserve', 'guest', 'marketplace', 'vehicle', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'unit': ['ucumCode', 'symbol', 'label', 'kind', 'siDigitalFrameworkUri', 'unCefactCommonCode', 'qudtUnitIri', 'wikidataId', 'toBaseFactor', 'toBaseOffset', 'iso4217', 'iso4217Numeric', 'minorExponent', 'logBase'],
    'user': ['osUsername', 'primaryUser', 'actorType'],
    'video': ['durationMs', 'resolution', 'frameRate', 'codec', 'viewCount', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'webpage': ['visitCount', 'lastVisitUnix', 'contentType', 'error'],
    'website': ['status', 'versionId', 'anonymous', 'claimToken', 'claimUrl'],
}

# Every shape whose `also:` chain includes `event` (plus `event` itself).
# Derived from the shape graph — the shape IS the type.
EVENT_TYPES: list[str] = [
    'activity',
    'birth',
    'booking_offer',
    'class',
    'conversion',
    'event',
    'flight',
    'git_commit',
    'health-immunization',
    'health-observation',
    'health-panel',
    'health-procedure',
    'health-reference-range',
    'invitation',
    'launch',
    'leg',
    'loaded_model',
    'meeting',
    'membership',
    'memex',
    'offer',
    'order',
    'pass',
    'reservation',
    'role',
    'spec',
    'task',
    'transaction',
    'transition',
    'trip',
]

# `derived:` bindings per shape — read-side resolver input.
# Binding grammar: {find, where, where_edge, is, get} | {latest: [...]} | dotted string.
SHAPE_DERIVED: dict[str, dict] = {
}

# `shortcuts:` per shape — write-side flat-create expansion table.
# Each entry: flat_key -> {writes: <edge>[is=<shape>].<field>}
SHAPE_SHORTCUTS: dict[str, dict] = {
}
