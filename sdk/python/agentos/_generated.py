"""Auto-generated TypedDict classes from shape YAML — do not edit.

Generated from 111 shapes.
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


class Bookmark(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    handle: str


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


class Change(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    kind: str
    path: str
    phase: str
    status: str
    summary: str
    version: str


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


class Flow(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    goal: str
    status: str
    trigger: str


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


class HealthCondition(TypedDict, total=False):
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
    clinicalArea: str
    clinicalStatus: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    icd10Code: str
    mitigation: str
    properties: Any
    proximity: str
    recurrence: list[str]
    severity: str
    showAs: str
    snomedCode: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    verificationStatus: str
    visibility: str


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
    favicon: str
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
    arrangement: str
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
    member_shape: str
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


class List(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrangement: str
    default_view: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str


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


class Milestone(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    criterion: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    reachedAt: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


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


class Module(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    path: str
    planned: bool
    role: str
    status: str
    version: str


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


class Outcome(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    archived: bool
    baseline: str
    current: str
    metric: str
    statement: str
    status: str
    target: str


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
    notes: str


class Persona(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    goals: list[str]
    headline: str
    painPoints: list[str]
    quote: str
    reachesFor: str
    who: str


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


class Playlist(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrangement: str
    default_view: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str


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


class Principle(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    domain: str
    rationale: str
    statement: str
    status: str


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
    favicon: str
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


class Shelf(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrangement: str
    default_view: str
    icon_size: int
    isDefault: bool
    isExclusive: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str


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


class Step(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    detail: str
    position: int
    status: str


class Symbol(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    kind: str
    lang: str
    signature: str
    sourceLine: int
    sourcePath: str
    summary: str
    urn: str


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


class UserIdentity(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    active: bool
    person_node_id: str
    user_id: str
    volume_id: str


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


class Volume(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    address: str
    auto_mount: bool
    default_view: str
    freeBytes: int
    icon: str
    kind: str
    provider: str
    readOnly: bool
    removable: bool
    scope: str
    totalBytes: int
    volume_id: str


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
    favicon: str
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


# Structured shape defs — consumed by the skill worker to attach
# `__shape_def__` on every @returns(shape) response. Wire-equivalent
# to `agentos_graph::ShapeDef`.
SHAPE_DEFS: dict[str, dict] = {
    'account': {'name': 'account', 'plural': 'accounts', 'description': "A user's presence within a namespace — their GitHub handle, Gmail address,", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountType', 'ty': 'string'}, {'name': 'bio', 'ty': 'text'}, {'name': 'color', 'ty': 'string'}, {'name': 'display', 'ty': 'string'}, {'name': 'displayName', 'ty': 'string'}, {'name': 'email', 'ty': 'string'}, {'name': 'handle', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'isActive', 'ty': 'boolean'}, {'name': 'issuer', 'ty': 'string'}, {'name': 'joinedDate', 'ty': 'datetime'}, {'name': 'lastActive', 'ty': 'datetime'}, {'name': 'lastProfileFetch', 'ty': 'datetime'}, {'name': 'metadata', 'ty': 'json'}, {'name': 'phone', 'ty': 'string'}, {'name': 'userId', 'ty': 'string'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'identifier'}},
    'activity': {'name': 'activity', 'plural': 'activities', 'description': 'An immutable change event — a graph mutation, skill run, search, or load.', 'icon': 'activity', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'action', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'changedKeys', 'ty': 'stringlist'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'number'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'success', 'ty': 'boolean'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'toolName', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'action', 'highlights': ['startDate', 'endDate', 'location']}},
    'actor': {'name': 'actor', 'plural': 'actors', 'description': 'Base type for anything that can be attributed as "who did this" in the graph.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}], 'display': {'subtitle': 'actorType'}},
    'aircraft': {'name': 'aircraft', 'plural': 'aircraft', 'description': 'An aircraft type (not an individual plane). Linked from flight search results.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'department', 'ty': 'string'}, {'name': 'iataCode', 'ty': 'string'}, {'name': 'icaoCode', 'ty': 'string', 'required': True}, {'name': 'images', 'ty': 'json'}, {'name': 'model', 'ty': 'string'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'rangeKm', 'ty': 'integer'}, {'name': 'seatCapacity', 'ty': 'integer'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'variant', 'ty': 'string'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'also': ['product'], 'identity': ['icaoCode'], 'display': {'subtitle': 'model'}},
    'airline': {'name': 'airline', 'plural': 'airlines', 'description': 'A commercial airline. Created from flight search results.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'alliance', 'ty': 'string'}, {'name': 'callsign', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'iataCode', 'ty': 'string', 'required': True}, {'name': 'icaoCode', 'ty': 'string'}, {'name': 'industry', 'ty': 'string'}], 'also': ['organization'], 'identity': ['iataCode'], 'display': {'subtitle': 'iataCode', 'image': 'image', 'highlights': ['headquarters']}},
    'airport': {'name': 'airport', 'plural': 'airports', 'description': 'An airport. Created from flight search results and linked to flights.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'city', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'countryCode', 'ty': 'string'}, {'name': 'elevationFt', 'ty': 'integer'}, {'name': 'iataCode', 'ty': 'string', 'required': True}, {'name': 'icaoCode', 'ty': 'string'}, {'name': 'terminalCount', 'ty': 'integer'}, {'name': 'timezone', 'ty': 'string'}], 'identity': ['iataCode'], 'display': {'subtitle': 'iataCode'}},
    'app': {'name': 'app', 'plural': 'apps', 'description': 'An application — something the shell can spawn as a window. Includes', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'defaultView', 'ty': 'string'}, {'name': 'handles', 'ty': 'stringlist'}, {'name': 'iconRole', 'ty': 'string'}, {'name': 'isSystem', 'ty': 'boolean'}, {'name': 'route', 'ty': 'string'}], 'identity': ['id'], 'display': {'subtitle': 'name'}},
    'birth': {'name': 'birth', 'plural': 'births', 'description': "A person's birth. The canonical event recording given/family names,", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'additionalName', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'familyName', 'ty': 'string'}, {'name': 'gender', 'ty': 'string'}, {'name': 'givenName', 'ty': 'string'}, {'name': 'honorificPrefix', 'ty': 'string'}, {'name': 'honorificSuffix', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'legalName', 'ty': 'string'}, {'name': 'maidenName', 'ty': 'string'}, {'name': 'nameOrder', 'ty': 'string'}, {'name': 'nickname', 'ty': 'string'}, {'name': 'phoneticFamilyName', 'ty': 'string'}, {'name': 'phoneticGivenName', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sortAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'location', 'highlights': ['startDate', 'location']}},
    'book': {'name': 'book', 'plural': 'books', 'description': 'A book. Books are BOTH creative works (the intellectual work — its', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'awardsWon', 'ty': 'stringlist'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'characters', 'ty': 'stringlist'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'department', 'ty': 'string'}, {'name': 'description', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'genres', 'ty': 'stringlist'}, {'name': 'images', 'ty': 'json'}, {'name': 'isbn', 'ty': 'string'}, {'name': 'isbn13', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'originalTitle', 'ty': 'string'}, {'name': 'pages', 'ty': 'integer'}, {'name': 'places', 'ty': 'stringlist'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'series', 'ty': 'string'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'also': ['creative_work', 'product'], 'identity_any': ['isbn13', 'isbn'], 'display': {'subtitle': 'written_by', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'booking_offer': {'name': 'booking_offer', 'plural': 'booking_offers', 'description': 'A signed, itemized, fully-priced commitment presented to a human for', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'approvedAt', 'ty': 'datetime'}, {'name': 'baseAmount', 'ty': 'number'}, {'name': 'blob', 'ty': 'string'}, {'name': 'cartId', 'ty': 'string', 'required': True}, {'name': 'checkoutUrl', 'ty': 'url'}, {'name': 'conditions', 'ty': 'json'}, {'name': 'confirmEndpoint', 'ty': 'url'}, {'name': 'contactEmail', 'ty': 'string'}, {'name': 'contactPhone', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'expiresAt', 'ty': 'datetime'}, {'name': 'feesAmount', 'ty': 'number'}, {'name': 'hasVoidWindow', 'ty': 'boolean'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isChangeable', 'ty': 'boolean'}, {'name': 'isRefundable', 'ty': 'boolean'}, {'name': 'itineraryHash', 'ty': 'string'}, {'name': 'preparedAt', 'ty': 'datetime'}, {'name': 'presentedAt', 'ty': 'datetime'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'referenceNumber', 'ty': 'string'}, {'name': 'review', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'signature', 'ty': 'string'}, {'name': 'signatureAlg', 'ty': 'string'}, {'name': 'signedBy', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'taxAmount', 'ty': 'number'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'totalAmount', 'ty': 'number'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'voidWindowEndsAt', 'ty': 'datetime'}], 'also': ['event'], 'identity': ['at', 'cartId'], 'display': {'subtitle': 'totalAmount', 'highlights': ['startDate', 'endDate', 'location']}},
    'bookmark': {'name': 'bookmark', 'plural': 'bookmarks', 'description': 'A pointer into the graph — the universal shortcut. A bookmark is a', 'icon': '"\\U0001F516"', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'handle', 'ty': 'string'}], 'identity': ['points_to'], 'display': {'subtitle': 'name'}},
    'branch': {'name': 'branch', 'plural': 'branches', 'description': 'A git branch.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'ahead', 'ty': 'integer'}, {'name': 'behind', 'ty': 'integer'}, {'name': 'commit', 'ty': 'string'}, {'name': 'isCurrent', 'ty': 'boolean'}, {'name': 'isRemote', 'ty': 'boolean'}, {'name': 'upstream', 'ty': 'string'}], 'display': {'subtitle': 'commit'}},
    'brand': {'name': 'brand', 'plural': 'brands', 'description': 'A consumer brand — a named, visual, commercial identity. Often (but not', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'primaryColor', 'ty': 'string'}, {'name': 'tagline', 'ty': 'string'}, {'name': 'textColor', 'ty': 'string'}], 'identity': ['url'], 'display': {'subtitle': 'tagline'}},
    'calendar': {'name': 'calendar', 'plural': 'calendars', 'description': 'A calendar — container for events.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accessRole', 'ty': 'string'}, {'name': 'backgroundColor', 'ty': 'string'}, {'name': 'calendarId', 'ty': 'string', 'required': True}, {'name': 'color', 'ty': 'string'}, {'name': 'foregroundColor', 'ty': 'string'}, {'name': 'isPrimary', 'ty': 'boolean'}, {'name': 'isReadonly', 'ty': 'boolean'}, {'name': 'source', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}], 'identity': ['at', 'calendarId'], 'display': {'subtitle': 'source'}},
    'change': {'name': 'change', 'plural': 'changes', 'description': 'A delta on something — a file born/modified/removed, a document revision,', 'icon': 'file-diff', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'phase', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'summary', 'ty': 'text'}, {'name': 'version', 'ty': 'string'}], 'display': {'subtitle': 'kind', 'body': 'summary', 'highlights': ['status', 'phase', 'path']}},
    'channel': {'name': 'channel', 'plural': 'channels', 'description': 'A content channel — typically a YouTube channel. Videos are uploaded to channels.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'banner', 'ty': 'url'}, {'name': 'subscriberCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'subscriberCount'}},
    'class': {'name': 'class', 'plural': 'classes', 'description': 'A scheduled, bookable group activity — gym classes, workshops, courses.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'activityType', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'capacity', 'ty': 'integer'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isFull', 'ty': 'boolean'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'spotsRemaining', 'ty': 'integer'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'activityType', 'highlights': ['startDate', 'endDate', 'location']}},
    'community': {'name': 'community', 'plural': 'communities', 'description': 'An online community — a subreddit, Facebook group, or similar.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allowCrypto', 'ty': 'boolean'}, {'name': 'memberCount', 'ty': 'integer'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'subscriberCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'text'}},
    'conversation': {'name': 'conversation', 'plural': 'conversations', 'description': 'A message thread — an iMessage chat, WhatsApp group, email thread, Claude', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountEmail', 'ty': 'string'}, {'name': 'cwd', 'ty': 'string'}, {'name': 'gitBranch', 'ty': 'string'}, {'name': 'historyId', 'ty': 'string'}, {'name': 'isArchived', 'ty': 'boolean'}, {'name': 'isGroup', 'ty': 'boolean'}, {'name': 'messageCount', 'ty': 'integer'}, {'name': 'source', 'ty': 'string'}, {'name': 'unreadCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'text'}},
    'conversion': {'name': 'conversion', 'plural': 'conversions', 'description': 'A contextual unit conversion — one that is NOT intrinsic to the units', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'factor', 'ty': 'number'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'rate', 'ty': 'number'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'kind', 'highlights': ['startDate', 'endDate', 'location']}},
    'creative_work': {'name': 'creative_work', 'plural': 'creative_works', 'description': "A creative work — the abstract level of FRBR's Work tier. Anything", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'tags', 'ty': 'stringlist'}], 'display': {'subtitle': 'written_by', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'credential': {'name': 'credential', 'plural': 'credentials', 'description': 'A credential held by AgentOS — the graph descriptor that mirrors one', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'domain', 'ty': 'string', 'required': True}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'itemType', 'ty': 'string', 'required': True}, {'name': 'lastVerified', 'ty': 'datetime'}, {'name': 'obtainedAt', 'ty': 'datetime'}, {'name': 'refreshable', 'ty': 'boolean'}, {'name': 'source', 'ty': 'string'}, {'name': 'storeRowId', 'ty': 'integer'}], 'identity': ['domain', 'identifier', 'itemType'], 'display': {'subtitle': 'source'}},
    'dimension': {'name': 'dimension', 'plural': 'dimensions', 'description': 'A physical dimension — the abstract nature of a quantity, expressed as', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'amount', 'ty': 'integer'}, {'name': 'current', 'ty': 'integer'}, {'name': 'dimensionless', 'ty': 'boolean'}, {'name': 'key', 'ty': 'string', 'required': True}, {'name': 'label', 'ty': 'string'}, {'name': 'length', 'ty': 'integer'}, {'name': 'luminous', 'ty': 'integer'}, {'name': 'mass', 'ty': 'integer'}, {'name': 'temperature', 'ty': 'integer'}, {'name': 'time', 'ty': 'integer'}], 'identity': ['key'], 'display': {'subtitle': 'label'}},
    'dns_record': {'name': 'dns_record', 'plural': 'dns_records', 'description': 'A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.).', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'domain', 'ty': 'string', 'required': True}, {'name': 'priority', 'ty': 'integer'}, {'name': 'recordId', 'ty': 'string'}, {'name': 'recordName', 'ty': 'string', 'required': True}, {'name': 'recordType', 'ty': 'string', 'required': True}, {'name': 'ttl', 'ty': 'integer'}, {'name': 'type', 'ty': 'string'}, {'name': 'values', 'ty': 'stringlist'}], 'identity': ['domain', 'recordType', 'recordName'], 'display': {'subtitle': 'recordType'}},
    'document': {'name': 'document', 'plural': 'documents', 'description': 'A document — any human-readable text content with structure and authorship.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'abstract', 'ty': 'text'}, {'name': 'contentType', 'ty': 'string'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tableOfContents', 'ty': 'text'}, {'name': 'wordCount', 'ty': 'integer'}], 'also': ['file'], 'display': {'subtitle': 'contentType', 'body': 'abstract', 'highlights': ['datePublished', 'author', 'wordCount']}},
    'domain': {'name': 'domain', 'plural': 'domains', 'description': 'A registered domain name. Also auto-created from email sender/recipient addresses.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'autoRenew', 'ty': 'boolean'}, {'name': 'nameservers', 'ty': 'stringlist'}, {'name': 'registrar', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}], 'identity': ['name'], 'display': {'subtitle': 'registrar'}},
    'email': {'name': 'email', 'plural': 'emails', 'description': 'An email message. Emails are also messages — querying by "message"', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountEmail', 'ty': 'string'}, {'name': 'attachments', 'ty': 'json'}, {'name': 'authResults', 'ty': 'string'}, {'name': 'bccRaw', 'ty': 'string'}, {'name': 'bodyHtml', 'ty': 'text'}, {'name': 'ccRaw', 'ty': 'string'}, {'name': 'conversationId', 'ty': 'string'}, {'name': 'deliveredTo', 'ty': 'string'}, {'name': 'draftId', 'ty': 'string'}, {'name': 'hasAttachments', 'ty': 'boolean'}, {'name': 'inReplyTo', 'ty': 'string'}, {'name': 'isAutomated', 'ty': 'boolean'}, {'name': 'isDraft', 'ty': 'boolean'}, {'name': 'isOutgoing', 'ty': 'boolean'}, {'name': 'isSent', 'ty': 'boolean'}, {'name': 'isSpam', 'ty': 'boolean'}, {'name': 'isStarred', 'ty': 'boolean'}, {'name': 'isTrash', 'ty': 'boolean'}, {'name': 'isUnread', 'ty': 'boolean'}, {'name': 'listId', 'ty': 'string'}, {'name': 'mailer', 'ty': 'string'}, {'name': 'manageSubscription', 'ty': 'string'}, {'name': 'messageId', 'ty': 'string'}, {'name': 'precedence', 'ty': 'string'}, {'name': 'references', 'ty': 'string'}, {'name': 'replyTo', 'ty': 'string'}, {'name': 'returnPath', 'ty': 'string'}, {'name': 'sizeEstimate', 'ty': 'integer'}, {'name': 'subject', 'ty': 'string'}, {'name': 'toRaw', 'ty': 'string'}, {'name': 'unsubscribe', 'ty': 'string'}, {'name': 'unsubscribeOneClick', 'ty': 'boolean'}], 'also': ['message'], 'identity': ['at', 'id'], 'display': {'subtitle': 'author'}},
    'episode': {'name': 'episode', 'plural': 'episodes', 'description': 'A single episode of a podcast or show. Transcribable.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'episodeNumber', 'ty': 'integer'}, {'name': 'seasonNumber', 'ty': 'integer'}], 'display': {'subtitle': 'author'}},
    'event': {'name': 'event', 'plural': 'events', 'description': 'Something that happens — at a time, optionally at a place, involving people.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'endDate', 'location']}},
    'fare': {'name': 'fare', 'plural': 'fares', 'description': 'The priced class-of-service unit for a transport journey — the BASE', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'basePrice', 'ty': 'number'}, {'name': 'bookingCode', 'ty': 'string'}, {'name': 'changeable', 'ty': 'boolean'}, {'name': 'class', 'ty': 'string'}, {'name': 'components', 'ty': 'integer'}, {'name': 'conditions', 'ty': 'json'}, {'name': 'currency', 'ty': 'string'}, {'name': 'fareFamily', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'milesEarned', 'ty': 'integer'}, {'name': 'passengerType', 'ty': 'string'}, {'name': 'pointsEarned', 'ty': 'integer'}, {'name': 'productType', 'ty': 'string'}, {'name': 'refundable', 'ty': 'boolean'}, {'name': 'restrictions', 'ty': 'stringlist'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'fareFamily'}},
    'file': {'name': 'file', 'plural': 'files', 'description': 'A file — source code, attachment, download, or any discrete digital artifact.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}], 'display': {'subtitle': 'path'}},
    'financial_account': {'name': 'financial_account', 'plural': 'financial_accounts', 'description': 'A financial account — bank checking/savings, brokerage, crypto wallet, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountId', 'ty': 'string'}, {'name': 'accountNumber', 'ty': 'string'}, {'name': 'accountType', 'ty': 'string'}, {'name': 'available', 'ty': 'number'}, {'name': 'balance', 'ty': 'number'}, {'name': 'cardType', 'ty': 'string'}, {'name': 'creditLimit', 'ty': 'number'}, {'name': 'currency', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'interestRate', 'ty': 'number'}, {'name': 'last4', 'ty': 'string'}, {'name': 'minimumPayment', 'ty': 'number'}, {'name': 'routingNumber', 'ty': 'string'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'last4'}},
    'flight': {'name': 'flight', 'plural': 'flights', 'description': 'A flight — a specific leg of air travel. A flight IS a leg.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrivalTime', 'ty': 'datetime'}, {'name': 'cabinClass', 'ty': 'string'}, {'name': 'carbonEmissions', 'ty': 'json'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureTime', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'string'}, {'name': 'durationMinutes', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flightNumber', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'layoverMinutes', 'ty': 'integer'}, {'name': 'polyline', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'sequence', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'stops', 'ty': 'integer'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'trace', 'ty': 'json'}, {'name': 'tracePointCount', 'ty': 'integer'}, {'name': 'vehicleType', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['leg'], 'display': {'subtitle': 'airline', 'highlights': ['startDate', 'endDate', 'location']}},
    'flow': {'name': 'flow', 'plural': 'flows', 'description': 'A process / swim-lane — actors across ordered steps. The universal shape', 'icon': 'workflow', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'goal', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}, {'name': 'trigger', 'ty': 'string'}], 'display': {'subtitle': 'goal', 'highlights': ['trigger', 'status']}},
    'font': {'name': 'font', 'plural': 'fonts', 'description': 'A typeface — the family-level work. One node per font family', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'designerUrl', 'ty': 'string'}, {'name': 'family', 'ty': 'string'}, {'name': 'formats', 'ty': 'stringlist'}, {'name': 'genericFamily', 'ty': 'string'}, {'name': 'glyphCount', 'ty': 'integer'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'licenseInfoUrl', 'ty': 'string'}, {'name': 'postscriptName', 'ty': 'string'}, {'name': 'scripts', 'ty': 'stringlist'}, {'name': 'styles', 'ty': 'stringlist'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'vendorUrl', 'ty': 'string'}, {'name': 'weights', 'ty': 'integerlist'}], 'also': ['creative_work'], 'identity_any': ['family', 'postscriptName'], 'display': {'subtitle': 'author', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'git_commit': {'name': 'git_commit', 'plural': 'git_commits', 'description': 'A git commit — a single point in version control history.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'additions', 'ty': 'integer'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'committedAt', 'ty': 'datetime'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'deletions', 'ty': 'integer'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'filesChanged', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'message', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'sha', 'ty': 'string'}, {'name': 'shortHash', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'author', 'highlights': ['startDate', 'endDate', 'location']}},
    'group': {'name': 'group', 'plural': 'groups', 'description': 'A group or community — online group, reading group, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'memberCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'category'}},
    'health-biomarker': {'name': 'health-biomarker', 'plural': 'health-biomarkers', 'description': 'The *definition* of a measurable health quantity — TSH, LDL cholesterol,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'analyteType', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'loincCode', 'ty': 'string'}, {'name': 'measure', 'ty': 'string'}], 'identity_any': ['loincCode', 'measure'], 'display': {'subtitle': 'category'}},
    'health-condition': {'name': 'health-condition', 'plural': 'health-conditions', 'description': 'A health condition — a diagnosis, problem, symptom, or family-history', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'bodySite', 'ty': 'string'}, {'name': 'clinicalArea', 'ty': 'string'}, {'name': 'clinicalStatus', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'icd10Code', 'ty': 'string'}, {'name': 'mitigation', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'proximity', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'severity', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'snomedCode', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'verificationStatus', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity_any': ['snomedCode', 'name'], 'display': {'subtitle': 'clinicalStatus', 'highlights': ['startDate', 'endDate', 'location']}},
    'health-immunization': {'name': 'health-immunization', 'plural': 'health-immunizations', 'description': 'An immunization — a single vaccine administration at a point in time.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'cvxCode', 'ty': 'string'}, {'name': 'dateAdministered', 'ty': 'datetime'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'diseaseTarget', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'doseNumber', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'lotNumber', 'ty': 'string'}, {'name': 'manufacturer', 'ty': 'string'}, {'name': 'notes', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'route', 'ty': 'string'}, {'name': 'seriesDoses', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'site', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'dateAdministered', 'highlights': ['startDate', 'endDate', 'location']}},
    'health-lab': {'name': 'health-lab', 'plural': 'health-labs', 'description': 'A clinical laboratory or testing facility — the place that processes a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accreditation', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'ccn', 'ty': 'string'}, {'name': 'cliaNumber', 'ty': 'string'}, {'name': 'industry', 'ty': 'string'}, {'name': 'labType', 'ty': 'string'}, {'name': 'npi', 'ty': 'string'}], 'also': ['organization'], 'identity_any': ['cliaNumber', 'url'], 'display': {'subtitle': 'labType', 'image': 'image', 'highlights': ['headquarters']}},
    'health-observation': {'name': 'health-observation', 'plural': 'health-observations', 'description': 'A single measured health value at a point in time — "LDL = 95 mg/dL on', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'community', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'favicon', 'ty': 'url'}, {'name': 'flag', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'indexedAt', 'ty': 'datetime'}, {'name': 'notes', 'ty': 'text'}, {'name': 'postId', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'refHigh', 'ty': 'number'}, {'name': 'refLow', 'ty': 'number'}, {'name': 'refText', 'ty': 'string'}, {'name': 'resultType', 'ty': 'string'}, {'name': 'score', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'similarity', 'ty': 'number'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'value', 'ty': 'number'}, {'name': 'valueText', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['result', 'event'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'endDate', 'location']}},
    'health-panel': {'name': 'health-panel', 'plural': 'health-panels', 'description': 'A panel — a named grouping of biomarkers ordered and reported together.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'fasting', 'ty': 'boolean'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'panelCode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['list', 'event'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'endDate', 'location']}},
    'health-procedure': {'name': 'health-procedure', 'plural': 'health-procedures', 'description': 'A procedure — a clinical action performed on the body. Surgeries', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'bodySite', 'ty': 'string'}, {'name': 'cptCode', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'findings', 'ty': 'text'}, {'name': 'followUp', 'ty': 'text'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'outcome', 'ty': 'string'}, {'name': 'performedDate', 'ty': 'datetime'}, {'name': 'procedureType', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'snomedCode', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity_any': ['cptCode', 'snomedCode', 'id'], 'display': {'subtitle': 'performedDate', 'highlights': ['startDate', 'endDate', 'location']}},
    'health-reference-range': {'name': 'health-reference-range', 'plural': 'health-reference-ranges', 'description': 'A lab-specific reference interval — the "normal range" for a biomarker,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'ageHigh', 'ty': 'number'}, {'name': 'ageLow', 'ty': 'number'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'category', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'fasting', 'ty': 'boolean'}, {'name': 'gestationalAge', 'ty': 'string'}, {'name': 'high', 'ty': 'number'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'low', 'ty': 'number'}, {'name': 'method', 'ty': 'string', 'required': True}, {'name': 'pregnancy', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'provenance', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'refText', 'ty': 'string'}, {'name': 'sex', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime', 'required': True}, {'name': 'status', 'ty': 'string'}, {'name': 'timeOfDay', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'unit', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['analyte', 'issuingLab', 'method', 'startDate'], 'display': {'subtitle': 'refText', 'highlights': ['startDate', 'endDate', 'location']}},
    'icon': {'name': 'icon', 'plural': 'icons', 'description': 'A small graphic intended for UI use — toolbar buttons, file-type', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'component', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'dimension', 'ty': 'integer'}, {'name': 'format', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'purpose', 'ty': 'string'}, {'name': 'style', 'ty': 'string'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['creative_work'], 'identity_any': ['component', 'url'], 'display': {'subtitle': 'purpose', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'image': {'name': 'image', 'plural': 'images', 'description': 'An image file. Photos, screenshots, diagrams, artwork.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'altText', 'ty': 'string'}, {'name': 'appName', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'displayId', 'ty': 'integer'}, {'name': 'displayIndex', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'height', 'ty': 'integer'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'width', 'ty': 'integer'}, {'name': 'windowId', 'ty': 'integer'}], 'also': ['creative_work', 'file'], 'identity_any': ['url'], 'display': {'subtitle': 'format', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'intellectual_property': {'name': 'intellectual_property', 'plural': 'intellectual_properties', 'description': 'A registered or pending intellectual-property right — a trademark,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'filingBasis', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string'}, {'name': 'mark', 'ty': 'string'}, {'name': 'niceClass', 'ty': 'integerlist'}, {'name': 'register', 'ty': 'string'}, {'name': 'renewalPeriod', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'validIn', 'ty': 'string'}, {'name': 'verificationUrl', 'ty': 'url'}], 'identity_any': ['identifier'], 'display': {'subtitle': 'category', 'highlights': ['identifier', 'status', 'granted_by']}},
    'invitation': {'name': 'invitation', 'plural': 'invitations', 'description': 'An invitation to join something — an organization, a workspace, a team, a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'acceptedAt', 'ty': 'datetime'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'email', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'invitationType', 'ty': 'string'}, {'name': 'message', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'revokedAt', 'ty': 'datetime'}, {'name': 'role', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'token', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'invitationType', 'highlights': ['startDate', 'endDate', 'location']}},
    'launch': {'name': 'launch', 'plural': 'launches', 'description': 'A rocket launch event. Carries flight-specific fields that previously', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'articleUrl', 'ty': 'url'}, {'name': 'crewIds', 'ty': 'stringlist'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flightNumber', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'landingOutcomes', 'ty': 'json'}, {'name': 'launchpadId', 'ty': 'string'}, {'name': 'patchImage', 'ty': 'url'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'reusedBoosters', 'ty': 'stringlist'}, {'name': 'rocketId', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'webcastUrl', 'ty': 'url'}, {'name': 'wikipediaUrl', 'ty': 'url'}], 'also': ['event'], 'display': {'subtitle': 'rocketId', 'highlights': ['startDate', 'rocketId', 'launchpadId']}},
    'leg': {'name': 'leg', 'plural': 'legs', 'description': 'One continuous movement on a single vehicle — takeoff to landing,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrivalTime', 'ty': 'datetime'}, {'name': 'cabinClass', 'ty': 'string'}, {'name': 'carbonEmissions', 'ty': 'json'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureTime', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'string'}, {'name': 'durationMinutes', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flightNumber', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'layoverMinutes', 'ty': 'integer'}, {'name': 'polyline', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'sequence', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'trace', 'ty': 'json'}, {'name': 'tracePointCount', 'ty': 'integer'}, {'name': 'vehicleType', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'flightNumber', 'highlights': ['startDate', 'endDate', 'location']}},
    'list': {'name': 'list', 'plural': 'lists', 'description': 'A list — the universal ordered (or not) collection. Folders, menus,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'name'}},
    'loaded_model': {'name': 'loaded_model', 'plural': 'loaded_models', 'description': 'A currently loaded/running AI model instance.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'digest', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'quantization', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'size', 'ty': 'string'}, {'name': 'sizeVram', 'ty': 'integer'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'vramUsage', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'size', 'highlights': ['startDate', 'endDate', 'location']}},
    'mcp_session': {'name': 'mcp_session', 'plural': 'mcp_sessions', 'description': 'An MCP session — a client connected, made some calls, disconnected.', 'icon': 'terminal', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'client', 'ty': 'string', 'required': True}, {'name': 'endedAt', 'ty': 'datetime'}, {'name': 'gitBranch', 'ty': 'string', 'required': True}, {'name': 'messageCount', 'ty': 'integer'}, {'name': 'projectId', 'ty': 'string', 'required': True}, {'name': 'sessionType', 'ty': 'string'}, {'name': 'startedAt', 'ty': 'datetime'}, {'name': 'tokenCount', 'ty': 'integer'}], 'identity': ['client', 'projectId', 'gitBranch'], 'display': {'subtitle': 'client'}},
    'meeting': {'name': 'meeting', 'plural': 'meetings', 'description': 'A calendar meeting — an event with virtual meeting details and transcripts.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'calendarLink', 'ty': 'url'}, {'name': 'conferenceProvider', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isVirtual', 'ty': 'boolean'}, {'name': 'meetingType', 'ty': 'string'}, {'name': 'meetingUrl', 'ty': 'url'}, {'name': 'phoneDialIn', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'location', 'highlights': ['startDate', 'endDate', 'location']}},
    'membership': {'name': 'membership', 'plural': 'memberships', 'description': 'A time-bounded right-of-belonging granted by an organization.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'autoRenew', 'ty': 'boolean'}, {'name': 'billingType', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'guestPassQuantity', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'tier', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'useCount', 'ty': 'integer'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'status', 'highlights': ['startDate', 'endDate', 'location']}},
    'message': {'name': 'message', 'plural': 'messages', 'description': 'A single message in a conversation. Base type — email extends this via `also`.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'conversationId', 'ty': 'string'}, {'name': 'isOutgoing', 'ty': 'boolean'}, {'name': 'isStarred', 'ty': 'boolean'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'from'}},
    'milestone': {'name': 'milestone', 'plural': 'milestones', 'description': 'A point-in-time checkpoint — a significant, zero-duration moment in a', 'icon': 'flag', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'criterion', 'ty': 'text'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'reachedAt', 'ty': 'datetime'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'status', 'body': 'criterion', 'highlights': ['status', 'reachedAt']}},
    'model': {'name': 'model', 'plural': 'models', 'description': 'An AI model — LLM, embedding model, or other ML model.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'contextLength', 'ty': 'integer'}, {'name': 'contextWindow', 'ty': 'integer'}, {'name': 'digest', 'ty': 'string'}, {'name': 'family', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'maxOutput', 'ty': 'integer'}, {'name': 'modality', 'ty': 'stringlist'}, {'name': 'modelType', 'ty': 'string'}, {'name': 'parameterSize', 'ty': 'string'}, {'name': 'pricingInput', 'ty': 'string'}, {'name': 'pricingOutput', 'ty': 'string'}, {'name': 'quantization', 'ty': 'string'}, {'name': 'quantizationLevel', 'ty': 'string'}, {'name': 'size', 'ty': 'string'}], 'identity': ['at', 'name'], 'display': {'subtitle': 'name'}},
    'module': {'name': 'module', 'plural': 'modules', 'description': 'A self-contained unit of a larger whole — a software module, a course', 'icon': 'package', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'planned', 'ty': 'boolean'}, {'name': 'role', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}, {'name': 'version', 'ty': 'string'}], 'display': {'subtitle': 'role', 'highlights': ['status', 'path']}},
    'note': {'name': 'note', 'plural': 'notes', 'description': 'Private text content, primarily for the author. Journal entries, PKM notes,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'isPinned', 'ty': 'boolean'}, {'name': 'noteType', 'ty': 'string'}], 'display': {'subtitle': 'noteType'}},
    'offer': {'name': 'offer', 'plural': 'offers', 'description': 'A purchasable offer — typically a flight itinerary with a price.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'availability', 'ty': 'string'}, {'name': 'bookingToken', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureToken', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'offerType', 'ty': 'string'}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['id'], 'display': {'subtitle': 'price', 'highlights': ['startDate', 'endDate', 'location']}},
    'order': {'name': 'order', 'plural': 'orders', 'description': 'A purchase order. Contains products and tracks delivery.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'body', 'ty': 'text'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'deliveryDate', 'ty': 'datetime'}, {'name': 'deliveryFee', 'ty': 'number'}, {'name': 'deliveryInstructions', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'eta', 'ty': 'string'}, {'name': 'fareBreakdown', 'ty': 'json'}, {'name': 'head', 'ty': 'text'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'interactionType', 'ty': 'string'}, {'name': 'itemStates', 'ty': 'json'}, {'name': 'latestArrival', 'ty': 'datetime'}, {'name': 'messages', 'ty': 'json'}, {'name': 'orderDate', 'ty': 'datetime'}, {'name': 'orderId', 'ty': 'string', 'required': True}, {'name': 'orderUuid', 'ty': 'string'}, {'name': 'originalTotal', 'ty': 'string'}, {'name': 'originalTotalAmount', 'ty': 'number'}, {'name': 'progress', 'ty': 'number'}, {'name': 'progressTotal', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'savings', 'ty': 'number'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'subtotal', 'ty': 'number'}, {'name': 'summary', 'ty': 'string'}, {'name': 'taxes', 'ty': 'number'}, {'name': 'timeline', 'ty': 'json'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'tipAmount', 'ty': 'number'}, {'name': 'total', 'ty': 'string'}, {'name': 'totalAmount', 'ty': 'number'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'orderId'], 'display': {'subtitle': 'total', 'highlights': ['startDate', 'endDate', 'location']}},
    'organization': {'name': 'organization', 'plural': 'organizations', 'description': 'A company, nonprofit, or other organization. Organizations are actors — they', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'industry', 'ty': 'string'}], 'also': ['actor'], 'identity': ['url'], 'display': {'subtitle': 'industry', 'image': 'image', 'highlights': ['headquarters']}},
    'outcome': {'name': 'outcome', 'plural': 'outcomes', 'description': 'A tracked target-state — the change being sought, with a status and', 'icon': 'target', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'archived', 'ty': 'boolean'}, {'name': 'baseline', 'ty': 'string'}, {'name': 'current', 'ty': 'string'}, {'name': 'metric', 'ty': 'string'}, {'name': 'statement', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}, {'name': 'target', 'ty': 'string'}], 'display': {'subtitle': 'status', 'body': 'statement'}},
    'pass': {'name': 'pass', 'plural': 'passes', 'description': 'A fixed-quantity right-of-access — a bundle of entries, a multi-day', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'boardingGroup', 'ty': 'string'}, {'name': 'checkinStatus', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'gate', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isAllDayPass', 'ty': 'boolean'}, {'name': 'nameOnTicket', 'ty': 'string'}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'purchasedQuantity', 'ty': 'integer'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'seatAssignment', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'terminal', 'ty': 'string'}, {'name': 'ticketClass', 'ty': 'string'}, {'name': 'ticketNumber', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'useCount', 'ty': 'integer'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'status', 'highlights': ['startDate', 'endDate', 'location']}},
    'payment_method': {'name': 'payment_method', 'plural': 'payment_methods', 'description': 'A saved payment instrument — credit/debit card, PayPal/Venmo account,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'balance', 'ty': 'number'}, {'name': 'binRange', 'ty': 'string'}, {'name': 'brand', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customDescription', 'ty': 'string'}, {'name': 'displayName', 'ty': 'string'}, {'name': 'expMonth', 'ty': 'integer'}, {'name': 'expYear', 'ty': 'integer'}, {'name': 'expirationDate', 'ty': 'string'}, {'name': 'fingerprint', 'ty': 'string'}, {'name': 'holderName', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isExpired', 'ty': 'boolean'}, {'name': 'isPrimary', 'ty': 'boolean'}, {'name': 'isSelected', 'ty': 'boolean'}, {'name': 'last4', 'ty': 'string'}, {'name': 'metadata', 'ty': 'json'}, {'name': 'providerTokens', 'ty': 'json'}, {'name': 'status', 'ty': 'string'}, {'name': 'subtype', 'ty': 'string'}, {'name': 'type', 'ty': 'string'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'displayName'}},
    'person': {'name': 'person', 'plural': 'people', 'description': 'A real human. People are actors — they can own accounts, hold roles,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'about', 'ty': 'text'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'notes', 'ty': 'text'}], 'derived': [{'key': 'additionalName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'additionalName'}, {'find': 'changed', 'is': 'transition', 'get': 'additionalName'}]}}, {'key': 'birthdate', 'spec': {'find': 'born_in', 'is': 'birth', 'get': 'startDate'}}, {'key': 'current_residence', 'spec': {'find': 'lived_at', 'where_link': {'to': None}, 'get': 'name'}}, {'key': 'current_role', 'spec': {'find': 'worked_at', 'where_link': {'to': None}, 'get': 'title'}}, {'key': 'familyName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'familyName'}, {'find': 'changed', 'is': 'transition', 'get': 'familyName'}]}}, {'key': 'gender', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'gender'}, {'find': 'changed', 'is': 'transition', 'get': 'gender'}]}}, {'key': 'givenName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'givenName'}, {'find': 'changed', 'is': 'transition', 'get': 'givenName'}]}}, {'key': 'honorificPrefix', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificPrefix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificPrefix'}]}}, {'key': 'honorificSuffix', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificSuffix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificSuffix'}]}}, {'key': 'legalName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'legalName'}, {'find': 'changed', 'is': 'transition', 'get': 'legalName'}]}}, {'key': 'maidenName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'maidenName'}, {'find': 'changed', 'is': 'transition', 'get': 'maidenName'}]}}, {'key': 'nameOrder', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nameOrder'}, {'find': 'changed', 'is': 'transition', 'get': 'nameOrder'}]}}, {'key': 'nickname', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nickname'}, {'find': 'changed', 'is': 'transition', 'get': 'nickname'}]}}, {'key': 'phoneticFamilyName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticFamilyName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticFamilyName'}]}}, {'key': 'phoneticGivenName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticGivenName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticGivenName'}]}}, {'key': 'sortAs', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'sortAs'}, {'find': 'changed', 'is': 'transition', 'get': 'sortAs'}]}}], 'shortcuts': [{'key': 'additionalName', 'writes': 'born_in[is=birth].additionalName'}, {'key': 'birthdate', 'writes': 'born_in[is=birth].startDate'}, {'key': 'familyName', 'writes': 'born_in[is=birth].familyName'}, {'key': 'gender', 'writes': 'born_in[is=birth].gender'}, {'key': 'givenName', 'writes': 'born_in[is=birth].givenName'}, {'key': 'honorificPrefix', 'writes': 'born_in[is=birth].honorificPrefix'}, {'key': 'honorificSuffix', 'writes': 'born_in[is=birth].honorificSuffix'}, {'key': 'legalName', 'writes': 'born_in[is=birth].legalName'}, {'key': 'maidenName', 'writes': 'born_in[is=birth].maidenName'}, {'key': 'nameOrder', 'writes': 'born_in[is=birth].nameOrder'}, {'key': 'nickname', 'writes': 'born_in[is=birth].nickname'}, {'key': 'phoneticFamilyName', 'writes': 'born_in[is=birth].phoneticFamilyName'}, {'key': 'phoneticGivenName', 'writes': 'born_in[is=birth].phoneticGivenName'}, {'key': 'sortAs', 'writes': 'born_in[is=birth].sortAs'}], 'also': ['actor'], 'identity_any': ['url'], 'display': {'subtitle': 'about', 'image': 'image', 'body': 'notes', 'highlights': ['birthdate', 'gender']}},
    'persona': {'name': 'persona', 'plural': 'personas', 'description': 'An archetype of an audience segment — a named, hypothetical user that', 'icon': 'user-round-search', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'goals', 'ty': 'stringlist'}, {'name': 'headline', 'ty': 'string'}, {'name': 'painPoints', 'ty': 'stringlist'}, {'name': 'quote', 'ty': 'text'}, {'name': 'reachesFor', 'ty': 'text'}, {'name': 'who', 'ty': 'text'}], 'display': {'subtitle': 'headline', 'body': 'who', 'highlights': ['reachesFor', 'quote']}},
    'place': {'name': 'place', 'plural': 'places', 'description': 'A physical location — address, building, city, or point of interest.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accuracy', 'ty': 'string'}, {'name': 'businessStatus', 'ty': 'string'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'city', 'ty': 'string'}, {'name': 'closedMessage', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'countryCode', 'ty': 'string'}, {'name': 'district', 'ty': 'string'}, {'name': 'eta', 'ty': 'string'}, {'name': 'featureType', 'ty': 'string'}, {'name': 'fullAddress', 'ty': 'string'}, {'name': 'googlePlaceId', 'ty': 'string'}, {'name': 'hours', 'ty': 'json'}, {'name': 'isOrderable', 'ty': 'boolean'}, {'name': 'latitude', 'ty': 'number'}, {'name': 'locality', 'ty': 'string'}, {'name': 'longitude', 'ty': 'number'}, {'name': 'mapboxId', 'ty': 'string'}, {'name': 'neighborhood', 'ty': 'string'}, {'name': 'phone', 'ty': 'string'}, {'name': 'placeFormatted', 'ty': 'string'}, {'name': 'postalCode', 'ty': 'string'}, {'name': 'priceLevel', 'ty': 'string'}, {'name': 'productCount', 'ty': 'integer'}, {'name': 'rating', 'ty': 'number'}, {'name': 'region', 'ty': 'string'}, {'name': 'reviewCount', 'ty': 'integer'}, {'name': 'street', 'ty': 'string'}, {'name': 'streetNumber', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'website', 'ty': 'url'}, {'name': 'wikidataId', 'ty': 'string'}], 'identity_any': ['googlePlaceId', 'mapboxId'], 'display': {'subtitle': 'featureType', 'image': 'image', 'body': 'fullAddress', 'highlights': ['city', 'country', 'rating']}},
    'playlist': {'name': 'playlist', 'plural': 'playlists', 'description': 'A video playlist. Playlists are lists that contain videos instead of products.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}], 'also': ['list'], 'display': {'subtitle': 'text'}},
    'podcast': {'name': 'podcast', 'plural': 'podcasts', 'description': "A podcast series. Contains episodes. Not the audio itself — that's on the episode.", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'feedUrl', 'ty': 'url'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'host'}},
    'post': {'name': 'post', 'plural': 'posts', 'description': 'A piece of published content — a Reddit submission, HN story, YouTube upload,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'commentCount', 'ty': 'integer'}, {'name': 'community', 'ty': 'string'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'postType', 'ty': 'string'}, {'name': 'score', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'author'}},
    'practice': {'name': 'practice', 'plural': 'practices', 'description': 'A field of practice or study — a discipline a person practices, or the', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aliases', 'ty': 'stringlist'}, {'name': 'code', 'ty': 'string'}, {'name': 'codeSystem', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}], 'display': {'subtitle': 'parent'}},
    'principle': {'name': 'principle', 'plural': 'principles', 'description': 'A guiding bright-line — a value or rule used to judge edge cases. Universal:', 'icon': 'scale', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'domain', 'ty': 'string'}, {'name': 'rationale', 'ty': 'text'}, {'name': 'statement', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}], 'display': {'subtitle': 'domain', 'body': 'rationale', 'highlights': ['statement', 'status']}},
    'product': {'name': 'product', 'plural': 'products', 'description': 'A purchasable item OR an identifiable product released into the world.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'department', 'ty': 'string'}, {'name': 'images', 'ty': 'json'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'identity_any': ['url'], 'display': {'subtitle': 'brand'}},
    'project': {'name': 'project', 'plural': 'projects', 'description': 'A project that groups tasks. Tasks belong to projects.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'color', 'ty': 'string'}, {'name': 'parentId', 'ty': 'string'}, {'name': 'state', 'ty': 'string'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'state'}},
    'protocol': {'name': 'protocol', 'plural': 'protocols', 'description': 'A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'homepage', 'ty': 'url'}, {'name': 'rfc', 'ty': 'string'}, {'name': 'wikidataId', 'ty': 'string'}], 'identity': ['name'], 'display': {'subtitle': 'name'}},
    'qualification': {'name': 'qualification', 'plural': 'qualifications', 'description': 'An earned qualification — a degree, professional license, board', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string'}, {'name': 'level', 'ty': 'string'}, {'name': 'renewalPeriod', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'validIn', 'ty': 'string'}, {'name': 'verificationUrl', 'ty': 'url'}], 'identity_any': ['identifier'], 'display': {'subtitle': 'category', 'highlights': ['identifier', 'validIn', 'granted_by']}},
    'quantity-kind': {'name': 'quantity-kind', 'plural': 'quantity-kinds', 'description': 'A quantity kind — WHAT is being measured, semantically. "Mass', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'key', 'ty': 'string', 'required': True}, {'name': 'label', 'ty': 'string'}], 'identity': ['key'], 'display': {'subtitle': 'label'}},
    'quote': {'name': 'quote', 'plural': 'quotes', 'description': 'A notable quote. Attribution is a graph relationship, not a field —', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'context', 'ty': 'string'}, {'name': 'year', 'ty': 'integer'}], 'display': {'subtitle': 'year'}},
    'repository': {'name': 'repository', 'plural': 'repositories', 'description': 'A source code repository.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'defaultBranch', 'ty': 'string'}, {'name': 'forks', 'ty': 'integer'}, {'name': 'isArchived', 'ty': 'boolean'}, {'name': 'isPrivate', 'ty': 'boolean'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'openIssues', 'ty': 'integer'}, {'name': 'size', 'ty': 'integer'}, {'name': 'stars', 'ty': 'integer'}, {'name': 'topics', 'ty': 'stringlist'}], 'identity_any': ['path', 'url'], 'display': {'subtitle': 'language'}},
    'reservation': {'name': 'reservation', 'plural': 'reservations', 'description': 'A forward commitment to a future thing — a flight booking, a hotel', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'availableActions', 'ty': 'stringlist'}, {'name': 'baseAmount', 'ty': 'number'}, {'name': 'bookingTime', 'ty': 'datetime'}, {'name': 'bookingType', 'ty': 'string'}, {'name': 'checkinUrl', 'ty': 'url'}, {'name': 'conditions', 'ty': 'json'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'endTime', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'modifiedTime', 'ty': 'datetime'}, {'name': 'partySize', 'ty': 'integer'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'reservationId', 'ty': 'string', 'required': True}, {'name': 'reservationType', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'startTime', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'taxAmount', 'ty': 'number'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'totalAmount', 'ty': 'number'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'voidWindowEndsAt', 'ty': 'datetime'}], 'also': ['event'], 'identity': ['at', 'reservationId'], 'display': {'subtitle': 'reservationType', 'highlights': ['startDate', 'endDate', 'location']}},
    'result': {'name': 'result', 'plural': 'results', 'description': 'A search result — a pointer to something found. Not the thing itself.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'community', 'ty': 'string'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'favicon', 'ty': 'url'}, {'name': 'indexedAt', 'ty': 'datetime'}, {'name': 'postId', 'ty': 'string'}, {'name': 'resultType', 'ty': 'string'}, {'name': 'score', 'ty': 'integer'}, {'name': 'similarity', 'ty': 'number'}], 'display': {'subtitle': 'url'}},
    'review': {'name': 'review', 'plural': 'reviews', 'description': 'A user review of a product. Reviews are also posts, so they carry engagement metrics.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'commentCount', 'ty': 'integer'}, {'name': 'community', 'ty': 'string'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'isVerified', 'ty': 'boolean'}, {'name': 'postType', 'ty': 'string'}, {'name': 'rating', 'ty': 'number'}, {'name': 'ratingMax', 'ty': 'number'}, {'name': 'score', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['post'], 'display': {'subtitle': 'author'}},
    'role': {'name': 'role', 'plural': 'roles', 'description': "A person's position at an organization (job title, board seat, etc.).", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'department', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'roleType', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'title', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'name', 'highlights': ['startDate', 'endDate', 'location']}},
    'seatmap': {'name': 'seatmap', 'plural': 'seatmaps', 'description': 'A seat map for a specific flight + cabin, returned by an airline skill.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aircraftCode', 'ty': 'string'}, {'name': 'availableSeats', 'ty': 'integer'}, {'name': 'basicEconomyLocked', 'ty': 'boolean'}, {'name': 'cabins', 'ty': 'json'}, {'name': 'classOfService', 'ty': 'string'}, {'name': 'destination', 'ty': 'string'}, {'name': 'fareBasisCode', 'ty': 'string'}, {'name': 'flightNumber', 'ty': 'string'}, {'name': 'hasExitRow', 'ty': 'boolean'}, {'name': 'hasFreeSeats', 'ty': 'boolean'}, {'name': 'hasPaidSeats', 'ty': 'boolean'}, {'name': 'origin', 'ty': 'string'}, {'name': 'tiers', 'ty': 'json'}, {'name': 'totalSeats', 'ty': 'integer'}], 'identity': ['id'], 'display': {'title': 'flightNumber'}},
    'shelf': {'name': 'shelf', 'plural': 'shelves', 'description': 'A bookshelf. Shelves are lists that contain books instead of generic products.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isExclusive', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}], 'also': ['list'], 'display': {'subtitle': 'isExclusive'}},
    'skill': {'name': 'skill', 'plural': 'skills', 'description': 'A connected service/integration in agentOS. Each skill provides tools', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'color', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'error', 'ty': 'text'}, {'name': 'skillId', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}], 'display': {'subtitle': 'description'}},
    'software': {'name': 'software', 'plural': 'software', 'description': 'A software product — operating system, application, library, icon pack,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'applicationCategory', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'codename', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'department', 'ty': 'string'}, {'name': 'images', 'ty': 'json'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'runtimePlatform', 'ty': 'string'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'version', 'ty': 'string'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'also': ['product'], 'identity_any': ['url'], 'display': {'subtitle': 'applicationCategory', 'highlights': ['version', 'runtimePlatform']}},
    'sound': {'name': 'sound', 'plural': 'sounds', 'description': 'An audio clip — startup chimes, error beeps, notification dings,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'bitDepth', 'ty': 'integer'}, {'name': 'channels', 'ty': 'integer'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'purpose', 'ty': 'string'}, {'name': 'sampleRate', 'ty': 'integer'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['creative_work', 'file'], 'identity_any': ['url'], 'display': {'subtitle': 'purpose', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'source': {'name': 'source', 'plural': 'sources', 'description': 'A content source — where skills, themes, shapes, and wallpapers live.', 'icon': '"\\U0001F4E6"', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'address', 'ty': 'string', 'required': True}, {'name': 'description', 'ty': 'text'}, {'name': 'enabled', 'ty': 'boolean'}, {'name': 'lastSynced', 'ty': 'datetime'}, {'name': 'scanner', 'ty': 'string'}, {'name': 'sourceId', 'ty': 'string'}], 'identity': ['address'], 'display': {'subtitle': 'sourceId'}},
    'spec': {'name': 'spec', 'plural': 'specs', 'description': 'A spec — a design document describing work to be done.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'labels', 'ty': 'stringlist'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'parentId', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'priority', 'ty': 'integer'}, {'name': 'problem', 'ty': 'text'}, {'name': 'projectId', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'remoteId', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'state', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'successCriteria', 'ty': 'text'}, {'name': 'target', 'ty': 'json'}, {'name': 'targetDate', 'ty': 'datetime'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['task', 'file'], 'display': {'subtitle': 'state', 'highlights': ['startDate', 'endDate', 'location']}},
    'step': {'name': 'step', 'plural': 'steps', 'description': 'One ordered act within a flow. A first-class node, not an array slot:', 'icon': 'list-ordered', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'detail', 'ty': 'text'}, {'name': 'position', 'ty': 'integer'}, {'name': 'status', 'ty': 'string'}], 'display': {'subtitle': 'status', 'body': 'detail', 'highlights': ['position', 'status']}},
    'symbol': {'name': 'symbol', 'plural': 'symbols', 'description': 'A code symbol — one named thing in a source surface: an MCP tool/op, a', 'icon': 'code', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'lang', 'ty': 'string'}, {'name': 'signature', 'ty': 'text'}, {'name': 'sourceLine', 'ty': 'integer'}, {'name': 'sourcePath', 'ty': 'string'}, {'name': 'summary', 'ty': 'text'}, {'name': 'urn', 'ty': 'string'}], 'display': {'subtitle': 'signature', 'body': 'summary', 'highlights': ['kind', 'lang', 'sourcePath']}},
    'tag': {'name': 'tag', 'plural': 'tags', 'description': 'A tag or label — Gmail label, Todoist label, GitHub label, git tag,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'annotated', 'ty': 'boolean'}, {'name': 'color', 'ty': 'string'}, {'name': 'hash', 'ty': 'string'}, {'name': 'tagType', 'ty': 'string'}], 'identity': ['name'], 'display': {'title': 'name', 'subtitle': 'tagType'}},
    'task': {'name': 'task', 'plural': 'tasks', 'description': 'A work item — issue, ticket, or to-do. Supports hierarchy (parent/children)', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'labels', 'ty': 'stringlist'}, {'name': 'parentId', 'ty': 'string'}, {'name': 'priority', 'ty': 'integer'}, {'name': 'projectId', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'remoteId', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'state', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'target', 'ty': 'json'}, {'name': 'targetDate', 'ty': 'datetime'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'state', 'highlights': ['startDate', 'endDate', 'location']}},
    'tax_line': {'name': 'tax_line', 'plural': 'tax_lines', 'description': 'A single tax, fee, or surcharge line item on a priced commerce', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'amount', 'ty': 'number'}, {'name': 'appliesToIndex', 'ty': 'integer'}, {'name': 'code', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'description', 'ty': 'string'}, {'name': 'inclusive', 'ty': 'boolean'}, {'name': 'kind', 'ty': 'string'}, {'name': 'merchantImposed', 'ty': 'boolean'}, {'name': 'nature', 'ty': 'string'}, {'name': 'rate', 'ty': 'number'}, {'name': 'refundable', 'ty': 'boolean'}, {'name': 'taxableAmount', 'ty': 'number'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'description'}},
    'theme': {'name': 'theme', 'plural': 'themes', 'description': "An OS theme — a named knob-vector over its family's structure.", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'defaultBackgroundColor', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'family', 'ty': 'string'}, {'name': 'startMenu', 'ty': 'string'}, {'name': 'style', 'ty': 'string'}, {'name': 'themeId', 'ty': 'string', 'required': True}], 'identity': ['themeId'], 'display': {'subtitle': 'family'}},
    'tool_call': {'name': 'tool_call', 'plural': 'tool_calls', 'description': 'A single tool invocation made by an agent during a message.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'input', 'ty': 'text'}, {'name': 'isError', 'ty': 'boolean'}, {'name': 'output', 'ty': 'text'}], 'identity': ['platform', 'id'], 'display': {'subtitle': 'name'}},
    'transaction': {'name': 'transaction', 'plural': 'transactions', 'description': 'A financial transaction — credit card charge, bank transfer, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'amount', 'ty': 'number'}, {'name': 'balance', 'ty': 'number'}, {'name': 'category', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'details', 'ty': 'json'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'notes', 'ty': 'string'}, {'name': 'pending', 'ty': 'boolean'}, {'name': 'postingDate', 'ty': 'datetime'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'recurring', 'ty': 'boolean'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'type', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'category', 'body': 'notes', 'highlights': ['amount', 'postingDate', 'currency']}},
    'transcript': {'name': 'transcript', 'plural': 'transcripts', 'description': 'A text transcript of audio/video content. Linked from meetings and videos.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'contentRole', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'language', 'ty': 'string'}, {'name': 'segmentCount', 'ty': 'integer'}, {'name': 'segments', 'ty': 'json'}, {'name': 'sourceType', 'ty': 'string'}], 'display': {'subtitle': 'language'}},
    'transition': {'name': 'transition', 'plural': 'transitions', 'description': 'An identity change — name, gender, religion, sports team, anything', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'additionalName', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'familyName', 'ty': 'string'}, {'name': 'gender', 'ty': 'string'}, {'name': 'givenName', 'ty': 'string'}, {'name': 'honorificPrefix', 'ty': 'string'}, {'name': 'honorificSuffix', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'legalName', 'ty': 'string'}, {'name': 'maidenName', 'ty': 'string'}, {'name': 'nameOrder', 'ty': 'string'}, {'name': 'nickname', 'ty': 'string'}, {'name': 'phoneticFamilyName', 'ty': 'string'}, {'name': 'phoneticGivenName', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sortAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'givenName', 'familyName', 'gender']}},
    'trip': {'name': 'trip', 'plural': 'trips', 'description': 'A directed journey from origin to destination — one direction of travel.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrivalTime', 'ty': 'datetime'}, {'name': 'bookingToken', 'ty': 'string'}, {'name': 'cabinClass', 'ty': 'string'}, {'name': 'carbonEmissions', 'ty': 'json'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureTime', 'ty': 'datetime'}, {'name': 'distance', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'string'}, {'name': 'durationMinutes', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'fare', 'ty': 'string'}, {'name': 'fareAmount', 'ty': 'number'}, {'name': 'guest', 'ty': 'json'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isPool', 'ty': 'boolean'}, {'name': 'isReserve', 'ty': 'boolean'}, {'name': 'isScheduled', 'ty': 'boolean'}, {'name': 'isSurge', 'ty': 'boolean'}, {'name': 'marketplace', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'rating', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'stops', 'ty': 'integer'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'trackingUrl', 'ty': 'url'}, {'name': 'tripType', 'ty': 'string'}, {'name': 'vehicle', 'ty': 'json'}, {'name': 'vehicleType', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'tripType', 'highlights': ['startDate', 'endDate', 'location']}},
    'unit': {'name': 'unit', 'plural': 'units', 'description': 'A unit of measure — a concrete scale for a quantity. mg/dL, USD, pascal,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'iso4217', 'ty': 'string'}, {'name': 'iso4217Numeric', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'label', 'ty': 'string'}, {'name': 'logBase', 'ty': 'number'}, {'name': 'minorExponent', 'ty': 'integer'}, {'name': 'qudtUnitIri', 'ty': 'string'}, {'name': 'siDigitalFrameworkUri', 'ty': 'string'}, {'name': 'symbol', 'ty': 'string'}, {'name': 'toBaseFactor', 'ty': 'number'}, {'name': 'toBaseOffset', 'ty': 'number'}, {'name': 'ucumCode', 'ty': 'string'}, {'name': 'unCefactCommonCode', 'ty': 'string'}, {'name': 'wikidataId', 'ty': 'string'}], 'identity_any': ['ucumCode', 'siDigitalFrameworkUri', 'iso4217'], 'display': {'subtitle': 'symbol'}},
    'user': {'name': 'user', 'plural': 'users', 'description': "An AgentOS user — the seat at this machine. Carries the user's", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'osUsername', 'ty': 'string'}, {'name': 'primaryUser', 'ty': 'boolean'}], 'also': ['actor'], 'identity_any': ['osUsername'], 'display': {'subtitle': 'name'}},
    'user_identity': {'name': 'user_identity', 'plural': 'user_identities', 'description': 'An identity claim — "the engine-level user X identifies as person:Y', 'icon': 'user', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'active', 'ty': 'boolean'}, {'name': 'person_node_id', 'ty': 'string'}, {'name': 'user_id', 'ty': 'string'}, {'name': 'volume_id', 'ty': 'string'}], 'display': {'subtitle': 'volume_id', 'highlights': ['person_node_id', 'active']}},
    'video': {'name': 'video', 'plural': 'videos', 'description': 'A video file — the media artifact, not the social context around it.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'codec', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'frameRate', 'ty': 'number'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'resolution', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'viewCount', 'ty': 'integer'}], 'also': ['creative_work', 'file'], 'display': {'subtitle': 'author', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}},
    'volume': {'name': 'volume', 'plural': 'volumes', 'description': 'A mounted Volume — any named source of typed nodes the engine has', 'icon': 'drive', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'address', 'ty': 'string'}, {'name': 'auto_mount', 'ty': 'boolean'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'freeBytes', 'ty': 'integer'}, {'name': 'icon', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'provider', 'ty': 'string'}, {'name': 'readOnly', 'ty': 'boolean'}, {'name': 'removable', 'ty': 'boolean'}, {'name': 'scope', 'ty': 'string'}, {'name': 'totalBytes', 'ty': 'integer'}, {'name': 'volume_id', 'ty': 'string'}], 'display': {'subtitle': 'kind'}},
    'webpage': {'name': 'webpage', 'plural': 'webpages', 'description': 'A web page. Base type for search result. Also used for browser history', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'contentType', 'ty': 'string'}, {'name': 'error', 'ty': 'string'}, {'name': 'favicon', 'ty': 'url'}, {'name': 'lastVisitUnix', 'ty': 'integer'}, {'name': 'visitCount', 'ty': 'integer'}], 'identity': ['url'], 'display': {'subtitle': 'url'}},
    'website': {'name': 'website', 'plural': 'websites', 'description': 'A published website (not a single page — see webpage for that).', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'anonymous', 'ty': 'boolean'}, {'name': 'claimToken', 'ty': 'string'}, {'name': 'claimUrl', 'ty': 'url'}, {'name': 'status', 'ty': 'string'}, {'name': 'versionId', 'ty': 'string'}], 'identity': ['url'], 'display': {'subtitle': 'url'}},
}

# Identity keys per shape — sidecars for the skill worker.
SHAPE_IDENTITIES: dict[str, list[str]] = {
    'account': ['at', 'identifier'],
    'aircraft': ['icaoCode'],
    'airline': ['iataCode'],
    'airport': ['iataCode'],
    'app': ['id'],
    'booking_offer': ['at', 'cartId'],
    'bookmark': ['points_to'],
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
    'aircraft': ['model', 'variant', 'seatCapacity', 'rangeKm', 'iataCode', 'icaoCode', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'airline': ['iataCode', 'icaoCode', 'callsign', 'country', 'alliance', 'industry', 'actorType'],
    'airport': ['iataCode', 'icaoCode', 'city', 'country', 'countryCode', 'timezone', 'elevationFt', 'terminalCount'],
    'app': ['id', 'name', 'iconRole', 'route', 'defaultView', 'isSystem', 'handles'],
    'birth': ['givenName', 'additionalName', 'familyName', 'honorificPrefix', 'honorificSuffix', 'legalName', 'maidenName', 'sortAs', 'nameOrder', 'phoneticGivenName', 'phoneticFamilyName', 'gender', 'nickname', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'book': ['isbn', 'isbn13', 'pages', 'genres', 'series', 'format', 'language', 'originalTitle', 'places', 'characters', 'awardsWon', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'coverage', 'tags', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'booking_offer': ['cartId', 'referenceNumber', 'status', 'preparedAt', 'presentedAt', 'approvedAt', 'expiresAt', 'currency', 'baseAmount', 'taxAmount', 'feesAmount', 'totalAmount', 'itineraryHash', 'signature', 'signatureAlg', 'signedBy', 'checkoutUrl', 'confirmEndpoint', 'isRefundable', 'isChangeable', 'hasVoidWindow', 'voidWindowEndsAt', 'conditions', 'blob', 'review', 'contactEmail', 'contactPhone', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'bookmark': ['name', 'handle'],
    'branch': ['commit', 'upstream', 'ahead', 'behind', 'isCurrent', 'isRemote'],
    'brand': ['tagline', 'country', 'primaryColor', 'textColor'],
    'calendar': ['calendarId', 'color', 'backgroundColor', 'foregroundColor', 'isPrimary', 'isReadonly', 'accessRole', 'source', 'timezone'],
    'change': ['kind', 'summary', 'status', 'path', 'phase', 'version'],
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
    'flow': ['goal', 'trigger', 'status'],
    'font': ['family', 'genericFamily', 'postscriptName', 'weights', 'styles', 'formats', 'scripts', 'glyphCount', 'designerUrl', 'vendorUrl', 'licenseInfoUrl', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags'],
    'git_commit': ['sha', 'shortHash', 'message', 'additions', 'deletions', 'filesChanged', 'committedAt', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'group': ['memberCount', 'category'],
    'health-biomarker': ['measure', 'category', 'loincCode', 'analyteType', 'description'],
    'health-condition': ['clinicalStatus', 'verificationStatus', 'proximity', 'bodySite', 'severity', 'snomedCode', 'icd10Code', 'clinicalArea', 'mitigation', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-immunization': ['dateAdministered', 'cvxCode', 'manufacturer', 'lotNumber', 'doseNumber', 'seriesDoses', 'site', 'route', 'diseaseTarget', 'notes', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-lab': ['cliaNumber', 'npi', 'ccn', 'labType', 'accreditation', 'industry', 'actorType'],
    'health-observation': ['value', 'valueText', 'refLow', 'refHigh', 'refText', 'flag', 'status', 'notes', 'indexedAt', 'resultType', 'favicon', 'externalUrl', 'postId', 'score', 'similarity', 'community', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-panel': ['panelCode', 'fasting', 'description', 'id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-procedure': ['performedDate', 'procedureType', 'bodySite', 'outcome', 'status', 'cptCode', 'snomedCode', 'findings', 'followUp', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-reference-range': ['low', 'high', 'unit', 'refText', 'category', 'provenance', 'method', 'ageLow', 'ageHigh', 'sex', 'pregnancy', 'gestationalAge', 'fasting', 'timeOfDay', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'icon': ['dimension', 'format', 'url', 'component', 'purpose', 'style', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'language', 'coverage', 'tags'],
    'image': ['width', 'height', 'format', 'altText', 'appName', 'windowId', 'displayId', 'displayIndex', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'encoding', 'lineCount', 'kind', 'sha'],
    'intellectual_property': ['category', 'mark', 'identifier', 'register', 'status', 'filingBasis', 'niceClass', 'validIn', 'renewalPeriod', 'verificationUrl'],
    'invitation': ['invitationType', 'email', 'role', 'status', 'token', 'acceptedAt', 'revokedAt', 'message', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'launch': ['flightNumber', 'rocketId', 'launchpadId', 'crewIds', 'reusedBoosters', 'landingOutcomes', 'articleUrl', 'webcastUrl', 'wikipediaUrl', 'patchImage', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'leg': ['sequence', 'departureTime', 'arrivalTime', 'duration', 'durationMinutes', 'flightNumber', 'cabinClass', 'vehicleType', 'layoverMinutes', 'carbonEmissions', 'trace', 'tracePointCount', 'polyline', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'list': ['id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path'],
    'loaded_model': ['size', 'quantization', 'vramUsage', 'sizeVram', 'digest', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'mcp_session': ['client', 'projectId', 'gitBranch', 'sessionType', 'startedAt', 'endedAt', 'messageCount', 'tokenCount'],
    'meeting': ['calendarLink', 'isVirtual', 'meetingUrl', 'conferenceProvider', 'phoneDialIn', 'meetingType', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'membership': ['status', 'tier', 'autoRenew', 'price', 'currency', 'billingType', 'useCount', 'guestPassQuantity', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'message': ['isOutgoing', 'isStarred', 'conversationId'],
    'milestone': ['reachedAt', 'criterion', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'model': ['contextLength', 'contextWindow', 'maxOutput', 'pricingInput', 'pricingOutput', 'modality', 'modelType', 'quantization', 'quantizationLevel', 'size', 'parameterSize', 'format', 'family', 'digest'],
    'module': ['name', 'role', 'path', 'version', 'status', 'planned'],
    'note': ['noteType', 'isPinned'],
    'offer': ['price', 'currency', 'offerType', 'availability', 'bookingToken', 'departureToken', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'order': ['orderId', 'orderDate', 'total', 'totalAmount', 'originalTotal', 'originalTotalAmount', 'savings', 'currency', 'status', 'deliveryDate', 'eta', 'subtotal', 'tipAmount', 'deliveryFee', 'taxes', 'summary', 'fareBreakdown', 'deliveryInstructions', 'interactionType', 'orderUuid', 'body', 'head', 'messages', 'timeline', 'itemStates', 'latestArrival', 'progress', 'progressTotal', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'organization': ['industry', 'actorType'],
    'outcome': ['statement', 'status', 'archived', 'metric', 'baseline', 'current', 'target'],
    'pass': ['status', 'quantity', 'purchasedQuantity', 'useCount', 'isAllDayPass', 'price', 'currency', 'ticketNumber', 'nameOnTicket', 'seatAssignment', 'boardingGroup', 'ticketClass', 'gate', 'terminal', 'checkinStatus', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'payment_method': ['identifier', 'type', 'subtype', 'brand', 'displayName', 'customDescription', 'holderName', 'last4', 'binRange', 'expMonth', 'expYear', 'expirationDate', 'currency', 'balance', 'fingerprint', 'isDefault', 'isPrimary', 'isExpired', 'isSelected', 'status', 'providerTokens', 'metadata'],
    'person': ['url', 'notes', 'about', 'actorType'],
    'persona': ['headline', 'who', 'goals', 'painPoints', 'reachesFor', 'quote'],
    'place': ['fullAddress', 'placeFormatted', 'streetNumber', 'street', 'neighborhood', 'locality', 'city', 'district', 'region', 'postalCode', 'country', 'countryCode', 'latitude', 'longitude', 'accuracy', 'featureType', 'categories', 'phone', 'website', 'hours', 'businessStatus', 'rating', 'reviewCount', 'priceLevel', 'timezone', 'eta', 'isOrderable', 'closedMessage', 'productCount', 'mapboxId', 'wikidataId', 'googlePlaceId'],
    'playlist': ['id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path'],
    'podcast': ['feedUrl'],
    'post': ['externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'practice': ['description', 'code', 'codeSystem', 'aliases'],
    'principle': ['name', 'statement', 'rationale', 'domain', 'status'],
    'product': ['category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'project': ['state', 'color', 'parentId'],
    'protocol': ['name', 'homepage', 'rfc', 'wikidataId'],
    'qualification': ['category', 'identifier', 'status', 'renewalPeriod', 'level', 'validIn', 'verificationUrl'],
    'quantity-kind': ['key', 'label'],
    'quote': ['context', 'year'],
    'repository': ['stars', 'forks', 'language', 'topics', 'openIssues', 'isArchived', 'isPrivate', 'defaultBranch', 'license', 'size'],
    'reservation': ['reservationType', 'reservationId', 'status', 'bookingType', 'bookingTime', 'modifiedTime', 'startTime', 'endTime', 'partySize', 'totalAmount', 'baseAmount', 'taxAmount', 'currency', 'checkinUrl', 'conditions', 'voidWindowEndsAt', 'availableActions', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'result': ['indexedAt', 'resultType', 'favicon', 'externalUrl', 'postId', 'score', 'similarity', 'community'],
    'review': ['rating', 'ratingMax', 'tags', 'isVerified', 'externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'role': ['title', 'department', 'roleType', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'seatmap': ['flightNumber', 'origin', 'destination', 'fareBasisCode', 'classOfService', 'aircraftCode', 'totalSeats', 'availableSeats', 'cabins', 'tiers', 'hasExitRow', 'hasFreeSeats', 'hasPaidSeats', 'basicEconomyLocked'],
    'shelf': ['isExclusive', 'id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path'],
    'skill': ['skillId', 'description', 'color', 'status', 'error'],
    'software': ['version', 'applicationCategory', 'runtimePlatform', 'codename', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'sound': ['durationMs', 'channels', 'sampleRate', 'bitDepth', 'purpose', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'source': ['sourceId', 'address', 'scanner', 'enabled', 'description', 'lastSynced'],
    'spec': ['problem', 'successCriteria', 'remoteId', 'priority', 'state', 'labels', 'targetDate', 'target', 'parentId', 'projectId', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'step': ['position', 'detail', 'status'],
    'symbol': ['urn', 'kind', 'lang', 'signature', 'summary', 'sourcePath', 'sourceLine'],
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
    'user_identity': ['user_id', 'volume_id', 'person_node_id', 'active'],
    'video': ['durationMs', 'resolution', 'frameRate', 'codec', 'viewCount', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'volume': ['volume_id', 'kind', 'address', 'provider', 'auto_mount', 'readOnly', 'removable', 'totalBytes', 'freeBytes', 'scope', 'icon', 'default_view'],
    'webpage': ['visitCount', 'lastVisitUnix', 'contentType', 'favicon', 'error'],
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
    'health-condition',
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
    'milestone',
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
# Binding grammar: {find, where, where_link, is, get} | {latest: [...]} | dotted string.
SHAPE_DERIVED: dict[str, dict] = {
    'person': {'birthdate': {'find': 'born_in', 'is': 'birth', 'get': 'startDate'}, 'current_residence': {'find': 'lived_at', 'where_link': {'to': None}, 'get': 'name'}, 'current_role': {'find': 'worked_at', 'where_link': {'to': None}, 'get': 'title'}, 'givenName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'givenName'}, {'find': 'changed', 'is': 'transition', 'get': 'givenName'}]}, 'additionalName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'additionalName'}, {'find': 'changed', 'is': 'transition', 'get': 'additionalName'}]}, 'familyName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'familyName'}, {'find': 'changed', 'is': 'transition', 'get': 'familyName'}]}, 'honorificPrefix': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificPrefix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificPrefix'}]}, 'honorificSuffix': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificSuffix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificSuffix'}]}, 'legalName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'legalName'}, {'find': 'changed', 'is': 'transition', 'get': 'legalName'}]}, 'maidenName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'maidenName'}, {'find': 'changed', 'is': 'transition', 'get': 'maidenName'}]}, 'sortAs': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'sortAs'}, {'find': 'changed', 'is': 'transition', 'get': 'sortAs'}]}, 'nameOrder': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nameOrder'}, {'find': 'changed', 'is': 'transition', 'get': 'nameOrder'}]}, 'phoneticGivenName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticGivenName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticGivenName'}]}, 'phoneticFamilyName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticFamilyName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticFamilyName'}]}, 'gender': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'gender'}, {'find': 'changed', 'is': 'transition', 'get': 'gender'}]}, 'nickname': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nickname'}, {'find': 'changed', 'is': 'transition', 'get': 'nickname'}]}},
}

# `shortcuts:` per shape — write-side flat-create expansion table.
# Each entry: flat_key -> {writes: <link>[is=<shape>].<field>}
SHAPE_SHORTCUTS: dict[str, dict] = {
    'person': {'birthdate': {'writes': 'born_in[is=birth].startDate'}, 'givenName': {'writes': 'born_in[is=birth].givenName'}, 'additionalName': {'writes': 'born_in[is=birth].additionalName'}, 'familyName': {'writes': 'born_in[is=birth].familyName'}, 'honorificPrefix': {'writes': 'born_in[is=birth].honorificPrefix'}, 'honorificSuffix': {'writes': 'born_in[is=birth].honorificSuffix'}, 'legalName': {'writes': 'born_in[is=birth].legalName'}, 'maidenName': {'writes': 'born_in[is=birth].maidenName'}, 'sortAs': {'writes': 'born_in[is=birth].sortAs'}, 'nameOrder': {'writes': 'born_in[is=birth].nameOrder'}, 'phoneticGivenName': {'writes': 'born_in[is=birth].phoneticGivenName'}, 'phoneticFamilyName': {'writes': 'born_in[is=birth].phoneticFamilyName'}, 'gender': {'writes': 'born_in[is=birth].gender'}, 'nickname': {'writes': 'born_in[is=birth].nickname'}},
}
